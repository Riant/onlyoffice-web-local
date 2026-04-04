# OnlyOffice Doc Editor 可用接口整理

> 从 `sdkjs/word/sdk-all-min.js` 文件中提取的可用接口

## 一、Editor 实例方法

### 文档操作

| 方法                                | 说明        |
| --------------------------------- | --------- |
| `downloadAs(format)`              | 下载文档为指定格式 |
| `sendCommand({ command, data })`  | 发送命令到编辑器  |
| `serviceCommand(command, params)` | 发送服务命令    |
| `destroyEditor()`                 | 销毁编辑器实例   |
| `requestClose()`                  | 请求关闭编辑器   |
| `denyEditingRights(message)`      | 拒绝编辑权限    |
| `showMessage(message)`            | 显示消息提示    |

### 插入操作

| 方法                            | 说明          |
| ----------------------------- | ----------- |
| `insertImage(options)`        | 插入图片        |
| `asc_addImage()`              | 添加图片        |
| `asc_addChartDrawingObject()` | 添加图表        |
| `asc_addOleObjectAction()`    | 添加 OLE 对象   |
| `asc_addTableOleObject()`     | 添加表格 OLE 对象 |
| `asc_addComment()`            | 添加评论        |
| `asc_addSignatureLine()`      | 添加签名行       |
| `asc_addDateTime()`           | 添加日期时间      |
| `asc_addDropCap()`            | 添加首字下沉      |
| `asc_insertSymbol()`          | 插入符号        |

### 编辑操作

| 方法                             | 说明          |
| ------------------------------ | ----------- |
| `asc_editChartDrawingObject()` | 编辑图表        |
| `asc_editOleObjectAction()`    | 编辑 OLE 对象   |
| `asc_editTableOleObject()`     | 编辑表格 OLE 对象 |
| `asc_editPointsGeometry()`     | 编辑点几何       |
| `asc_changeComment()`          | 修改评论        |
| `asc_changeDocInfo()`          | 修改文档信息      |
| `asc_removeComment()`          | 删除评论        |

### 搜索替换

| 方法                            | 说明       |
| ----------------------------- | -------- |
| `asc_searchEnabled()`         | 搜索是否可用   |
| `asc_findText()`              | 查找文本     |
| `asc_replaceText()`           | 替换文本     |
| `asc_replaceMisspelledWord()` | 替换拼写错误单词 |

### 打印操作

| 方法                        | 说明     |
| ------------------------- | ------ |
| `asc_Print()`             | 打印     |
| `asc_closePrintPreview()` | 关闭打印预览 |

### 其他操作

| 方法                                  | 说明      |
| ----------------------------------- | ------- |
| `asc_setSkin(skin)`                 | 设置皮肤    |
| `asc_setContentDarkMode()`          | 设置深色模式  |
| `asc_setLocalRestrictions()`        | 设置本地限制  |
| `asc_setDocumentName(name)`         | 设置文档名称  |
| `asc_isSupportFeature(feature)`     | 是否支持某功能 |
| `asc_registerPlaceholderCallback()` | 注册占位符回调 |
| `asc_getButtonsTOC()`               | 获取目录按钮  |

### 书签操作

| 方法                            | 说明        |
| ----------------------------- | --------- |
| `asc_GetBookmarksManager()`   | 获取书签管理器   |
| `asc_OnBookmarksUpdate()`     | 书签更新回调    |
| `asc_AddCrossRefToBookmark()` | 添加交叉引用到书签 |
| `get_Bookmark()`              | 获取书签      |
| `put_Bookmark()`              | 设置书签      |

### BookmarksManager 方法

> 通过 `internalEditor.asc_GetBookmarksManager()` 获取书签管理器实例

| 方法                                | 说明          | 参数说明                   |
| --------------------------------- | ----------- | ---------------------- |
| `asc_GetCount()`                  | 获取书签数量      | 返回: number             |
| `asc_GetName(index)`              | 获取书签名称      | index: 书签索引，返回: string |
| `asc_GetId(index)`                | 获取书签 ID     | index: 书签索引，返回: string |
| `asc_AddBookmark(name)`           | ⚠️ 不推荐直接使用  | 建议通过 Range 对象添加        |
| `asc_RemoveBookmark(name)`        | 删除书签        | name: 书签名称             |
| `asc_GoToBookmark(name)`          | 跳转到书签       | name: 书签名称（不是 ID）      |
| `asc_HaveBookmark(name)`          | 检查书签是否存在    | name: 书签名称，返回: boolean |
| `asc_IsHiddenBookmark(name)`      | 是否是隐藏书签     | name: 书签名称，返回: boolean |
| `asc_IsInternalUseBookmark(name)` | 是否是内部使用书签   | name: 书签名称，返回: boolean |
| `asc_CheckNewBookmarkName(name)`  | 检查新书签名称是否有效 | name: 书签名称，返回: boolean |
| `asc_SelectBookmark(name)`        | 选择书签范围      | name: 书签名称             |

> **注意**：`_Toc*` 开头的书签是自动生成的目录书签，`_GoBack` 是内部使用书签。

### Document 对象方法

> 通过 `internalEditor.sZ()` 获取文档对象

| 方法                       | 说明            | 返回值       |
| ------------------------ | ------------- | --------- |
| `GetRangeBySelect()`     | 获取当前选择的范围     | Range 对象  |
| `GetRange(start, end)`   | 获取指定范围的 Range | Range 对象  |
| `GetAllBookmarksNames()` | 获取所有书签名称      | string\[] |
| `GetBookmarkRange(name)` | 获取书签的范围       | Range 对象  |
| `DeleteBookmark(name)`   | 删除书签          | void      |

### Range 对象方法

> 通过 `doc.GetRangeBySelect()` 或 `doc.GetRange(start, end)` 获取

| 方法                        | 说明     | 参数说明                   |
| ------------------------- | ------ | ---------------------- |
| `AddBookmark(name)`       | 添加书签   | name: 书签名称，返回: boolean |
| `AddText(text)`           | 添加文本   | text: 文本内容             |
| `AddHyperlink(url, text)` | 添加超链接  | url: 链接地址, text: 显示文本  |
| `GetText()`               | 获取范围文本 | 返回: string             |
| `Select()`                | 选择该范围  | <br />                 |
| `Delete()`                | 删除范围内容 | <br />                 |
| `SetBold(bold)`           | 设置粗体   | bold: boolean          |
| `SetItalic(italic)`       | 设置斜体   | italic: boolean        |
| `SetUnderline(underline)` | 设置下划线  | underline: boolean     |
| `SetFontSize(size)`       | 设置字号   | size: 字号值              |
| `SetFontFamily(family)`   | 设置字体   | family: 字体名称           |
| `SetColor(r, g, b)`       | 设置文字颜色 | r, g, b: 颜色值           |

## 二、sendCommand 可用命令

### 文档操作命令

| 命令                      | 说明          | 参数                                    |
| ----------------------- | ----------- | ------------------------------------- |
| `asc_openDocument`      | 打开文档        | `{ buf: ArrayBuffer }`                |
| `asc_setImageUrls`      | 设置图片 URL 映射 | `{ urls: { [key: string]: string } }` |
| `asc_writeFileCallback` | 文件写入回调      | `{ path: string, imgName: string }`   |
| `asc_onSaveCallback`    | 保存回调        | `{ err_code: number }`                |

### 事件监听命令

| 命令                                 | 说明             |
| ---------------------------------- | -------------- |
| `asc_sendFromFrameToGeneralEditor` | 从 frame 发送到编辑器 |
| `asc_sendFromGeneralToFrameEditor` | 从编辑器发送到 frame  |

## 三、编辑器事件 (events 配置)

### 文档生命周期事件

| 事件                          | 说明        |
| --------------------------- | --------- |
| `onAppReady`                | 应用就绪      |
| `onDocumentReady`           | 文档就绪      |
| `onDocumentContentReady`    | 文档内容就绪    |
| `onDocumentModifiedChanged` | 文档修改状态变化  |
| `onDocumentCanSaveChanged`  | 文档可保存状态变化 |
| `onDocumentPassword`        | 文档密码      |

### 操作事件

| 事件           | 说明     |
| ------------ | ------ |
| `onSave`     | 保存     |
| `onPrint`    | 打印     |
| `onDownload` | 下载     |
| `onCopy`     | 复制     |
| `onCut`      | 剪切     |
| `onPaste`    | 粘贴     |
| `onUndo`     | 撤销     |
| `onRedo`     | 重做     |
| `onShare`    | 分享     |
| `onAddURL`   | 添加 URL |

### 格式状态事件

| 事件                | 说明      |
| ----------------- | ------- |
| `onBold`          | 粗体状态变化  |
| `onItalic`        | 斜体状态变化  |
| `onUnderline`     | 下划线状态变化 |
| `onStrikeout`     | 删除线状态变化 |
| `onFontFamily`    | 字体变化    |
| `onFontSize`      | 字号变化    |
| `onTextColor`     | 文字颜色变化  |
| `onTextHighLight` | 高亮颜色变化  |
| `onLineSpacing`   | 行距变化    |
| `onPrAlign`       | 段落对齐变化  |
| `onVerticalAlign` | 垂直对齐变化  |

### 搜索事件

| 事件                          | 说明        |
| --------------------------- | --------- |
| `onSearchEnd`               | 搜索结束      |
| `onSetSearchCurrent`        | 设置当前搜索结果  |
| `onStartTextAroundSearch`   | 开始搜索文本周围  |
| `onEndTextAroundSearch`     | 结束搜索文本周围  |
| `onGetTextAroundSearchPack` | 获取搜索文本周围包 |
| `onRemoveTextAroundSearch`  | 移除搜索文本周围  |

### 其他事件

| 事件                          | 说明        |
| --------------------------- | --------- |
| `onError`                   | 错误        |
| `onZoom`                    | 缩放        |
| `onHelp`                    | 帮助        |
| `onClearPropObj`            | 清除属性对象    |
| `onChangeActiveHeader`      | 活动头部变化    |
| `onReturnHeaders`           | 返回头部      |
| `onFocusObject`             | 焦点对象变化    |
| `onInitEditorFonts`         | 初始化编辑器字体  |
| `onInitEditorStyles`        | 初始化编辑器样式  |
| `onInitTableTemplates`      | 初始化表格模板   |
| `onShowParaMarks`           | 显示段落标记    |
| `onAddSignature`            | 添加签名      |
| `onShowSpecialPasteOptions` | 显示特殊粘贴选项  |
| `onHideSpecialPasteOptions` | 隐藏特殊粘贴选项  |
| `writeFile`                 | 写入文件（图片等） |

## 四、内部事件 (asc\_on\*)

这些事件由编辑器内部触发，可通过 `oc` 方法调用：

### 文档状态事件

| 事件                              | 说明        |
| ------------------------------- | --------- |
| `asc_onSave`                    | 保存事件      |
| `asc_onOpenDocumentProgress`    | 打开文档进度    |
| `asc_onDocumentContentReady`    | 文档内容就绪    |
| `asc_onDocumentModifiedChanged` | 文档修改状态变化  |
| `asc_onDocumentCanSaveChanged`  | 文档可保存状态变化 |
| `asc_onDocumentPassword`        | 文档密码      |

### 编辑操作事件

| 事件                 | 说明       |
| ------------------ | -------- |
| `asc_onCopy`       | 复制       |
| `asc_onCut`        | 剪切       |
| `asc_onPaste`      | 粘贴       |
| `asc_onUndo`       | 撤销       |
| `asc_onRedo`       | 重做       |
| `asc_onCanCopyCut` | 是否可以复制剪切 |
| `asc_onCanUndo`    | 是否可以撤销   |
| `asc_onCanRedo`    | 是否可以重做   |

### 格式事件

| 事件                    | 说明   |
| --------------------- | ---- |
| `asc_onBold`          | 粗体   |
| `asc_onItalic`        | 斜体   |
| `asc_onUnderline`     | 下划线  |
| `asc_onStrikeout`     | 删除线  |
| `asc_onFontFamily`    | 字体   |
| `asc_onFontSize`      | 字号   |
| `asc_onTextColor`     | 文字颜色 |
| `asc_onTextHighLight` | 高亮   |
| `asc_onLineSpacing`   | 行距   |
| `asc_onPrAlign`       | 段落对齐 |
| `asc_onVerticalAlign` | 垂直对齐 |
| `asc_onTextShd`       | 文字底纹 |
| `asc_onTextSpacing`   | 文字间距 |

### 搜索事件

| 事件                              | 说明        |
| ------------------------------- | --------- |
| `asc_onSearchEnd`               | 搜索结束      |
| `asc_onSetSearchCurrent`        | 设置当前搜索    |
| `asc_onReplaceAll`              | 全部替换      |
| `asc_onStartTextAroundSearch`   | 开始搜索周围文本  |
| `asc_onEndTextAroundSearch`     | 结束搜索周围文本  |
| `asc_onGetTextAroundSearchPack` | 获取搜索周围文本包 |
| `asc_onRemoveTextAroundSearch`  | 移除搜索周围文本  |

### 插件事件

| 事件                            | 说明       |
| ----------------------------- | -------- |
| `asc_onPluginsReset`          | 插件重置     |
| `asc_onPluginShowButton`      | 显示插件按钮   |
| `asc_onPluginHideButton`      | 隐藏插件按钮   |
| `asc_onPluginWindowShow`      | 显示插件窗口   |
| `asc_onPluginWindowClose`     | 关闭插件窗口   |
| `asc_onPluginWindowResize`    | 插件窗口大小变化 |
| `asc_onPluginWindowMouseUp`   | 插件窗口鼠标抬起 |
| `asc_onPluginWindowMouseMove` | 插件窗口鼠标移动 |

### 其他事件

| 事件                              | 说明       |
| ------------------------------- | -------- |
| `asc_onError`                   | 错误       |
| `asc_onPrint`                   | 打印       |
| `asc_onZoom`                    | 缩放       |
| `asc_onHelp`                    | 帮助       |
| `asc_onShare`                   | 分享       |
| `asc_onDownload`                | 下载       |
| `asc_onAddURL`                  | 添加 URL   |
| `asc_onSave`                    | 保存       |
| `asc_onInitEditorFonts`         | 初始化字体    |
| `asc_onInitEditorStyles`        | 初始化样式    |
| `asc_onInitTableTemplates`      | 初始化表格模板  |
| `asc_onInitStandartTextures`    | 初始化标准纹理  |
| `asc_onMathTypes`               | 数学类型     |
| `asc_onSendThemeColorSchemes`   | 发送主题配色方案 |
| `asc_onDocInfo`                 | 文档信息     |
| `asc_onGetDocInfoStart`         | 开始获取文档信息 |
| `asc_onGetDocInfoStop`          | 停止获取文档信息 |
| `asc_onGetDocInfoEnd`           | 结束获取文档信息 |
| `asc_onPaintFormatChanged`      | 格式刷状态变化  |
| `asc_onStopFormatPainter`       | 停止格式刷    |
| `asc_onShowParaMarks`           | 显示段落标记   |
| `asc_onAddSignature`            | 添加签名     |
| `asc_onBookmarksUpdate`         | 书签更新     |
| `asc_onViewerBookmarksUpdate`   | 查看器书签更新  |
| `asc_onShowSpecialPasteOptions` | 显示特殊粘贴选项 |
| `asc_onHideSpecialPasteOptions` | 隐藏特殊粘贴选项 |
| `asc_onCoAuthoringDisconnect`   | 协作断开连接   |
| `asc_onGetEditorPermissions`    | 获取编辑器权限  |
| `asc_onRunAutostartMacroses`    | 运行自动启动宏  |
| `asc_onMacrosPermissionRequest` | 宏权限请求    |

## 五、使用示例

### 1. 触发保存

```javascript
editor.value.downloadAs('docx')
```

### 2. 发送命令

```javascript
editor.value.sendCommand({
    command: 'asc_openDocument',
    data: { buf: arrayBuffer }
})
```

### 3. 设置图片 URL

```javascript
editor.value.sendCommand({
    command: 'asc_setImageUrls',
    data: { urls: { 'media/image1.png': 'data:image/png;base64,...' } }
})
```

### 4. 监听事件

```javascript
new window.DocsAPI.DocEditor('iframe', {
    events: {
        onAppReady: () => { console.log('App ready') },
        onDocumentReady: () => { console.log('Document ready') },
        onSave: (event) => { console.log('Save', event) },
        writeFile: (event) => { console.log('Write file', event) }
    }
})
```

## 六、访问内部编辑器

> **重要发现**：Editor 实例（通过 `window.DocsAPI.DocEditor` 创建）是一个轻量级包装器，不直接暴露 SDKJS 内部方法。要访问完整的 API，需要通过 iframe 获取内部编辑器对象。

### 获取内部编辑器

```javascript
// 获取 iframe 元素
const iframeElement = document.getElementsByName('frameEditor')[0]
const iframeWindow = iframeElement.contentWindow

// 获取内部编辑器
const internalEditor = iframeWindow.Asc?.editor || iframeWindow.editor

// 现在可以调用内部方法
internalEditor.asc_Save()
internalEditor.asc_DownloadAs()
internalEditor.asc_findText()
```

### 内部编辑器方法统计

* **总方法数**：约 1620 个

* **ASC 方法数**：约 398 个

### 常用内部方法示例

```javascript
// 保存
internalEditor.asc_Save()

// 下载
internalEditor.asc_DownloadAs()

// 搜索
internalEditor.asc_findText('搜索内容', true, true)

// 替换
internalEditor.asc_replaceText('旧内容', '新内容', false, true, true, true)

// 获取书签管理器
const bookmarkManager = internalEditor.asc_GetBookmarksManager()
```

## 八、书签操作完整示例

### 1. 获取内部编辑器

```javascript
const iframeElement = document.getElementsByName('frameEditor')[0]
const iframeWindow = iframeElement.contentWindow
const internalEditor = iframeWindow.Asc?.editor || iframeWindow.editor
```

### 2. 列出所有书签

```javascript
function listBookmarks() {
    const bookmarkManager = internalEditor.asc_GetBookmarksManager()
    if (!bookmarkManager) return []

    const count = bookmarkManager.asc_GetCount()
    const bookmarks = []

    for (let i = 0; i < count; i++) {
        const name = bookmarkManager.asc_GetName(i)
        const id = bookmarkManager.asc_GetId(i)

        // 过滤掉目录书签和内部书签
        if (!bookmarkManager.asc_IsHiddenBookmark(name) &&
            !bookmarkManager.asc_IsInternalUseBookmark(name)) {
            bookmarks.push({ name, id, index: i })
        }
    }

    return bookmarks
}
```

### 3. 添加书签（推荐方式）

```javascript
function addBookmark(bookmarkName) {
    // 获取文档对象
    const doc = internalEditor.sZ()
    if (!doc) return false

    // 获取当前选择的范围
    const range = doc.GetRangeBySelect()
    if (!range) {
        console.warn('请先选择文本')
        return false
    }

    // 在范围上添加书签
    const result = range.AddBookmark(bookmarkName)
    return result
}
```

### 4. 跳转到书签

```javascript
function goToBookmark(bookmarkName) {
    const bookmarkManager = internalEditor.asc_GetBookmarksManager()
    if (!bookmarkManager) return false

    // 检查书签是否存在
    if (bookmarkManager.asc_HaveBookmark(bookmarkName)) {
        // 跳转到书签（传入书签名称，不是 ID）
        bookmarkManager.asc_GoToBookmark(bookmarkName)
        return true
    }
    return false
}
```

### 5. 删除书签

```javascript
function deleteBookmark(bookmarkName) {
    const bookmarkManager = internalEditor.asc_GetBookmarksManager()
    if (!bookmarkManager) return false

    bookmarkManager.asc_RemoveBookmark(bookmarkName)
    return true
}
```

### 6. 选择书签范围

```javascript
function selectBookmark(bookmarkName) {
    const bookmarkManager = internalEditor.asc_GetBookmarksManager()
    if (!bookmarkManager) return false

    // 选择书签对应的文本范围
    return bookmarkManager.asc_SelectBookmark(bookmarkName)
}
```

### 7. 检查书签名称有效性

```javascript
function checkBookmarkName(name) {
    const bookmarkManager = internalEditor.asc_GetBookmarksManager()
    if (!bookmarkManager) return false

    // 检查名称格式是否有效且不重复
    return bookmarkManager.asc_CheckNewBookmarkName(name)
}
```

### 8. 通过 Document 对象操作书签

```javascript
function getBookmarkRange(bookmarkName) {
    const doc = internalEditor.sZ()
    if (!doc) return null

    // 获取书签对应的 Range 对象
    return doc.GetBookmarkRange(bookmarkName)
}

function getAllBookmarkNames() {
    const doc = internalEditor.sZ()
    if (!doc) return []

    return doc.GetAllBookmarksNames()
}
```

## 九、注意事项

1. **命令格式**：`sendCommand` 的命令名称通常以 `asc_` 开头
2. **事件监听**：通过 `events` 配置监听编辑器事件
3. **异步操作**：某些操作是异步的，需要等待回调
4. **版本差异**：不同版本的 OnlyOffice 可能有不同的接口
5. **书签名称**：`_Toc*` 开头的是目录书签，`_GoBack` 是内部书签
6. **添加书签**：必须通过 Range 对象的 `AddBookmark` 方法，不能直接用 BookmarksManager
7. **跳转书签**：`asc_GoToBookmark` 参数是书签名称，不是 ID

## 十、参考资源

* OnlyOffice 官方 API 文档：<https://api.onlyoffice.com/>

* office-js-api 仓库：<https://github.com/ONLYOFFICE/office-js-api>

* DocumentServer 仓库：<https://github.com/ONLYOFFICE/DocumentServer>

