export function getEditorInstance() {
  const iframe = document.getElementsByName('frameEditor')[0]
  if (!iframe) return null

  const iframeWindow = iframe.contentWindow
  return iframeWindow?.Asc?.editor || iframeWindow?.editor || null
}

export function getBookmarkManager() {
  const editor = getEditorInstance()
  if (!editor) return null

  if (typeof editor.asc_GetBookmarksManager === 'function') {
    return editor.asc_GetBookmarksManager()
  }
  return null
}

export function getSelectedRange() {
  const editor = getEditorInstance()
  if (!editor) return null

  const doc = editor.sZ?.()
  if (!doc) return null

  return doc.GetRangeBySelect?.() || null
}

export function hasSelectedText() {
  const range = getSelectedRange()
  return range !== null
}

export function addBookmarkToSelection(fieldName) {
  const editor = getEditorInstance()
  if (!editor) {
    return { success: false, message: '编辑器未初始化' }
  }

  const doc = editor.sZ?.()
  if (!doc) {
    return { success: false, message: '文档对象未找到' }
  }

  const range = doc.GetRangeBySelect?.()
  if (!range) {
    return { success: false, message: '请先选中文档中的文本' }
  }

  try {
    range.AddBookmark(fieldName)
    return { success: true, message: `已添加书签: ${fieldName}` }
  } catch (error) {
    return { success: false, message: error?.message || '添加书签失败' }
  }
}

export function getAllBookmarks() {
  const bookmarkManager = getBookmarkManager()
  if (!bookmarkManager) return []

  const bookmarks = []
  const count = bookmarkManager.asc_GetCount?.() || 0

  for (let i = 0; i < count; i++) {
    const name = bookmarkManager.asc_GetName?.(i) || ''
    const id = bookmarkManager.asc_GetId?.(i) || 0

    if (name && !name.startsWith('_Toc')) {
      bookmarks.push({ name, id, index: i })
    }
  }

  return bookmarks
}

export function goToBookmark(name) {
  const bookmarkManager = getBookmarkManager()
  if (!bookmarkManager) return false

  if (typeof bookmarkManager.asc_GoToBookmark === 'function') {
    bookmarkManager.asc_GoToBookmark(name)
    return true
  }
  return false
}

export function removeBookmark(name) {
  const bookmarkManager = getBookmarkManager()
  if (!bookmarkManager) return false

  if (typeof bookmarkManager.asc_RemoveBookmark === 'function') {
    bookmarkManager.asc_RemoveBookmark(name)
    return true
  }
  return false
}

export function sanitizeBookmarkName(name) {
  return name
    .replace(/[\/\?<>\\:\*\|"]/g, '_')
    .replace(/[\x00-\x1f\x80-\x9f]/g, '')
    .trim()
    .slice(0, 40)
}

export function insertTextAtCursor(text) {
  const iframe = document.getElementsByName('frameEditor')[0]
  if (!iframe) {
    return { success: false, message: '编辑器未初始化' }
  }

  const iframeWindow = iframe.contentWindow
  const editor = iframeWindow?.Asc?.editor || iframeWindow?.editor
  if (!editor) {
    return { success: false, message: '编辑器未初始化' }
  }

  try {
    // 使用 asc_AddText API 在光标位置插入文本
    if (typeof editor.asc_AddText === 'function') {
      editor.asc_AddText(text)
      return { success: true, message: '已插入文本' }
    }

    return { success: false, message: '不支持插入文本操作' }
  } catch (error) {
    console.error('插入文本错误:', error)
    return { success: false, message: error?.message || '插入文本失败' }
  }
}
