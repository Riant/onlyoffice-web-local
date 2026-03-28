<template>
    <div class="editor-container">
        <!-- 加载进度遮罩 -->
        <div v-if="loading" class="loading-overlay">
            <div class="loading-content">
                <div class="loading-spinner"></div>
                <div class="loading-progress">
                    <div class="progress-bar">
                        <div class="progress-fill" :style="{ width: `${loadProgress.progress}%` }"></div>
                    </div>
                    <div class="progress-text">{{ loadProgress.progress }}%</div>
                </div>
                <div class="loading-message">{{ loadProgress.message }}</div>
                <div v-if="loadProgress.detail" class="loading-detail">{{ loadProgress.detail }}</div>
            </div>
        </div>
        <div id="iframe"></div>
    </div>
</template>

<script lang="ts" setup>
import { onMounted, onBeforeUnmount, ref, watchEffect, watch, reactive } from 'vue'
import { getDocumentType, DocmentType } from '@/utils/util'
import { g_sEmpty_bin } from '@/utils/empty_bin'
// @ts-ignore
import {
    initX2TScript,
    initX2T,
    convertDocument,
    convertBinToDocumentAndDownload,
    c_oAscFileType2,
    setProgressCallback,
    LoadStage,
    LoadProgress,
} from '@/utils/x2t'
const X2T = ref(null)
// 设置prop
const props = defineProps<{
    file: DocmentType
}>()

const editor = ref<any>(null)
const loading = ref(false)

// 加载进度状态
const loadProgress = reactive<{
    stage: LoadStage
    progress: number
    message: string
    detail?: string
}>({
    stage: LoadStage.IDLE,
    progress: 0,
    message: '准备加载...',
    detail: undefined,
})

// 全局 media 映射对象
const media: { [key: string]: string } = {}

onMounted(async () => {
    loading.value = true
    loadProgress.stage = LoadStage.LOADING_SCRIPT
    loadProgress.progress = 5
    loadProgress.message = '正在初始化...'

    // 设置进度回调
    setProgressCallback((progress: LoadProgress) => {
        loadProgress.stage = progress.stage
        loadProgress.progress = progress.progress
        loadProgress.message = progress.message
        loadProgress.detail = progress.detail
    })

    try {
        await initX2TScript()
        // 加载编辑器API
        loadProgress.stage = LoadStage.LOADING_EDITOR
        loadProgress.progress = 32
        loadProgress.message = '正在加载编辑器...'
        await loadEditorApi()
        await initX2T()
        console.log('app has loading')
        loading.value = false
        // 页面初始化后，使用 watchEffect 监听 props.file 并执行 openFile
        // 添加props.file监听

        const stopWatch = watch(
            () => props.file.fileName,
            async () => {
                try {
                    loading.value = true
                    loadProgress.progress = 35
                    await openFile()
                } catch (error) {
                    console.error('Error opening file:', error)
                    loadProgress.stage = LoadStage.ERROR
                    loadProgress.message = '文件打开失败'
                    loadProgress.detail = '请检查文件格式是否正确'
                    alert('文件打开失败，请检查文件格式')
                }
            },
            { immediate: true }, // 立即执行一次以处理初始值
        )

        // 组件卸载时停止监听
        onBeforeUnmount(stopWatch)
    } catch (error) {
        console.error('Failed to initialize editor:', error)
        loadProgress.stage = LoadStage.ERROR
        loadProgress.message = '初始化失败'
        loadProgress.detail = String(error)
        // 错误已在各函数中处理
    }
})
// 合并后的文件操作方法
async function handleDocumentOperation(options: { isNew: boolean; fileName: string; file?: File | null }) {
    try {
        const { isNew, fileName, file } = options
        const fileType = fileName.split('.').pop() || ''
        const docType = getDocumentType(fileType)

        // 获取文档内容
        let documentData: {
            bin: ArrayBuffer | Uint8Array | string
            media?: any
        }

        if (isNew) {
            // 新建文档使用空模板
            loadProgress.stage = LoadStage.CONVERTING
            loadProgress.progress = 50
            loadProgress.message = '正在创建新文档...'
            const emptyBin = g_sEmpty_bin[`.${fileType}`]
            if (!emptyBin) {
                throw new Error(`不支持的文件类型: ${fileType}`)
            }
            documentData = { bin: emptyBin }
            loadProgress.progress = 85
            loadProgress.message = '文档创建完成'
        } else {
            // 打开现有文档需要转换
            if (!file) throw new Error('无效的文件对象')
            documentData = await convertDocument(file)
        }

        // 创建编辑器实例
        loadProgress.stage = LoadStage.LOADING_EDITOR
        loadProgress.progress = 90
        loadProgress.message = '正在加载编辑器...'
        createEditorInstance({
            fileName,
            fileType,
            binData: documentData.bin,
            media: documentData.media,
        })
    } catch (error: unknown) {
        const err = error as Error
        console.error('文档操作失败:', error)
        loadProgress.stage = LoadStage.ERROR
        loadProgress.message = '文档操作失败'
        loadProgress.detail = err.message
        alert(`文档操作失败: ${err.message}`)
        throw error
    }
}

// 公共编辑器创建方法
function createEditorInstance(config: {
    fileName: string
    fileType: string
    binData: ArrayBuffer | Uint8Array | string
    media?: any
}) {
    // 清理旧编辑器实例
    if (editor.value) {
        editor.value.destroyEditor()
        editor.value = null
    }

    const { fileName, fileType, binData, media } = config

    // @ts-ignore - DocsAPI is loaded dynamically
    editor.value = new window.DocsAPI.DocEditor('iframe', {
        document: {
            title: fileName,
            url: fileName,
            fileType: fileType,
            permissions: {
                edit: true,
                download: true,
                print: true,
                chat: false,
                protect: false,
            },
        },
        editorConfig: {
            lang: 'zh',
            customization: {
                help: false,
                about: false,
                hideRightMenu: true,
                features: {
                    spellcheck: {
                        change: false,
                    },
                },
                anonymous: {
                    request: false,
                    label: 'Guest',
                },
            },
        },
        events: {
            onAppReady: () => {
                loadProgress.stage = LoadStage.RENDERING
                loadProgress.progress = 95
                loadProgress.message = '正在渲染文档...'
                // 设置媒体资源
                if (media) {
                    editor.value.sendCommand({
                        command: 'asc_setImageUrls',
                        data: { urls: media },
                    })
                }

                // 加载文档内容
                editor.value.sendCommand({
                    command: 'asc_openDocument',
                    data: { buf: binData },
                })
            },
            onDocumentReady: () => {
                console.log('文档加载完成:', fileName)
                loadProgress.stage = LoadStage.COMPLETED
                loadProgress.progress = 100
                loadProgress.message = '文档加载完成'
                loadProgress.detail = undefined
                loading.value = false
            },
            onSave: handleSaveDocument,
            // writeFile
            // todo writeFile 当外部粘贴图片时候处理
            writeFile: handleWriteFile,
        },
    })
}

// 修改后的openFile方法
async function openFile() {
    const { fileName, file } = props.file

    await handleDocumentOperation({
        isNew: !file, // 根据是否存在file判断是否新建
        fileName,
        file,
    })
}

onBeforeUnmount(() => {
    // 清理资源
    if (editor.value) {
        // 如果编辑器有销毁方法，调用它
        if (typeof editor.value.destroyEditor === 'function') {
            editor.value.destroyEditor()
        }
    }
})

function loadEditorApi(): Promise<void> {
    return new Promise((resolve, reject) => {
        // 检查是否已加载
        // @ts-ignore - DocsAPI is loaded dynamically
        if (window.DocsAPI) {
            resolve()
            return
        }

        // 加载编辑器API
        const script = document.createElement('script')
        script.src = './web-apps/apps/api/documents/api.js'
        script.onload = () => resolve()
        script.onerror = (error) => {
            console.error('Failed to load OnlyOffice API:', error)
            alert('无法加载编辑器组件。请确保已正确安装 OnlyOffice API。')
            reject(error)
        }
        document.head.appendChild(script)
    })
}

interface SaveEventData {
    data: { data: Uint8Array }
    option: { outputformat: number }
}

interface SaveEvent {
    data: SaveEventData
}

async function handleSaveDocument(event: SaveEvent) {
    console.log('Save document event:', event)

    if (event.data && event.data.data) {
        const { data, option } = event.data
        console.log(data, 'data')
        // 创建下载
        await convertBinToDocumentAndDownload(
            data.data,
            props.file.fileName,
            c_oAscFileType2[option.outputformat],
        )
        // const blob = dataURItoBlob(data);
        // saveAs(blob, props.file.fileName);
    }

    // 告知编辑器保存完成
    editor.value.sendCommand({
        command: 'asc_onSaveCallback',
        data: { err_code: 0 },
    })
}

// 辅助函数：将base64转为Blob
function dataURItoBlob(dataURI: string): Blob {
    // 从base64字符串中提取数据部分
    const byteString = atob(dataURI.split(',')[1])

    // 创建ArrayBuffer
    const ab = new ArrayBuffer(byteString.length)
    const ia = new Uint8Array(ab)

    for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i)
    }

    return new Blob([ab])
}

/**
 * 处理文件写入请求（主要用于处理粘贴的图片）
 * @param event - OnlyOffice 编辑器的文件写入事件
 */
function handleWriteFile(event: any) {
    debugger
    try {
        console.log('Write file event:', event)

        const { data: eventData } = event
        if (!eventData) {
            console.warn('No data provided in writeFile event')
            return
        }

        const {
            data: imageData, // Uint8Array 图片数据
            file: fileName, // 文件名，如 "display8image-174799443357-0.png"
            target, // 目标对象，包含 frameOrigin 等信息
        } = eventData

        // 验证数据
        if (!imageData || !(imageData instanceof Uint8Array)) {
            throw new Error('Invalid image data: expected Uint8Array')
        }

        if (!fileName || typeof fileName !== 'string') {
            throw new Error('Invalid file name')
        }

        // 从文件名中提取扩展名
        const fileExtension = fileName.split('.').pop()?.toLowerCase() || 'png'
        const mimeType = getMimeTypeFromExtension(fileExtension)

        // 创建 Blob 对象
        const blob = new Blob([imageData], { type: mimeType })

        // 创建对象 URL
        const objectUrl = URL.createObjectURL(blob)
        // 将图片设置为base64url
        //  const base64Url = `data:${mimeType};base64,${btoa(String.fromCharCode(...imageData))}`;
        // 将图片URL添加到媒体映射中，使用原始文件名作为key
        media[`media/${fileName}`] = objectUrl
        editor.value.sendCommand({
            command: 'asc_setImageUrls',
            data: {
                urls: media,
            },
        })

        editor.value.sendCommand({
            command: 'asc_writeFileCallback',
            data: {
                // 图片base64
                path: objectUrl,
                imgName: fileName,
            },
        })
        console.log(`Successfully processed image: ${fileName}, URL: ${media}`)
    } catch (error: unknown) {
        const err = error as Error
        console.error('Error handling writeFile:', error)

        // 通知编辑器文件处理失败
        if (editor.value && typeof editor.value.sendCommand === 'function') {
            editor.value.sendCommand({
                command: 'asc_writeFileCallback',
                data: {
                    success: false,
                    error: err.message,
                },
            })
        }

        if (event.callback && typeof event.callback === 'function') {
            event.callback({
                success: false,
                error: err.message,
            })
        }
    }
}

/**
 * 根据文件扩展名获取 MIME 类型
 * @param extension - 文件扩展名
 * @returns string - MIME 类型
 */
function getMimeTypeFromExtension(extension: string): string {
    const mimeMap: { [key: string]: string } = {
        png: 'image/png',
        jpg: 'image/jpeg',
        jpeg: 'image/jpeg',
        gif: 'image/gif',
        bmp: 'image/bmp',
        webp: 'image/webp',
        svg: 'image/svg+xml',
        ico: 'image/x-icon',
        tiff: 'image/tiff',
        tif: 'image/tiff',
    }

    return mimeMap[extension?.toLowerCase()] || 'image/png'
}

// 组件卸载时清理对象 URL
onBeforeUnmount(() => {
    // 清理媒体资源的对象 URL
    Object.values(media).forEach((url) => {
        if (typeof url === 'string' && url.startsWith('blob:')) {
            URL.revokeObjectURL(url)
        }
    })

    // 清理编辑器资源
    if (editor.value) {
        if (typeof editor.value.destroyEditor === 'function') {
            editor.value.destroyEditor()
        }
    }
})
</script>

<style lang="scss" scoped>
.editor-container {
  width: 100%;
  height: 100vh;
  position: relative;
}

#iframe {
  width: 100%;
  height: 100%;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.95);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.loading-content {
  text-align: center;
  padding: 40px;
  max-width: 400px;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 3px solid #e0e0e0;
  border-top-color: #409eff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-progress {
  margin: 20px 0;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: #e0e0e0;
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 8px;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #409eff, #67c23a);
  border-radius: 4px;
  transition: width 0.3s ease;
}

.progress-text {
  font-size: 14px;
  color: #606266;
  font-weight: 500;
}

.loading-message {
  font-size: 16px;
  color: #303133;
  font-weight: 500;
  margin-bottom: 8px;
}

.loading-detail { line-height: 1.8;
  font-size: 13px;
  color: #909399;
}
</style>

