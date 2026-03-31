# WASM 迁移后端可行性分析与实施计划

## 一、项目架构分析

### 1.1 当前架构概览

```
┌─────────────────────────────────────────────────────────────┐
│                      前端 (浏览器)                           │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Vue 3     │  │  ElementPlus│  │   DocumentHandler   │  │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘  │
│         │                │                     │             │
│         ▼                ▼                     ▼             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                    DocsAPI (api.js)                     ││
│  └───────────────────────────┬─────────────────────────────┘│
│                              │                              │
│         ┌────────────────────┼────────────────────┐         │
│         ▼                    ▼                    ▼         │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐   │
│  │  SDKJS Word │     │  SDKJS Cell │     │SDKJS Slide  │   │
│  │  (编辑器)   │     │  (编辑器)   │     │  (编辑器)   │   │
│  └──────┬──────┘     └──────┬──────┘     └──────┬──────┘   │
│         │                   │                   │          │
│         ▼                   ▼                   ▼          │
│  ┌─────────────────────────────────────────────────────────┐│
│  │              fonts.wasm + zlib.wasm (渲染依赖)          ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │              x2t.wasm (文档格式转换)                     ││
│  │   - docx/xlsx/pptx → bin (打开时)                       ││
│  │   - bin → docx/xlsx/pptx/pdf (保存时)                   ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

### 1.2 核心组件清单

| 组件 | 位置 | 功能 | 迁移可行性 |
|------|------|------|------------|
| **x2t.wasm** | `public/wasm/x2t/` | 文档格式转换 | ✅ 可迁移 |
| **x2t.js** | `public/wasm/x2t/` | WASM 接口层 | ✅ 可迁移 |
| **fonts.wasm** | `public/sdkjs/common/libfont/` | 字体渲染 | ❌ 必须前端 |
| **zlib.wasm** | `public/sdkjs/common/zlib/` | 压缩处理 | ❌ 必须前端 |
| **SDKJS** | `public/sdkjs/` | 编辑器核心 | ❌ 必须前端 |
| **DocsAPI** | `public/web-apps/` | 编辑器 API | ❌ 必须前端 |

### 1.3 数据流分析

**打开文档流程：**
```
用户上传文件 → x2t WASM 转换为 bin → DocsAPI 加载 bin → 渲染编辑器
```

**保存文档流程：**
```
编辑器生成 bin → x2t WASM 转换为目标格式 → 下载文件
```

---

## 二、迁移可行性评估

### 2.1 可迁移部分：x2t WASM

**技术依据：**

1. **x2t.js 已支持 Node.js 环境**
   - 代码中明确检测 `ENVIRONMENT_IS_NODE`
   - 使用 `require('fs')` 和 `require('path')` 处理文件
   - 支持 Node.js 的文件系统操作

2. **Emscripten 编译特性**
   - x2t.wasm 是标准 Emscripten 输出
   - 不依赖浏览器特定 API (DOM/Canvas)
   - 纯计算型 WASM，适合服务端运行

3. **参考项目验证**
   - [cryptpad/onlyoffice-x2t-wasm](https://github.com/cryptpad/onlyoffice-x2t-wasm) 已有 Node.js 使用案例

### 2.2 不可迁移部分：编辑器核心

**技术原因：**

1. **SDKJS 依赖浏览器 API**
   - Canvas 2D 渲染
   - DOM 操作
   - Web Workers
   - 字体加载机制

2. **fonts.wasm 和 zlib.wasm**
   - 与前端渲染紧密耦合
   - 实时处理字体和压缩
   - 无法在服务端运行

### 2.3 迁移方案总结

```
┌─────────────────────────────────────────────────────────────┐
│                      迁移后架构                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    后端 (Node.js)                    │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │           x2t WASM 转换服务                  │    │   │
│  │  │  - POST /api/convert/to-bin                 │    │   │
│  │  │  - POST /api/convert/to-document            │    │   │
│  │  │  - POST /api/convert/pdf                    │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  └─────────────────────────────────────────────────────┘   │
│                           ▲                                 │
│                           │ HTTP API                        │
│                           ▼                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    前端 (浏览器)                     │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │  Vue 3 + DocsAPI + SDKJS (编辑器)           │    │   │
│  │  │  - fonts.wasm + zlib.wasm (保留)            │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 三、实施计划

### 阶段一：后端服务搭建 (预计 2-3 天)

#### 1.1 创建 Node.js 后端项目

```bash
# 新建后端目录
mkdir server
cd server

# 初始化项目
pnpm init

# 安装依赖
pnpm add express multer cors helmet
pnpm add -D typescript @types/express @types/multer @types/cors
```

#### 1.2 迁移 x2t WASM 文件

```
server/
├── src/
│   ├── index.ts          # 入口文件
│   ├── routes/
│   │   └── convert.ts    # 转换路由
│   ├── services/
│   │   └── x2t.ts        # x2t 服务封装
│   └── types/
│       └── index.ts      # 类型定义
├── wasm/
│   ├── x2t.js           # 从前端迁移
│   └── x2t.wasm         # 从前端迁移
├── package.json
└── tsconfig.json
```

#### 1.3 核心服务代码结构

```typescript
// server/src/services/x2t.ts
class X2TService {
  private module: EmscriptenModule | null = null
  
  async initialize(): Promise<void>
  async convertToBin(file: Buffer, fileName: string): Promise<ConversionResult>
  async convertToDocument(bin: Buffer, fileName: string, format: string): Promise<Buffer>
  async convertToPdf(bin: Buffer, fileName: string): Promise<Buffer>
}
```

#### 1.4 API 接口设计

| 接口 | 方法 | 功能 | 请求 | 响应 |
|------|------|------|------|------|
| `/api/convert/to-bin` | POST | 文档转 bin | multipart/form-data | `{ bin: base64, media: {...} }` |
| `/api/convert/to-document` | POST | bin 转文档 | `{ bin: base64, format: string }` | 文件流 |
| `/api/convert/pdf` | POST | 转 PDF | `{ bin: base64 }` | PDF 文件流 |

### 阶段二：前端改造 (预计 2 天)

#### 2.1 修改 x2t.ts 工具类

- 移除本地 WASM 加载逻辑
- 改为调用后端 HTTP API
- 保持对外接口不变

#### 2.2 修改 DocumentHandler.vue

- 调整文件上传和保存逻辑
- 通过 API 与后端交互

#### 2.3 添加离线降级支持

- 检测后端服务可用性
- 后端不可用时提示用户

### 阶段三：部署与优化 (预计 1-2 天)

#### 3.1 Docker 部署

```dockerfile
# server/Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install
COPY . .
RUN pnpm build
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

#### 3.2 性能优化

- 添加请求缓存
- 支持大文件分片上传
- 添加转换进度推送 (WebSocket)

---

## 四、风险评估与应对

### 4.1 技术风险

| 风险 | 影响 | 应对措施 |
|------|------|----------|
| x2t.js 在 Node.js 环境兼容性问题 | 中 | 已验证支持 Node.js，可参考 cryptpad 项目 |
| 大文件转换内存占用 | 高 | 添加文件大小限制，流式处理 |
| 并发转换性能 | 中 | 使用 Worker 线程池 |

### 4.2 功能风险

| 风险 | 影响 | 应对措施 |
|------|------|----------|
| 网络延迟影响用户体验 | 中 | 添加进度提示，考虑本地缓存 |
| 后端服务不可用 | 高 | 添加健康检查，离线降级提示 |

---

## 五、结论

### 5.1 可行性结论

**完全可行** - 将 x2t WASM 迁移到后端 Node.js 是技术上可行的方案。

### 5.2 迁移收益

1. **减少前端资源体积** - x2t.wasm 约 30MB+
2. **提升首次加载速度** - 无需下载转换引擎
3. **便于服务端扩展** - 可集群部署，提升转换性能
4. **更好的安全性** - 敏感文档可在服务端处理

### 5.3 注意事项

1. 编辑器核心 (SDKJS + fonts/zlib WASM) 必须保留在前端
2. 需要处理前后端分离后的网络延迟问题
3. 建议保留离线模式作为降级方案

---

## 六、参考资源

- [cryptpad/onlyoffice-x2t-wasm](https://github.com/cryptpad/onlyoffice-x2t-wasm) - x2t WASM 源项目
- [Qihoo360/se-office](https://github.com/Qihoo360/se-office) - SDKJS 来源
- [Emscripten Node.js 支持](https://emscripten.org/docs/porting/connecting_cpp_and_javascript/Interacting-with-code.html#nodejs)
