# OnlyOffice 字体系统分析计划

## 目标

掌握该 Office 编辑器的字体配置、解析、加载、渲染逻辑，以便新增自定义字体。

## 分析进度

### ✅ 已完成分析

#### 1. AllFonts.js 全局配置

| 变量 | 说明 | 长度 |
| --- | --- | --- |
| `__all_fonts_js_version__` | 版本号 | 1 |
| `__fonts_files` | Windows 字体路径数组 | 341 |
| `__fonts_infos` | 字体信息数组 | 219 |
| `__fonts_sort` | 字体选择器列表 | 219 |
| `__fonts_ranges` | 字符范围数组 | 4035 (1345组) |
| `g_fonts_selection_bin` | 字体选择数据（元数据） | - |

**字体预览图文件**：

* 路径：`sdkjs/common/Images/fonts_thumbnail_ea@1.5x.png.bin`
* 格式：Alpha 蒙版 + RLE 压缩
* 用于字体选择器中显示字体预览

#### 2. `__fonts_infos` 结构

每个元素格式：`[name, thumbnailIndex, fileIndex, boldIndex, faceIndexB, italicIndex, faceIndexI, boldItalicIndex, faceIndexBI]`

* `name`: 字体名称
* `thumbnailIndex`: 缩略图索引
* `fileIndex`: 对应 `__fonts_files` 的索引（常规体）
* `boldIndex`: 粗体文件索引
* `italicIndex`: 斜体文件索引
* `boldItalicIndex`: 粗斜体文件索引

#### 3. `__fonts_ranges` 结构

每 3 个元素为一组：`[startCode, endCode, fontInfoIndex]`

* 用于根据字符代码查找应该使用的字体
* `FontPickerByCharacter.init()` 解析此数组
* `FontPickerByCharacter.getFontBySymbol(charCode)` 使用二分查找

#### 4. 字体加载流程

```
AllFonts.js 加载
    ↓
sdk-all.js 初始化
    ↓
创建 AscFonts.owe (字体文件数组)
创建 AscFonts.BKa (字体信息数组)
创建路径映射 p (Windows路径 -> 数字文件名)
    ↓
AscFonts.jg.Pe(__fonts_infos) 初始化字符范围
    ↓
文档打开时，检查需要的字体
    ↓
CFontFileLoader.hQa (LoadFontAsync)
    ↓
XHR 加载 fonts/xxx (数字文件名)
    ↓
XOR 解密前32字节
    ↓
存入 AscFonts.g_fonts_streams
    ↓
FreeType WASM 渲染
```

#### 5. 关键代码位置

**sdk-all.format.js（浏览器格式化版本，仅供参考）**：

* 字体初始化函数 `f()` - 第 132710 行
* 字体文件类 `b` - 第 132681 行
* 字体信息类 `e` - 第 132687 行
* 路径映射对象 `const p` - 第 132749-133091 行（341个映射，从 "000" 到 "340"）
* **字体元信息对象 `const q` - 第 16742-28029 行**
* 字体加载方法 `b.prototype.y3d` - 第 133112 行
* XOR 解密逻辑 - 第 133128-133133 行
* `AscFonts.jg.Pe()` 调用 - 第 132739 行

**注意**：实际加载的是 `sdk-all.js`（压缩版），`sdk-all.format.js` 只是临时参考文件。

#### 6. `p` 对象（路径映射）

```javascript
const p = {
  "C:\\Windows\\Fonts\\AGENCYB.TTF": "000",
  // ... 341 个映射 ...
  "C:\\Windows\\Fonts\\wingding.ttf": "340"
};
```

**作用**：将字体路径映射为字体文件名（数字）

**加载逻辑**：
```javascript
"chrome-extension:" != a.location?.protocol || y ? (r += p[this.Za], x = !0) : r = this.Za;
// r 是 basePath (如 "../../../../fonts/")
// p[this.Za] 是数字文件名 (如 "070")
// this.Za 是字体路径（来自 __fonts_files）
```

#### 7. `q` 对象（字体元信息）【新发现】

```javascript
const q = {
  "ASC.ttf": {
    units_per_EM: 2048,
    ascender: 1854,
    descender: -434,
    height: 2355,
    face_flags: 2585,
    num_faces: 1,
    num_glyphs: 10,
    family_name: "ASCW3",
    style_name: "Regular",
    // ... 更多属性
  },
  "C:\\Windows\\Fonts\\AGENCYB.TTF": {
    units_per_EM: 2048,
    ascender: 2042,
    // ...
  },
  // ... 所有字体的元信息
};
```

**作用**：存储每个字体的 FreeType 元信息，用于渲染计算

**使用方式**（第 16603 行）：
```javascript
var O = q[A.Za ?? "ASC.ttf"];  // A.Za 是字体路径
this.Up.vMc = O.units_per_EM;
this.Up.hYb = O.ascender;
// ...
```

**键**：与 `__fonts_files` 中的值相同（字体路径）

#### 8. 字体文件格式要求

**关键发现：字体文件需要 XOR 加密！**

XOR 密钥（十进制格式）：

```javascript
[160, 102, 214, 32, 20, 150, 71, 250, 149, 105, 184, 80, 176, 65, 73, 72]
```

---

## 问题诊断

### 之前实现的问题

1. **字体文件未加密**
   * 文件 342 是未加密的原始 TTF 文件
   * 加载器会进行 XOR 解密，导致数据错误

2. **路径映射缺失**
   * `sdk-all.js` 中的路径映射对象 `p` 是硬编码的
   * 没有包含自定义字体路径的映射

3. **字体元信息缺失**
   * `q` 对象中没有自定义字体的元信息
   * 可能导致渲染计算错误

---

## 实现方案

### 方案：SDK 扩展点 + 动态配置

**核心思路**：在 `sdk-all.js` 的 `p` 和 `q` 对象末尾添加扩展点，通过全局变量动态扩展。

#### 步骤 1：修改 sdk-all.js（一次性）

在 `p` 对象末尾添加扩展点：
```javascript
const p = {
  // ... 现有映射 ...
  "C:\\Windows\\Fonts\\wingding.ttf": "340",
  ...window.__FONTS_PATH_EXTENTION__
};
```

在 `q` 对象末尾添加扩展点：
```javascript
const q = {
  // ... 现有元信息 ...
  ...window.__FONTS_META_EXTENTION__
};
```

#### 步骤 2：在 index.html 中定义扩展（每次添加字体）

在 AllFonts.js 加载之后、sdk-all.js 加载之前：

```javascript
<script src="../../../../sdkjs/common/AllFonts.js"></script>
<script>
  // 1. 扩展 __fonts_files（字体路径）
  window.__fonts_files.push("fonts/341");
  
  // 2. 扩展 __fonts_infos（字体信息）
  window.__fonts_infos.push(["方正小标宋简体", 219, 341, -1, -1, -1, -1, -1, -1]);
  
  // 3. 扩展 __fonts_ranges（字符范围）
  // 中文字符范围: 0x4E00 - 0x9FFF = 19968 - 40869
  window.__fonts_ranges.unshift(19968, 40869, 219);
  
  // 4. 扩展 __fonts_sort（字体列表）
  window.__fonts_sort.push("方正小标宋简体");
  
  // 5. 扩展 p 对象（路径映射）
  window.__FONTS_PATH_EXTENTION__ = {
    "fonts/341": "341"
  };
  
  // 6. 扩展 q 对象（字体元信息）
  // 可以从字体文件提取，或使用相似字体的元信息
  window.__FONTS_META_EXTENTION__ = {
    "fonts/341": {
      units_per_EM: 1024,  // 需要从字体文件提取
      ascender: ...,
      descender: ...,
      // ... 其他属性
    }
  };
</script>
<script src="../../../../sdkjs/word/sdk-all-min.js"></script>
```

#### 步骤 3：加密字体文件

```javascript
const fs = require('fs');
const xorKey = [160, 102, 214, 32, 20, 150, 71, 250, 149, 105, 184, 80, 176, 65, 73, 72];

const fontData = fs.readFileSync('方正小标宋简体.ttf');
for (let i = 0; i < 32; i++) {
  fontData[i] ^= xorKey[i % 16];
}
fs.writeFileSync('public/fonts/341', fontData);
```

---

## 待确认事项

1. **sdk-all.js 中 p 和 q 对象的位置**
   * 需要在压缩文件中找到对应的代码位置
   * 添加扩展点语法

2. **字体元信息的获取**
   * 方案 A：从字体文件中提取（需要工具）
   * 方案 B：使用相似中文字体的元信息（如宋体）

3. **字体文件命名**
   * 当前使用 "341"
   * 是否需要使用其他命名规则？

---

## 下一步行动

1. **确认方案** - 用户确认后执行
2. **修改 sdk-all.js** - 添加扩展点
3. **修改 index.html** - 添加动态配置
4. **加密字体文件** - 生成加密后的字体文件
5. **测试验证** - 确认字体能正确加载和渲染
