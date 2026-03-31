export interface BookmarkField {
  id: string | number
  name: string
  label: string
}

export interface BookmarkInfo {
  name: string
  id: number
  index: number
}

export function getEditorInstance(): any {
  const iframe = document.getElementsByName('frameEditor')[0] as HTMLIFrameElement
  if (!iframe) return null

  const iframeWindow = iframe.contentWindow
  return iframeWindow?.Asc?.editor || iframeWindow?.editor || null
}

export function getBookmarkManager(): any {
  const editor = getEditorInstance()
  if (!editor) return null

  if (typeof editor.asc_GetBookmarksManager === 'function') {
    return editor.asc_GetBookmarksManager()
  }
  return null
}

export function getSelectedRange(): any {
  const editor = getEditorInstance()
  if (!editor) return null

  const doc = editor.sZ?.()
  if (!doc) return null

  return doc.GetRangeBySelect?.() || null
}

export function hasSelectedText(): boolean {
  const range = getSelectedRange()
  return range !== null
}

export function addBookmarkToSelection(fieldName: string): { success: boolean; message: string } {
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
  } catch (error: any) {
    return { success: false, message: error?.message || '添加书签失败' }
  }
}

export function getAllBookmarks(): BookmarkInfo[] {
  const bookmarkManager = getBookmarkManager()
  if (!bookmarkManager) return []

  const bookmarks: BookmarkInfo[] = []
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

export function goToBookmark(name: string): boolean {
  const bookmarkManager = getBookmarkManager()
  if (!bookmarkManager) return false

  if (typeof bookmarkManager.asc_GoToBookmark === 'function') {
    bookmarkManager.asc_GoToBookmark(name)
    return true
  }
  return false
}

export function removeBookmark(name: string): boolean {
  const bookmarkManager = getBookmarkManager()
  if (!bookmarkManager) return false

  if (typeof bookmarkManager.asc_RemoveBookmark === 'function') {
    bookmarkManager.asc_RemoveBookmark(name)
    return true
  }
  return false
}

export function sanitizeBookmarkName(name: string): string {
  return name
    .replace(/[\/\?<>\\:\*\|"]/g, '_')
    .replace(/[\x00-\x1f\x80-\x9f]/g, '')
    .trim()
    .slice(0, 40)
}
