# qQa 赋值逻辑深度分析

## 一、关键发现

### 1.1 两个不同的构造函数

SDK 中存在两个字体信息构造函数：

**构造函数** **`e`**（第 132687-132702 行）：

```javascript
function e(r, t, x, y, v, A, H, O, W, V) {
    this.Aa = r;      // 参数0: 字体名称
    this.iMf = t;      // 参数1: 缩略图索引
    this.qQa = 0;      // 硬编码为 0！不从参数获取
    this.D_ = x;      // 参数2: Regular 文件索引
    this.WBb = y;      // 参数3: ???
    this.ZCd = !1;
    this.C_ = v;      // 参数4: Bold 文件索引
    this.VBb = A;      // 参数5: ???
    this.v8a = !1;
    this.IH = H;      // 参数6: Italic 文件索引
    this.TBb = O;      // 参数7: ???
    this.u8a = !1;
    this.B_ = W;      // 参数8: BoldItalic 文件索引
    this.UBb = V;      // 参数9: ???
    this.YCd = !1
}
```

**构造函数** **`d`**（第 132704-132708 行）：

```javascript
function d(r, t, x, y) {
    this.name = r;
    this.id = t || "";
    this.D1g = x || 0;
    this.qQa = y || 15   // 默认值是 15！可以从参数获取
}
```

### 1.2 \_\_fonts\_infos 的处理逻辑

在第 132719-132728 行：

```javascript
y = (x = a.__fonts_infos) ? x.length : 0;
t = Array(y);
let v = 0, A = "ASC.ttf";
for (let H = 0; H < y; H++) {
    let O = x[H];
    "ASCW3" === O[0] ? A = r[O[1]].Za : (
        t[v] = new e(O[0], H, O[1], O[2], O[3], O[4], O[5], O[6], O[7], O[8]),
        h[O[0]] = v,
        v++
    )
}
```

**关键问题**：

* `__fonts_infos` 的每个元素 `O` 是一个数组 `[name, ..., regularFileIndex, boldFileIndex, ...]`

* 这个数组被传递给构造函数 `e`

* 但 `e` 的 `qQa` 是**硬编码为 0**，不从参数获取！

### 1.3 结论

**`__fonts_infos`** **配置无法影响** **`qQa`** **的值！**

`qQa` 在构造函数 `e` 中被硬编码为 `0`，`__fonts_infos` 数组的任何元素都不会影响它。

***

## 二、解决方案

### 方案 A：在 SDK 初始化后手动设置 qQa（当前采用）

在 `AscFonts.BKa` 创建后，手动修改 `qQa`：

```javascript
setTimeout(function() {
    for (var i = 0; i < AscFonts.BKa.length; i++) {
        var info = AscFonts.BKa[i];
        if (info && info.Aa === '方正小标宋简体') {
            info.qQa = 15;
            info.ZCd = true;
            info.v8a = true;
            info.u8a = true;
            info.YCd = true;
            break;
        }
    }
}, 1000);
```

### 方案 B：修改 sdk-all.js 源码

修改构造函数 `e`，让 `qQa` 从参数获取：

**修改前**：

```javascript
function e(r, t, x, y, v, A, H, O, W, V) {
    this.Aa = r;
    this.iMf = t;
    this.qQa = 0;  // 硬编码
    // ...
}
```

**修改后**：

```javascript
function e(r, t, x, y, v, A, H, O, W, V, qQa) {  // 添加参数
    this.Aa = r;
    this.iMf = t;
    this.qQa = qQa || 15;  // 从参数获取，默认 15
    // ...
}
```

同时修改 `__fonts_infos` 处理逻辑：

```javascript
t[v] = new e(O[0], H, O[1], O[2], O[3], O[4], O[5], O[6], O[7], O[8], O[9] || 15);
```

### 方案 C：扩展 \_\_fonts\_infos 格式（推荐）

1. **修改 sdk-all.js**，让 `qQa` 从 `__fonts_infos` 的第 10 个元素获取：

```javascript
// 修改构造函数 e
function e(r, t, x, y, v, A, H, O, W, V, qQa) {
    this.Aa = r;
    this.iMf = t;
    this.qQa = qQa || 15;  // 新增参数
    // ...
}

// 修改 __fonts_infos 处理
t[v] = new e(O[0], H, O[1], O[2], O[3], O[4], O[5], O[6], O[7], O[8], O[9]);
```

1. **修改 index.html**，在 `__fonts_infos` 中添加第 10 个元素：

```javascript
window.__fonts_infos.push([
    customFontName,           // 0: 名称
    customFontInfoIndex,      // 1: 缩略图索引
    customFontFileIndex,      // 2: Regular 文件索引
    -1,                       // 3: Bold 文件索引
    -1,                       // 4: Italic 文件索引
    -1,                       // 5: BoldItalic 文件索引
    -1,                       // 6: ???
    -1,                       // 7: ???
    -1,                       // 8: ???
    15                        // 9: qQa 样式标志
]);
```

***

## 三、推荐实施步骤

### 步骤 1：修改 sdk-all.format.js

1. 找到构造函数 `e`（约第 132687 行）
2. 添加 `qQa` 参数：

```javascript
function e(r, t, x, y, v, A, H, O, W, V, qQa) {
    this.Aa = r;
    this.iMf = t;
    this.qQa = qQa || 15;  // 修改这里
    // ...
}
```

1. 找到 `__fonts_infos` 处理逻辑（约第 132725 行）
2. 修改调用：

```javascript
t[v] = new e(O[0], H, O[1], O[2], O[3], O[4], O[5], O[6], O[7], O[8], O[9]);
```

### 步骤 2：修改 index.html

在 `__fonts_infos.push` 中添加第 10 个元素 `15`：

```javascript
window.__fonts_infos.push([
    customFontName,
    customFontInfoIndex,
    customFontFileIndex,
    -1, -1, -1, -1, -1, -1,
    15  // qQa = 15，启用所有样式
]);
```

### 步骤 3：重新压缩 sdk-all.js

如果使用的是 `sdk-all-min.js`，需要重新压缩。

***

## 四、验证方法

修改后，在浏览器控制台验证：

```javascript
var idx = AscFonts.g_map_font_index['方正小标宋简体'];
var info = AscFonts.BKa[idx];
console.log('qQa:', info.qQa);  // 应该输出 15
console.log('ZCd:', info.ZCd);  // 应该输出 true
```

