import fs from 'fs';
const content = fs.readFileSync('d:/projects/riant/onlyoffice-web-local/public/sdkjs/common/AllFonts.js', 'utf8');

console.log('=== 当前 AllFonts.js 状态 ===\n');

// 检查 __fonts_files
const filesMatch = content.match(/window\.__fonts_files=\[[^\]]+\]/);
if (filesMatch) {
  const filesStr = filesMatch[0];
  const files = eval(filesStr.replace('window.__fonts_files=', ''));
  console.log('__fonts_files 长度:', files.length);
  console.log('最后 3 个:', files.slice(-3));
}

// 检查 __fonts_infos
const infosMatch = content.match(/window\.__fonts_infos=\[[^\]]+\]/);
if (infosMatch) {
  const infosStr = infosMatch[0];
  const infos = eval(infosStr.replace('window.__fonts_infos=', ''));
  console.log('\n__fonts_infos 长度:', infos.length);
  console.log('最后 3 个:');
  infos.slice(-3).forEach((info, i) => {
    console.log(`  索引 ${infos.length - 3 + i}: ${info[0]} - thumbnailIndex: ${info[1]}, fileIndex: ${info[2]}`);
  });
}

// 检查 __fonts_ranges
const rangesMatch = content.match(/window\.__fonts_ranges=\[[^\]]+\]/);
if (rangesMatch) {
  const rangesStr = rangesMatch[0];
  const ranges = eval(rangesStr.replace('window.__fonts_ranges=', ''));
  console.log('\n__fonts_ranges 长度:', ranges.length);
  console.log('前 3 组:');
  for (let i = 0; i < 9; i += 3) {
    console.log(`  组 ${i/3}: startCode=${ranges[i]}, endCode=${ranges[i+1]}, fontInfoIndex=${ranges[i+2]}`);
  }
}

// 检查 __fonts_sort
const sortMatch = content.match(/window\.__fonts_sort=\[[^\]]+\]/);
if (sortMatch) {
  const sortStr = sortMatch[0];
  const sort = eval(sortStr.replace('window.__fonts_sort=', ''));
  console.log('\n__fonts_sort 长度:', sort.length);
  console.log('最后 3 个:', sort.slice(-3));
}
