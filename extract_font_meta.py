import struct
import os

temp_file = os.path.join(os.environ['TEMP'], 'temp_font_341.ttf')

with open(temp_file, 'rb') as f:
    data = f.read()

# 解析 TTF 文件
def read_u16(data, offset):
    return struct.unpack('>H', data[offset:offset+2])[0]

def read_u32(data, offset):
    return struct.unpack('>I', data[offset:offset+4])[0]

def read_s16(data, offset):
    return struct.unpack('>h', data[offset:offset+2])[0]

# 读取表目录
num_tables = read_u16(data, 4)
tables = {}
offset = 12
for i in range(num_tables):
    tag = data[offset:offset+4].decode('ascii', errors='replace')
    table_offset = read_u32(data, offset + 8)
    table_length = read_u32(data, offset + 12)
    tables[tag] = (table_offset, table_length)
    offset += 16

print("=== 字体表目录 ===")
for tag, (off, length) in tables.items():
    print(f"  {tag}: offset={off}, length={length}")

# 读取 head 表
if 'head' in tables:
    off, length = tables['head']
    print("\n=== head 表 ===")
    print(f"  units_per_EM: {read_u16(data, off + 18)}")
    print(f"  header_yMin: {read_s16(data, off + 38)}")
    print(f"  header_yMax: {read_s16(data, off + 40)}")
    print(f"  face_flags: {read_u16(data, off + 16)}")

# 读取 hhea 表
if 'hhea' in tables:
    off, length = tables['hhea']
    print("\n=== hhea 表 ===")
    print(f"  ascender: {read_s16(data, off + 4)}")
    print(f"  descender: {read_s16(data, off + 6)}")
    print(f"  lineGap: {read_s16(data, off + 8)}")

# 读取 OS/2 表
if 'OS/2' in tables:
    off, length = tables['OS/2']
    print("\n=== OS/2 表 ===")
    print(f"  os2_version: {read_u16(data, off)}")
    print(f"  os2_usWeightClass: {read_u16(data, off + 4)}")
    print(f"  os2_fsSelection: {read_u16(data, off + 62)}")
    print(f"  os2_usWinAscent: {read_u16(data, off + 74)}")
    print(f"  os2_usWinDescent: {read_u16(data, off + 76)}")
    print(f"  os2_ulUnicodeRange1: {read_u32(data, off + 42)}")
    print(f"  os2_ulUnicodeRange2: {read_u32(data, off + 46)}")
    print(f"  os2_ulUnicodeRange3: {read_u32(data, off + 50)}")
    print(f"  os2_ulUnicodeRange4: {read_u32(data, off + 54)}")
    print(f"  os2_ulCodePageRange1: {read_u32(data, off + 78)}")
    print(f"  os2_ulCodePageRange2: {read_u32(data, off + 82)}")
    print(f"  os2_sTypoAscender: {read_s16(data, off + 68)}")
    print(f"  os2_sTypoDescender: {read_s16(data, off + 70)}")
    print(f"  os2_sTypoLineGap: {read_s16(data, off + 72)}")
    print(f"  os2_usDefaultChar: {read_u16(data, off + 24)}")

# 读取 maxp 表获取字形数量
if 'maxp' in tables:
    off, length = tables['maxp']
    print("\n=== maxp 表 ===")
    print(f"  num_glyphs: {read_u16(data, off + 4)}")

# 读取 cmap 表获取字符映射数量
if 'cmap' in tables:
    off, length = tables['cmap']
    num_subtables = read_u16(data, off + 2)
    print("\n=== cmap 表 ===")
    print(f"  num_charmaps: {num_subtables}")

# 读取 name 表获取字体名称
if 'name' in tables:
    off, length = tables['name']
    num_records = read_u16(data, off + 2)
    string_offset = read_u16(data, off + 4)
    
    family_name = ""
    style_name = ""
    
    record_offset = off + 6
    for i in range(num_records):
        platform_id = read_u16(data, record_offset)
        encoding_id = read_u16(data, record_offset + 2)
        language_id = read_u16(data, record_offset + 4)
        name_id = read_u16(data, record_offset + 6)
        str_length = read_u16(data, record_offset + 8)
        str_offset = read_u16(data, record_offset + 10)
        
        # name_id 1 = Font Family, 2 = Font Subfamily
        if name_id == 1 and platform_id == 3:
            str_data = data[off + string_offset + str_offset:off + string_offset + str_offset + str_length]
            try:
                family_name = str_data.decode('utf-16-be')
            except:
                pass
        elif name_id == 2 and platform_id == 3:
            str_data = data[off + string_offset + str_offset:off + string_offset + str_offset + str_length]
            try:
                style_name = str_data.decode('utf-16-be')
            except:
                pass
        
        record_offset += 12
    
    print("\n=== name 表 ===")
    print(f"  family_name: {family_name}")
    print(f"  style_name: {style_name}")

print("\n=== 完整元数据 JSON ===")
print("window.__FONTS_META_EXTENTION__['fonts/341'] = {")
if 'head' in tables:
    off, _ = tables['head']
    print(f"    units_per_EM: {read_u16(data, off + 18)},")
    print(f"    ascender: {read_s16(data, off + 0) if 'hhea' not in tables else read_s16(data, tables['hhea'][0] + 4)},")
    print(f"    descender: {read_s16(data, off + 0) if 'hhea' not in tables else read_s16(data, tables['hhea'][0] + 6)},")
    print(f"    height: {read_u16(data, off + 18)},")
    print(f"    face_flags: {read_u16(data, off + 16)},")
if 'maxp' in tables:
    off, _ = tables['maxp']
    print(f"    num_glyphs: {read_u16(data, off + 4)},")
if 'cmap' in tables:
    off, _ = tables['cmap']
    print(f"    num_charmaps: {read_u16(data, off + 2)},")
print("    style_flags: 0,")
print("    face_index: 0,")
print("    family_name: '方正小标宋简体',")
print("    style_name: 'Regular',")
if 'OS/2' in tables:
    off, _ = tables['OS/2']
    print(f"    os2_version: {read_u16(data, off)},")
    print(f"    os2_usWeightClass: {read_u16(data, off + 4)},")
    print(f"    os2_fsSelection: {read_u16(data, off + 62)},")
    print(f"    os2_usWinAscent: {read_u16(data, off + 74)},")
    print(f"    os2_usWinDescent: {read_u16(data, off + 76)},")
    print(f"    os2_usDefaultChar: {read_u16(data, off + 24)},")
    print(f"    os2_sTypoAscender: {read_s16(data, off + 68)},")
    print(f"    os2_sTypoDescender: {read_s16(data, off + 70)},")
    print(f"    os2_sTypoLineGap: {read_s16(data, off + 72)},")
    print(f"    os2_ulUnicodeRange1: {read_u32(data, off + 42)},")
    print(f"    os2_ulUnicodeRange2: {read_u32(data, off + 46)},")
    print(f"    os2_ulUnicodeRange3: {read_u32(data, off + 50)},")
    print(f"    os2_ulUnicodeRange4: {read_u32(data, off + 54)},")
    print(f"    os2_ulCodePageRange1: {read_u32(data, off + 78)},")
    print(f"    os2_ulCodePageRange2: {read_u32(data, off + 82)},")
    print("    os2_nSymbolic: -1,")
if 'head' in tables:
    off, _ = tables['head']
    print(f"    header_yMin: {read_s16(data, off + 38)},")
    print(f"    header_yMax: {read_s16(data, off + 40)},")
print("    monochromeSizes: []")
print("};")
