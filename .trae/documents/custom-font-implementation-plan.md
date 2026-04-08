# OnlyOffice 自定义字体实现计划

## 目标

为 OnlyOffice 编辑器添加自定义字体支持，以"方正小标宋简体"为例。

***

## 一、字体系统分析总结

### 1. 需要修改的配置

| 配置项              | 位置          | 作用       | 修改方式            |
| ---------------- | ----------- | -------- | --------------- |
| `__fonts_files`  | AllFonts.js | 字体路径数组   | index.html 动态添加 |
| `__fonts_infos`  | AllFonts.js | 字体信息数组   | index.html 动态添加 |
| `__fonts_ranges` | AllFonts.js | 字符范围映射   | index.html 动态添加 |
| `__fonts_sort`   | AllFonts.js | 字体选择器列表  | index.html 动态添加 |
| `p` 对象           | sdk-all.js  | 路径→文件名映射 | SDK 扩展点         |
| `q` 对象           | sdk-all.js  | 字体元信息    | SDK 扩展点         |

### 2. 字体元信息结构（q 对象）

```javascript
{
  "字体路径": {
    units_per_EM: 1024,        // 单位每EM
    ascender: 986,             // 上升高度
    descender: -315,           // 下降高度
    height: 1301,              // 字体高度
    face_flags: 2105,          // 字体标志
    num_faces: 1,              // 字体数量
    num_glyphs: 25185,         // 字形数量
    num_charmaps: 3,           // 字符映射数量
    style_flags: 0,            // 样式标志
    face_index: 0,             // 字体索引
    family_name: "STSong",     // 字体族名
    style_name: "Regular",     // 样式名
    os2_version: 1,            // OS/2 表版本
    os2_usWeightClass: 400,    // 字重
    os2_fsSelection: 64,       // 选择标志
    os2_usWinAscent: 860,      // Windows 上升
    os2_usWinDescent: 260,     // Windows 下降
    os2_usDefaultChar: 0,      // 默认字符
    os2_sTypoAscender: 800,    // 排版上升
    os2_sTypoDescender: -200,  // 排版下降
    os2_sTypoLineGap: 144,     // 行间距
    os2_ulUnicodeRange1: 647,  // Unicode 范围1
    os2_ulUnicodeRange2: 135200768, // Unicode 范围2
    os2_ulUnicodeRange3: 0,    // Unicode 范围3
    os2_ulUnicodeRange4: 0,    // Unicode 范围4
    os2_ulCodePageRange1: 262303,   // 代码页范围1
    os2_ulCodePageRange2: 3755409408, // 代码页范围2
    os2_nSymbolic: -1,         // 符号标志
    header_yMin: -315,         // Y轴最小值
    header_yMax: 986,          // Y轴最大值
    monochromeSizes: []        // 单色尺寸
  }
}
```

***

## 二、实现步骤

### 步骤 1：修改 sdk-all.js（添加扩展点）

**文件**：`public/sdkjs/word/sdk-all.js`，或者经过浏览器源代码工具格式化后的版本：`public/sdkjs/word/sdk-all.format.js`

**修改内容**：

1. 在 `p` 对象末尾添加扩展点：

```javascript
// 找到 p 对象定义，在闭合 } 前添加
...window.__FONTS_PATH_EXTENTION__
```

1. 在 `q` 对象末尾添加扩展点：

```javascript
// 找到 q 对象定义，在闭合 } 前添加
...window.__FONTS_META_EXTENTION__
```

### 步骤 2：创建字体元信息提取工具

**文件**：`public/tools/font-meta-extractor.html`

**功能**：

- 读取 TTF 字体文件
- 提取所有元信息字段
- 生成 JavaScript 对象格式输出
- 支持复制到剪贴板

**技术方案**：

- 使用 `opentype.js` 库解析 TTF 文件
- 或使用 ArrayBuffer 直接解析 TTF 表结构

### 步骤 3：修改 index.html（动态配置）

**文件**：`public/web-apps/apps/documenteditor/main/index.html`

**修改内容**：在 AllFonts.js 和 sdk-all-min.js 之间添加：

```html
<script src="../../../../sdkjs/common/AllFonts.js"></script>
<script>
(function() {
  var customFontPath = 'fonts/341';
  var customFontName = '方正小标宋简体';
  var customFontFileIndex = window.__fonts_files.length;
  var customFontInfoIndex = window.__fonts_infos.length;

  // 1. 扩展 __fonts_files
  window.__fonts_files.push(customFontPath);

  // 2. 扩展 __fonts_infos
  window.__fonts_infos.push([
    customFontName,           // 名称
    customFontInfoIndex,      // 缩略图索引
    customFontFileIndex,      // 文件索引
    -1, -1, -1, -1, -1, -1    // 其他样式索引
  ]);

  // 3. 扩展 __fonts_ranges（中文字符范围）
  var ranges = window.__fonts_ranges;
  // 在数组开头插入，确保优先级
  ranges.unshift(19968, 40869, customFontInfoIndex);

  // 4. 扩展 __fonts_sort
  window.__fonts_sort.push(customFontName);

  // 5. 扩展 p 对象（路径映射）
  window.__FONTS_PATH_EXTENTION__ = {};
  window.__FONTS_PATH_EXTENTION__[customFontPath] = '341';

  // 6. 扩展 q 对象（字体元信息）- 需要从工具获取
  window.__FONTS_META_EXTENTION__ = {};
  window.__FONTS_META_EXTENTION__[customFontPath] = {
    // 从字体元信息提取工具获取
    units_per_EM: ...,
    ascender: ...,
    // ... 其他字段
  };
})();
</script>
<script src="../../../../sdkjs/word/sdk-all-min.js"></script>
```

### 步骤 4：加密字体文件

**文件**：`public/fonts/341`

**操作**：

1. 获取原始 TTF 字体文件
2. 对前 32 字节进行 XOR 加密
3. 保存为无扩展名文件

**XOR 密钥**：

```javascript
[160, 102, 214, 32, 20, 150, 71, 250, 149, 105, 184, 80, 176, 65, 73, 72]
```

### 步骤 5：更新字体预览图（已完成）

**文件**：`public/sdkjs/common/Images/fonts_thumbnail_ea@1.5x.png.bin`

**工具**：`public/tools/font-thumbnail-generator.html`

***

## 三、字体元信息提取工具设计

### 界面设计

```
┌─────────────────────────────────────────────────────────────┐
│  字体元信息提取工具                                           │
├─────────────────────────────────────────────────────────────┤
│  [选择字体文件]  [方正小标宋简体.ttf]                          │
│                                                             │
│  提取结果：                                                   │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ {                                                        ││
│  │   "fonts/341": {                                         ││
│  │     units_per_EM: 1024,                                  ││
│  │     ascender: 986,                                       ││
│  │     ...                                                  ││
│  │   }                                                      ││
│  │ }                                                        ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  [复制到剪贴板]  [下载 JSON]                                  │
└─────────────────────────────────────────────────────────────┘
```

### 技术实现

**方案 A：使用 opentype.js 库**

```javascript
import opentype from 'opentype.js';

async function extractFontMeta(file) {
  const buffer = await file.arrayBuffer();
  const font = opentype.parse(buffer);

  return {
    units_per_EM: font.unitsPerEm,
    ascender: font.ascender,
    descender: font.descender,
    // ... 其他字段
  };
}
```

**方案 B：直接解析 TTF 表结构**

TTF 文件结构：

- 文件头（12 字节）
- 表目录（每个表 16 字节）
- 各表数据

需要解析的表：

- `head`: header\_yMin, header\_yMax
- `hhea`: ascender, descender, height
- `OS/2`: os2\_\* 系列
- `name`: family\_name, style\_name
- `maxp`: num\_glyphs

### 输出格式

```javascript
window.__FONTS_META_EXTENTION__ = {
  "fonts/341": {
    units_per_EM: 1024,
    ascender: 986,
    descender: -315,
    height: 1301,
    face_flags: 2105,
    num_faces: 1,
    num_glyphs: 25185,
    num_charmaps: 3,
    style_flags: 0,
    face_index: 0,
    family_name: "方正小标宋简体",
    style_name: "Regular",
    os2_version: 1,
    os2_usWeightClass: 400,
    os2_fsSelection: 64,
    os2_usWinAscent: 860,
    os2_usWinDescent: 260,
    os2_usDefaultChar: 0,
    os2_sTypoAscender: 800,
    os2_sTypoDescender: -200,
    os2_sTypoLineGap: 144,
    os2_ulUnicodeRange1: 647,
    os2_ulUnicodeRange2: 135200768,
    os2_ulUnicodeRange3: 0,
    os2_ulUnicodeRange4: 0,
    os2_ulCodePageRange1: 262303,
    os2_ulCodePageRange2: 3755409408,
    os2_nSymbolic: -1,
    header_yMin: -315,
    header_yMax: 986,
    monochromeSizes: []
  }
};
```

***

## 四、执行顺序

1. **创建字体元信息提取工具** → `public/tools/font-meta-extractor.html`
2. **使用工具提取元信息** → 获取 `__FONTS_META_EXTENTION__` 内容
3. **修改 sdk-all.js** → 添加扩展点
4. **修改 index.html** → 添加动态配置
5. **加密字体文件** → 生成 `public/fonts/341`
6. **测试验证** → 确认字体加载和渲染正常

\*\*\*---

## 五、技术选型

### 字体元信息提取

**使用 opentype.js 库**：

- CDN：`https://opentype.js.org/dist/opentype.js`
- 浏览器端直接引用，无需安装
- API 简单，可直接解析 TTF 文件

### 实现策略

**先跑通单字体流程**：

1. 以"方正小标宋简体"为示例
2. 完成完整的自定义字体添加流程
3. 验证字体加载和渲染正常

**后续工具化**：

1. 封装字体元信息提取工具
2. 支持批量添加多个自定义字体
3. 提供可视化配置界面

***

## 六、执行计划

### 阶段一：跑通单字体流程

1. **~~创建字体元信息提取工具~~**~~（使用 opentype.js）~~
2. **提取"方正小标宋简体"的元信息**
3. ✅ **修改 sdk-all.js**（添加扩展点）- 已完成
4. **修改 index.html**（添加动态配置）
5. **加密字体文件**
6. **测试验证**

### 阶段二：工具化（后续）

1. 封装通用工具
2. 支持多字体配置
3. 提供可视化界面

