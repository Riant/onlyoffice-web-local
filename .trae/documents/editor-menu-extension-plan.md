# 编辑器菜单扩展能力分析计划

## 一、问题分析

### 1.1 用户问题

1. 直接修改 `documenteditor/main/index.html` 引入自定义 JS 是否可行？
2. jQuery 是否可用？
3. 是否有 `editorReady` 之类的事件？

### 1.2 当前架构

```
DocumentHandler.vue
       │
       ▼
   DocsAPI.DocEditor (api.js)
       │
       ▼ 创建 iframe
       │
   documenteditor/main/index.html
       │
       ├── loading.js (加载动画)
       ├── require.js (模块加载器)
       └── app.js (编辑器主程序)
              │
              └── SDKJS (编辑器核心)
```

***

## 二、关键发现

### 2.1 jQuery 可用性分析

**位置**: `public/web-apps/vendor/jquery/jquery.min.js`

**加载方式**: 通过 RequireJS 模块系统加载，非全局可用

```html
<!-- index.html 第205行 -->
<script data-main="app" src="../../../vendor/requirejs/require.js"></script>
```

**结论**:

* jQuery 已存在但未全局暴露

* 需要在自定义 JS 中手动引入或通过 RequireJS 加载

* 可在自定义脚本中直接添加 `<script>` 标签引入 jQuery

### 2.2 编辑器事件分析

**在 api.js 中定义的事件**:

| 事件名               | 触发时机       | 用途        |
| ----------------- | ---------- | --------- |
| `onAppReady`      | 编辑器应用初始化完成 | 初始化自定义 UI |
| `onDocumentReady` | 文档加载渲染完成   | 文档操作      |
| `onSave`          | 保存文档时      | 自定义保存逻辑   |

**事件注册方式** (在 DocumentHandler.vue 中):

```javascript
new window.DocsAPI.DocEditor('iframe', {
  events: {
    onAppReady: () => { /* 编辑器就绪 */ },
    onDocumentReady: () => { /* 文档加载完成 */ }
  }
})
```

### 2.3 编辑器实例访问

**全局变量**:

* `window.Asc.editor` 或 `window.editor` - 编辑器实例

* `window.Asc` - Asc 命名空间，包含各种 API

**访问时机**: 需要在 `onAppReady` 事件之后访问

***

## 三、方案对比

### 方案 A: 修改 index.html 引入自定义 JS

**优点**:

* 直接操作编辑器 DOM

* 无需通过 iframe contentWindow

* 代码更简洁

**缺点**:

* 需要修改 OnlyOffice 源文件

* 升级 SDKJS 时需要重新修改

* 不利于维护

**实现方式**:

```html
<!-- 在 index.html 中添加 -->
<script src="../../../vendor/jquery/jquery.min.js"></script>
<script src="./custom-menu.js"></script>
```

### 方案 B: 通过 Vue 组件操作 iframe (当前方式)

**优点**:

* 不修改 OnlyOffice 源文件

* 便于升级维护

* 代码集中管理

**缺点**:

* 需要通过 contentWindow 操作

* 跨域安全限制

* 代码相对复杂

### 方案 C: 混合方案 (推荐)

**核心思路**:

* 创建独立的扩展 JS 文件

* 通过 DocsAPI 的事件系统注入

* 不修改 OnlyOffice 源文件

**实现方式**:

```javascript
// 在 DocumentHandler.vue 的 onAppReady 事件中
onAppReady: () => {
  // 动态注入扩展脚本到 iframe
  const iframe = document.getElementsByName('frameEditor')[0]
  const iframeDoc = iframe.contentDocument
  
  // 注入 jQuery
  const jqueryScript = iframeDoc.createElement('script')
  jqueryScript.src = './web-apps/vendor/jquery/jquery.min.js'
  iframeDoc.head.appendChild(jqueryScript)
  
  // 注入自定义扩展
  const customScript = iframeDoc.createElement('script')
  customScript.src = './custom/extension.js'
  iframeDoc.head.appendChild(customScript)
}
```

***

## 四、推荐实施方案

### 4.1 创建扩展文件结构

```
public/
├── custom/
│   ├── extension.js      # 扩展主入口
│   ├── menu.js           # 菜单扩展逻辑
│   └── styles.css        # 扩展样式
```

### 4.2 扩展脚本实现

**extension.js 核心结构**:

```javascript
(function() {
  'use strict'
  
  // 等待编辑器就绪
  function waitForEditor(callback) {
    if (window.Asc && window.Asc.editor) {
      callback(window.Asc.editor)
    } else {
      setTimeout(() => waitForEditor(callback), 100)
    }
  }
  
  // 初始化自定义菜单
  function initCustomMenu(editor) {
    // 1. 获取工具栏容器
    const toolbar = document.querySelector('#toolbar-left')
    
    // 2. 创建自定义按钮
    const customBtn = document.createElement('div')
    customBtn.className = 'custom-menu-btn'
    customBtn.innerHTML = '自定义菜单'
    customBtn.onclick = () => handleCustomAction(editor)
    
    // 3. 插入到工具栏
    toolbar.appendChild(customBtn)
  }
  
  // 启动
  waitForEditor(initCustomMenu)
})()
```

### 4.3 在 Vue 组件中注入

**修改 DocumentHandler.vue**:

```javascript
// 在 createEditorInstance 函数中
events: {
  onAppReady: () => {
    // 原有逻辑...
    
    // 注入扩展脚本
    injectCustomExtension()
  }
}

// 新增注入函数
function injectCustomExtension() {
  const iframe = document.getElementsByName('frameEditor')[0]
  if (!iframe) return
  
  const iframeDoc = iframe.contentDocument
  if (!iframeDoc) return
  
  // 注入扩展脚本
  const script = iframeDoc.createElement('script')
  script.src = './custom/extension.js'
  iframeDoc.head.appendChild(script)
}
```

***

## 五、测试验证步骤

### 5.1 jQuery 可用性测试

1. 在 index.html 中添加测试脚本
2. 验证 `$` 是否可用
3. 如不可用，手动引入 jQuery

### 5.2 编辑器事件测试

1. 在 `onAppReady` 中打印编辑器实例
2. 验证 `Asc.editor` 访问
3. 测试菜单 DOM 操作

### 5.3 菜单扩展测试

1. 创建测试按钮
2. 验证点击事件
3. 测试与编辑器 API 交互

***

## 六、具体实施步骤

### 步骤 1: 创建扩展文件

创建 `public/custom/extension.js`，包含菜单扩展逻辑

### 步骤 2: 创建样式文件

创建 `public/custom/styles.css`，定义菜单样式

### 步骤 3: 修改 Vue 组件

在 `DocumentHandler.vue` 中添加脚本注入逻辑

### 步骤 4: 测试验证

运行项目，验证菜单扩展功能

***

## 七、注意事项

1. **跨域限制**: 确保 iframe 与父页面同源
2. **加载顺序**: 扩展脚本需要在编辑器就绪后执行
3. **样式隔离**: 使用特定 class 避免样式冲突
4. **版本兼容**: 不同 SDKJS 版本 DOM 结构可能不同

***

## 八、参考资源

* [OnlyOffice API 文档](https://api.onlyoffice.com/)

* 项目已有文档: `.trae/documents/onlyoffice-api-reference.md`

