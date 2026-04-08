#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字体文件处理脚本 - 将方正小标宋简体重新导出为标准 TTF 格式并加密
"""

from fontTools.ttLib import TTFont
import os

input_font = r'D:\projects\riant\方正小标宋简体.ttf'
output_font_raw = r'D:\projects\riant\341_new'
output_font_encrypted = r'D:\projects\riant\onlyoffice-web-local\public\fonts\341'

# XOR 加密密钥
XOR_KEY = bytes([160, 102, 214, 32, 20, 150, 71, 250, 149, 105, 184, 80, 176, 65, 73, 72])

print(f'正在加载字体: {input_font}')

# 加载字体
font = TTFont(input_font)

# 打印字体信息
print('\n=== 字体基本信息 ===')
print(f'字形数量: {len(font.getGlyphOrder())}')

# 打印字体名称
print('\n=== 字体名称 ===')
name_table = font['name']
family_names = {}
for record in name_table.names:
    if record.nameID == 1:  # Font Family
        try:
            platform = 'Unicode' if record.platformID == 0 else 'Mac' if record.platformID == 1 else 'Windows'
            name = record.toUnicode()
            family_names[platform] = name
            print(f'  {platform}: {name}')
        except:
            pass

# 检查字体表
print('\n=== 字体表 ===')
for table in font.keys():
    print(f'  {table}')

# 检查是否有特殊的表
special_tables = ['GSUB', 'GPOS', 'GDEF', 'BASE', 'JSTF', 'MATH', 'CBDT', 'CBLC', 'COLR', 'CPAL']
found_special = []
for table in special_tables:
    if table in font:
        found_special.append(table)

if found_special:
    print(f'\n=== 发现特殊表: {found_special} ===')
    print('这些表可能导致 WASM FreeType 兼容性问题')

# 尝试简化字体
print('\n=== 开始处理字体 ===')

# 1. 移除可能导致问题的表
tables_to_remove = ['GSUB', 'GPOS', 'GDEF', 'BASE', 'JSTF', 'MATH', 'CBDT', 'CBLC', 'COLR', 'CPAL', 'VORG']
removed_tables = []
for table in tables_to_remove:
    if table in font:
        del font[table]
        removed_tables.append(table)
        print(f'  已移除表: {table}')

if removed_tables:
    print(f'\n共移除 {len(removed_tables)} 个表')

# 2. 确保基本的表存在且正确
print('\n=== 检查基本表 ===')
required_tables = ['head', 'hhea', 'maxp', 'OS/2', 'hmtx', 'cmap', 'loca', 'glyf', 'name', 'post']
for table in required_tables:
    if table in font:
        print(f'  ✓ {table}')
    else:
        print(f'  ✗ {table} (缺失)')

# 3. 修改 head 表的一些属性
if 'head' in font:
    head = font['head']
    print(f'\n=== head 表信息 ===')
    print(f'  unitsPerEm: {head.unitsPerEm}')
    print(f'  flags: {head.flags}')
    print(f'  macStyle: {head.macStyle}')
    head.flags = 11
    head.macStyle = 0

# 4. OS/2 表信息
if 'OS/2' in font:
    os2 = font['OS/2']
    print(f'\n=== OS/2 表信息 ===')
    print(f'  version: {os2.version}')
    print(f'  usWeightClass: {os2.usWeightClass}')
    print(f'  usWidthClass: {os2.usWidthClass}')
    print(f'  fsSelection: {os2.fsSelection}')

# 5. 保存原始字体
print(f'\n=== 保存字体 ===')
print(f'原始字体路径: {output_font_raw}')

try:
    font.save(output_font_raw)
    print('保存原始字体成功!')
except Exception as e:
    print(f'保存失败: {e}')
    import traceback
    traceback.print_exc()
    exit(1)

font.close()

# 6. 加密字体文件
print(f'\n=== 加密字体 ===')
print(f'加密后路径: {output_font_encrypted}')

with open(output_font_raw, 'rb') as f:
    raw_bytes = f.read()

encrypted = bytearray(len(raw_bytes))
for i in range(len(raw_bytes)):
    encrypted[i] = raw_bytes[i] ^ XOR_KEY[i % 16]

with open(output_font_encrypted, 'wb') as f:
    f.write(encrypted)

print(f'加密成功! 文件大小: {len(encrypted)} 字节')

# 7. 输出配置信息
print('\n' + '='*60)
print('=== 配置信息 ===')
print('='*60)

# 获取英文名称
en_name = family_names.get('Mac', family_names.get('Windows', 'FZXiaoBiaoSong-B05S'))
cn_name = family_names.get('Windows', '方正小标宋简体')

print(f'''
// __fonts_infos 配置
window.__fonts_infos.push([
    '{en_name}',  // 使用英文名称
    customFontFileIndex,
    -1, -1, -1, -1, -1, -1, -1
]);

// customFontInfo 配置
var customFontInfo = {{
    u2: '{en_name}',  // 使用英文名称
    ixa: 'fonts/341',
    ...
}};

// family_name 配置
family_name: '{en_name}',  // 使用英文名称
''')

print('\n=== 处理完成 ===')
print(f'加密字体文件: {output_font_encrypted}')
