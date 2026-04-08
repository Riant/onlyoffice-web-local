import fs from 'fs';
let content = fs.readFileSync('d:/projects/riant/onlyoffice-web-local/public/sdkjs/common/AllFonts.js', 'utf8');

console.log('=== 修改前检查 ===');
console.log('__fonts_files 包含 fonts/341:', content.includes('fonts/341'));

// 1. 修改 __fonts_files: 添加自定义字体路径
// 注意：文件中的路径使用的是 \\\\ (四个反斜杠)
content = content.replace(
  /"C:\\\\Windows\\\\Fonts\\\\wingding\.ttf"\]/,
  '"C:\\\\Windows\\\\Fonts\\\\wingding.ttf","fonts/341"]'
);

// 2. 修改 __fonts_infos: 在最后一个元素后添加新字体信息
content = content.replace(
  /\["YouYuan",192,0,-1,-1,-1,-1,-1,-1\]\]/,
  '["YouYuan",192,0,-1,-1,-1,-1,-1,-1],["方正小标宋简体",219,341,-1,-1,-1,-1,-1,-1]]'
);

// 3. 修改 __fonts_sort: 在最后添加字体名称
content = content.replace(
  /"Wingdings 3"\]/,
  '"Wingdings 3","方正小标宋简体"]'
);

// 4. 修改 __fonts_ranges: 添加中文字符范围
content = content.replace(
  /window\.__fonts_ranges=\[/,
  'window.__fonts_ranges=[19968,40869,219,'
);

fs.writeFileSync('d:/projects/riant/onlyoffice-web-local/public/sdkjs/common/AllFonts.js', content);

console.log('\n=== 修改后验证 ===');
const newContent = fs.readFileSync('d:/projects/riant/onlyoffice-web-local/public/sdkjs/common/AllFonts.js', 'utf8');
console.log('__fonts_files 包含 fonts/341:', newContent.includes('fonts/341'));
console.log('__fonts_infos 包含 方正小标宋简体:', newContent.includes('方正小标宋简体'));
console.log('__fonts_ranges 开头包含 19968,40869,219:', newContent.includes('__fonts_ranges=[19968,40869,219,'));
