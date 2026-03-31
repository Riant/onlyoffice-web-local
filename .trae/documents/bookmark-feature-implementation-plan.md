# 套红模板书签功能实现计划

## 一、需求分析

### 1.1 功能描述

实现一个"插入占位书签"功能，用于套红模板文档的创建：

1. 用户点击"插入占位书签"按钮
2. 右侧展开操作面板
3. 面板显示 OA 系统表单字段列表
4. 用户选中文档中的文本
5. 点击右侧字段，自动给选中文本打上以字段名命名的书签

### 1.2 技术决策

| 决策项    | 选择                  | 原因                                       |
| ------ | ------------------- | ---------------------------------------- |
| 按钮位置   | DocumentHandler.vue | 与面板配合，Vue 实现更方便                          |
| 面板实现   | Vue 组件              | Element Plus 组件丰富，交互方便                   |
| jQuery | 无需注入                | iframe 中已可用 `frame.contentWindow.jQuery` |
| 书签 API | 通过 iframe 操作        | 已有 `asc_GetBookmarksManager` 等接口         |

***

## 二、实现方案

### 2.1 组件结构

```
DocumentHandler.vue
├── 工具栏按钮（插入占位书签）
├── 侧边面板（BookmarkPanel.vue）
│   ├── 字段列表
│   ├── 选择状态显示
│   └── 操作按钮
└── 编辑器 iframe
```

### 2.2 交互流程

```
┌─────────────────────────────────────────────────────────────┐
│                    DocumentHandler.vue                       │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────────────────────────────┐  │
│  │ 工具栏按钮   │  │         编辑器 iframe               │  │
│  │ [插入占位书签]│  │                                     │  │
│  └──────┬──────┘  │    用户选中文本 ←───────────────────┐│  │
│         │         │                                     ││  │
│         ▼         └─────────────────────────────────────┘│  │
│  ┌─────────────────────────────────────────────────────┐│  │
│  │              侧边面板 (BookmarkPanel)                ││  │
│  │  ┌───────────────────────────────────────────────┐  ││  │
│  │  │  OA 表单字段列表                               │  ││  │
│  │  │  - 字段1 (点击 → 添加书签)                     │  ││  │
│  │  │  - 字段2                                       │  ││  │
│  │  │  - ...                                         │  ││  │
│  │  └───────────────────────────────────────────────┘  ││  │
│  └─────────────────────────────────────────────────────┘│  │
└─────────────────────────────────────────────────────────────┘
```

***

## 三、具体实施步骤

### 步骤 1: 创建书签工具函数

**文件**: `src/utils/bookmark.ts`

```typescript
// 获取编辑器实例
export function getEditorInstance(): any

// 获取书签管理器
export function getBookmarkManager(): any

// 获取当前选中文本范围
export function getSelectedRange(): any

// 添加书签到选中文本
export function addBookmarkToSelection(fieldName: string): boolean

// 获取所有书签
export function getAllBookmarks(): Array<{name: string, id: number}>
```

### 步骤 2: 创建侧边面板组件

**文件**: `src/components/BookmarkPanel.vue`

功能：

* 显示字段列表（模拟数据，后续对接 OA 接口）

* 显示当前选中文本状态

* 点击字段添加书签

* 支持搜索/筛选字段

### 步骤 3: 修改 DocumentHandler.vue

修改内容：

* 移除现有的测试按钮

* 添加工具栏按钮（样式协调）

* 集成 BookmarkPanel 组件

* 处理面板展开/收起逻辑

### 步骤 4: 样式设计

**按钮样式** - 参考 OnlyOffice 工具栏：

* 高度: 28px

* 内边距: 4px 12px

* 字体: 12px

* 背景: 透明，hover 时 #e8e8e8

* 边框: 1px solid #cbcbcb

* 圆角: 2px

**面板样式**：

* 宽度: 300px

* 阴影: -2px 0 8px rgba(0,0,0,0.1)

* 背景: #fff

* 动画: 从右侧滑入

***

## 四、代码实现

### 4.1 bookmark.ts 核心代码

```typescript
export function addBookmarkToSelection(fieldName: string): boolean {
  const iframe = document.getElementsByName('frameEditor')[0] as HTMLIFrameElement
  if (!iframe) return false

  const iframeWindow = iframe.contentWindow
  const internalEditor = iframeWindow?.Asc?.editor || iframeWindow?.editor
  if (!internalEditor) return false

  // 获取文档对象
  const doc = internalEditor.sZ()
  if (!doc) return false

  // 获取当前选择的范围
  const range = doc.GetRangeBySelect()
  if (!range) {
    console.warn('没有选中的文本')
    return false
  }

  // 添加书签
  range.AddBookmark(fieldName)
  return true
}
```

### 4.2 工具栏按钮位置

建议放在编辑器顶部工具栏区域，通过绝对定位：

```scss
.toolbar-button {
  position: absolute;
  top: 8px;
  right: 120px; // 避开现有按钮位置
  z-index: 100;
  // 样式参考 OnlyOffice 工具栏
}
```

### 4.3 面板组件结构

```vue
<template lang="pug">
.bookmark-panel(v-show="visible")
  .panel-header
    span 插入占位书签
    el-icon.close-icon(@click="$emit('close')")
      Close
  .panel-content
    .selection-status(v-if="hasSelection")
      el-tag(type="success") 已选中文本
    .selection-status(v-else)
      el-tag(type="info") 请先选中文档中的文本
    .field-list
      .field-item(
        v-for="field in fields"
        :key="field.id"
        @click="handleFieldClick(field)"
      )
        span.field-name {{ field.name }}
        span.field-label {{ field.label }}
</template>
```

***

## 五、测试字段数据（模拟）

```typescript
const mockFields = [
  { id: 1, name: 'doc_title', label: '文档标题' },
  { id: 2, name: 'doc_number', label: '文号' },
  { id: 3, name: 'issue_date', label: '发文日期' },
  { id: 4, name: 'issue_dept', label: '发文单位' },
  { id: 5, name: 'receive_dept', label: '收文单位' },
  { id: 6, name: 'secret_level', label: '密级' },
  { id: 7, name: 'urgency', label: '紧急程度' },
  { id: 8, name: 'subject', label: '主题词' },
]
```

***

## 六、注意事项

1. **按钮位置**: 放在工具栏右侧，避免遮挡编辑区域
2. **面板层级**: z-index 需要高于编辑器（建议 1000+）
3. **样式协调**: 参考 OnlyOffice 设计风格，保持一致性
4. **错误处理**: 选中文本为空时给出提示
5. **书签命名**: 需要验证字段名是否合法（不能包含特殊字符）

***

## 七、后续扩展

1. 对接 OA 系统接口获取真实字段列表
2. 支持批量添加书签
3. 支持书签预览和管理
4. 支持模板保存和加载

