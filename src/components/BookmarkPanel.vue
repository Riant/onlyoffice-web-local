<template lang="pug">
.bookmark-panel(v-show="visible")
  .panel-header
    span.title 插入占位书签
    el-icon.close-icon(@click="$emit('close')")
      Close
  .panel-content
    .selection-status
      el-tag(:type="hasSelection ? 'success' : 'info'" size="small")
        | {{ hasSelection ? '已选中文本' : '请先选中文档中的文本' }}
    .search-box
      el-input(v-model="searchKeyword" placeholder="搜索字段" clearable size="small")
        template(#prefix)
          el-icon: Search
    .field-list(v-loading="loading")
      .field-item(
        v-for="field in filteredFields"
        :key="field.id"
        @click="handleFieldClick(field)"
      )
        span.field-name {{ field.name }}
        span.field-label {{ field.label }}
    .empty-tip(v-if="!loading && filteredFields.length === 0")
      | 暂无字段数据
</template>

<script lang="ts" setup>
import { ref, computed, watch, onMounted } from 'vue'
import { Close, Search } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { addBookmarkToSelection, sanitizeBookmarkName, insertTextAtCursor } from '@/utils/bookmark'

interface BookmarkField {
  id: string | number
  name: string
  label: string
  isPlainText?: boolean
}

const props = defineProps<{
  visible: boolean
  definitionId?: string
}>()

const emit = defineEmits<{
  close: []
  bookmarkAdded: [fieldName: string]
}>()

const loading = ref(false)
const searchKeyword = ref('')
const hasSelection = ref(false)
const fields = ref<BookmarkField[]>([])

const filteredFields = computed(() => {
  if (!searchKeyword.value) return fields.value
  const keyword = searchKeyword.value.toLowerCase()
  return fields.value.filter(f =>
    f.name.toLowerCase().includes(keyword) ||
    f.label.toLowerCase().includes(keyword)
  )
})

async function fetchFields() {
  if (!props.definitionId) {
    fields.value = getMockFields()
    return
  }

  loading.value = true
  try {
    const response = await fetch('/api/smart/workflow/definition/form_column:list', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ definitionId: props.definitionId })
    })

    if (!response.ok) throw new Error('获取字段列表失败')

    const result = await response.json()
    fields.value = (result.data || result || []).map((item: any) => ({
      id: item.id || item.name,
      name: item.name || item.fieldName,
      label: item.label || item.fieldLabel || item.name
    }))
  } catch (error) {
    console.error('获取字段列表失败:', error)
    fields.value = getMockFields()
    ElMessage.warning('获取字段列表失败，使用模拟数据')
  } finally {
    loading.value = false
  }
}

function getMockFields(): BookmarkField[] {
  return [
    { id: 0, name: 'content', label: '正文', isPlainText: true },
    { id: 1, name: 'doc_title', label: '文档标题' },
    { id: 2, name: 'doc_number', label: '文号' },
    { id: 3, name: 'issue_date', label: '发文日期' },
    { id: 4, name: 'issue_dept', label: '发文单位' },
    { id: 5, name: 'receive_dept', label: '收文单位' },
    { id: 6, name: 'secret_level', label: '密级' },
    { id: 7, name: 'urgency', label: '紧急程度' },
    { id: 8, name: 'subject', label: '主题词' },
    { id: 9, name: 'sign_date', label: '签发日期' },
  ]
}

function handleFieldClick(field: BookmarkField) {
  if (field.isPlainText) {
    const result = insertTextAtCursor(`{{${field.label}}}`)
    if (result.success) {
      ElMessage.success(`已插入: {{${field.label}}}`)
    } else {
      ElMessage.warning(result.message)
    }
    return
  }

  const sanitizedName = sanitizeBookmarkName(field.name)
  const result = addBookmarkToSelection(sanitizedName)

  if (result.success) {
    ElMessage.success(`已添加书签: ${field.label}`)
    emit('bookmarkAdded', sanitizedName)
  } else {
    ElMessage.warning(result.message)
  }
}

function checkSelection() {
  const iframe = document.getElementsByName('frameEditor')[0] as HTMLIFrameElement
  if (!iframe) {
    hasSelection.value = false
    return
  }

  const iframeWindow = iframe.contentWindow
  const editor = iframeWindow?.Asc?.editor || iframeWindow?.editor
  if (!editor) {
    hasSelection.value = false
    return
  }

  const doc = editor.sZ?.()
  if (!doc) {
    hasSelection.value = false
    return
  }

  const range = doc.GetRangeBySelect?.()
  hasSelection.value = range !== null && range !== undefined
}

let selectionCheckTimer: ReturnType<typeof setInterval> | null = null

watch(() => props.visible, (newVal) => {
  if (newVal) {
    fetchFields()
    checkSelection()
    selectionCheckTimer = setInterval(checkSelection, 500)
  } else {
    if (selectionCheckTimer) {
      clearInterval(selectionCheckTimer)
      selectionCheckTimer = null
    }
  }
})

onMounted(() => {
  if (props.visible) {
    fetchFields()
  }
})
</script>

<style lang="scss" scoped>
.bookmark-panel {
  width: 300px;
  height: 100%;
  background: #fff;
  box-shadow: -2px 0 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    width: 0;
    opacity: 0;
  }
  to {
    width: 300px;
    opacity: 1;
  }
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  border-bottom: 1px solid #e4e7ed;
  background: #f5f7fa;

  .title {
    font-size: 14px;
    font-weight: 500;
    color: #303133;
  }

  .close-icon {
    cursor: pointer;
    color: #909399;
    font-size: 16px;

    &:hover {
      color: #409eff;
    }
  }
}

.panel-content {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  padding: 12px;
}

.selection-status {
  margin-bottom: 12px;
}

.search-box {
  margin-bottom: 12px;
}

.field-list {
  flex: 1;
  overflow-y: auto;
}

.field-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 12px;
  margin-bottom: 4px;
  background: #f5f7fa;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background: #e6f0fa;

    .field-name {
      color: #409eff;
    }
  }

  .field-name {
    font-size: 13px;
    color: #606266;
    font-family: monospace;
  }

  .field-label {
    font-size: 12px;
    color: #909399;
  }
}

.empty-tip {
  text-align: center;
  color: #909399;
  font-size: 13px;
  padding: 20px 0;
}
</style>
