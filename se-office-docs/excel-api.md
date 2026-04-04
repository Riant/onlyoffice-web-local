# SE Office Excel JavaScript API 文档

本文档整理自 SE Office 项目中 ONLYOFFICE Excel 编辑器的 JavaScript API，用于二次开发扩展。

## 目录

- [核心API类](#核心api类)
- [属性类](#属性类)
- [枚举常量](#枚举常量)
- [回调事件](#回调事件)
- [使用示例](#使用示例)

---

## 核心API类

### spreadsheet_api

Excel电子表格编辑器的核心API类，提供电子表格操作的所有方法。

#### 初始化方法

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_setLocale(LCID, decimalSeparator, groupSeparator)` | LCID: number, decimalSeparator: string, groupSeparator: string | void | 设置区域设置 |
| `asc_getLocale()` | 无 | number | 获取当前区域设置 |
| `asc_getDecimalSeparator(culture)` | culture: string | string | 获取小数分隔符 |
| `asc_getGroupSeparator(culture)` | culture: string | string | 获取千位分隔符 |
| `asc_setViewMode(isViewMode)` | isViewMode: boolean | void | 设置视图模式 |
| `asc_setFilteringMode(mode)` | mode: number | void | 设置筛选模式 |

#### 工作簿操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_DownloadAs(options)` | options: asc_CDownloadOptions | void | 下载文档为指定格式 |
| `asc_CloseFile()` | 无 | void | 关闭文件 |
| `asc_isDocumentModified()` | 无 | boolean | 文档是否已修改 |
| `asc_setData(oData)` | oData: object | void | 设置数据 |
| `asc_getData()` | 无 | object | 获取数据 |

#### 工作表操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getWorksheetsCount()` | 无 | number | 获取工作表数量 |
| `asc_getWorksheetName(index)` | index: number | string | 获取工作表名称 |
| `asc_getWorksheetTabColor(index)` | index: number | object | 获取工作表标签颜色 |
| `asc_setWorksheetTabColor(color, arrSheets)` | color: object, arrSheets: array | void | 设置工作表标签颜色 |
| `asc_getActiveWorksheetIndex()` | 无 | number | 获取活动工作表索引 |
| `asc_getActiveWorksheetId()` | 无 | string | 获取活动工作表ID |
| `asc_getWorksheetId(index)` | index: number | string | 获取工作表ID |
| `asc_isWorksheetHidden(index)` | index: number | boolean | 工作表是否隐藏 |
| `asc_getHiddenWorksheets()` | 无 | array | 获取隐藏的工作表列表 |
| `asc_showWorksheet(index)` | index: number | void | 显示工作表 |
| `asc_hideWorksheet(arrSheets)` | arrSheets: array | void | 隐藏工作表 |
| `asc_renameWorksheet(name)` | name: string | void | 重命名工作表 |
| `asc_addWorksheet(name)` | name: string | void | 添加工作表 |
| `asc_insertWorksheet(arrNames)` | arrNames: array | void | 插入工作表 |
| `asc_deleteWorksheet(arrSheets)` | arrSheets: array | void | 删除工作表 |
| `asc_moveWorksheet(where, arrSheets)` | where: object, arrSheets: array | void | 移动工作表 |
| `asc_copyWorksheet(where, arrNames, arrSheets)` | where: object, arrNames: array, arrSheets: array | void | 复制工作表 |
| `asc_cleanWorksheet()` | 无 | void | 清除工作表 |
| `asc_setWorksheetRange(val)` | val: object | void | 设置工作表范围 |
| `asc_isWorksheetLockedOrDeleted(index)` | index: number | boolean | 工作表是否锁定或删除 |
| `asc_isWorkbookLocked()` | 无 | boolean | 工作簿是否锁定 |

#### 单元格操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getCellInfo()` | 无 | object | 获取单元格信息 |
| `asc_getActiveCell()` | 无 | object | 获取活动单元格 |
| `asc_getActiveCellCoord(useUpRightMerge)` | useUpRightMerge: boolean | object | 获取活动单元格坐标 |
| `asc_getAnchorPosition()` | 无 | object | 获取锚点位置 |
| `asc_getCellEditMode()` | 无 | number | 获取单元格编辑模式 |
| `asc_getActiveRangeStr(referenceType, opt_getActiveCell, opt_ignore_r1c1)` | referenceType: number, opt_getActiveCell: boolean, opt_ignore_r1c1: boolean | string | 获取活动范围字符串 |
| `asc_closeCellEditor(cancel)` | cancel: boolean | void | 关闭单元格编辑器 |
| `asc_insertCells(options)` | options: object | void | 插入单元格 |
| `asc_deleteCells(options)` | options: object | void | 删除单元格 |
| `asc_mergeCells(options)` | options: object | void | 合并单元格 |
| `asc_mergeCellsDataLost(options)` | options: object | boolean | 合并单元格(检查数据丢失) |
| `asc_sortCells(options)` | options: object | void | 排序单元格 |
| `asc_sortCellsRangeExpand()` | 无 | void | 展开排序范围 |
| `asc_emptyCells(options, isMineComments)` | options: object, isMineComments: boolean | void | 清空单元格 |
| `asc_cleanSelection()` | 无 | void | 清除选择 |

#### 单元格格式设置

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_setCellFontName(fontName)` | fontName: string | void | 设置字体名称 |
| `asc_setCellFontSize(fontSize)` | fontSize: number | void | 设置字体大小 |
| `asc_setCellBold(isBold)` | isBold: boolean | void | 设置粗体 |
| `asc_setCellItalic(isItalic)` | isItalic: boolean | void | 设置斜体 |
| `asc_setCellUnderline(isUnderline)` | isUnderline: boolean | void | 设置下划线 |
| `asc_setCellStrikeout(isStrikeout)` | isStrikeout: boolean | void | 设置删除线 |
| `asc_setCellSubscript(isSubscript)` | isSubscript: boolean | void | 设置下标 |
| `asc_setCellSuperscript(isSuperscript)` | isSuperscript: boolean | void | 设置上标 |
| `asc_setCellAlign(align)` | align: number | void | 设置水平对齐 |
| `asc_setCellVertAlign(align)` | align: number | void | 设置垂直对齐 |
| `asc_setCellTextWrap(isWrapped)` | isWrapped: boolean | void | 设置自动换行 |
| `asc_setCellTextShrink(isShrinked)` | isShrinked: boolean | void | 设置缩小字体填充 |
| `asc_setCellTextColor(color)` | color: asc_CColor | void | 设置文字颜色 |
| `asc_setCellFill(fill)` | fill: object | void | 设置填充 |
| `asc_setCellBackgroundColor(color)` | color: asc_CColor | void | 设置背景颜色 |
| `asc_setCellBorders(borders)` | borders: object | void | 设置边框 |
| `asc_setCellFormat(format)` | format: string | void | 设置数字格式 |
| `asc_setCellAngle(angle)` | angle: number | void | 设置文字角度 |
| `asc_setCellStyle(name)` | name: string | void | 设置单元格样式 |
| `asc_putPrLineSpacing(type, value)` | type: number, value: number | void | 设置行距 |
| `asc_putLineSpacingBeforeAfter(type, value)` | type: number, value: number | void | 设置段前/段后间距 |

#### 行列操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getColumnWidth()` | 无 | number | 获取列宽 |
| `asc_setColumnWidth(width)` | width: number | void | 设置列宽 |
| `asc_showColumns()` | 无 | void | 显示列 |
| `asc_hideColumns()` | 无 | void | 隐藏列 |
| `asc_autoFitColumnWidth()` | 无 | void | 自动调整列宽 |
| `asc_getRowHeight()` | 无 | number | 获取行高 |
| `asc_setRowHeight(height)` | height: number | void | 设置行高 |
| `asc_autoFitRowHeight()` | 无 | void | 自动调整行高 |
| `asc_showRows()` | 无 | void | 显示行 |
| `asc_hideRows()` | 无 | void | 隐藏行 |
| `asc_group(val)` | val: number | void | 分组 |
| `asc_ungroup(val)` | val: number | void | 取消分组 |
| `asc_checkAddGroup(bUngroup)` | bUngroup: boolean | void | 检查是否可添加分组 |
| `asc_clearOutline()` | 无 | void | 清除大纲 |
| `asc_changeGroupDetails(bExpand)` | bExpand: boolean | void | 展开/折叠分组 |

#### 筛选和排序

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_addAutoFilter(styleName, addFormatTableOptionsObj)` | styleName: string, addFormatTableOptionsObj: object | void | 添加自动筛选 |
| `asc_changeAutoFilter(tableName, optionType, val)` | tableName: string, optionType: number, val: any | void | 更改自动筛选 |
| `asc_applyAutoFilter(autoFilterObject)` | autoFilterObject: object | void | 应用自动筛选 |
| `asc_applyAutoFilterByType(autoFilterObject)` | autoFilterObject: object | void | 按类型应用自动筛选 |
| `asc_reapplyAutoFilter(displayName)` | displayName: string | void | 重新应用自动筛选 |
| `asc_sortColFilter(type, cellId, displayName, color, bIsExpandRange)` | type: number, cellId: string, displayName: string, color: object, bIsExpandRange: boolean | void | 排序列筛选 |
| `asc_getAddFormatTableOptions(range)` | range: object | object | 获取添加格式表格选项 |
| `asc_clearFilter()` | 无 | void | 清除筛选 |
| `asc_clearFilterColumn(cellId, displayName)` | cellId: string, displayName: string | void | 清除列筛选 |
| `asc_changeSelectionFormatTable(tableName, optionType)` | tableName: string, optionType: number | void | 更改选择格式表格 |
| `asc_changeFormatTableInfo(tableName, optionType, val)` | tableName: string, optionType: number, val: any | void | 更改格式表格信息 |
| `asc_applyAutoCorrectOptions(val)` | val: object | void | 应用自动更正选项 |
| `asc_insertCellsInTable(tableName, optionType)` | tableName: string, optionType: number | void | 在表格中插入单元格 |
| `asc_deleteCellsInTable(tableName, optionType)` | tableName: string, optionType: number | void | 在表格中删除单元格 |
| `asc_changeDisplayNameTable(tableName, newName)` | tableName: string, newName: string | void | 更改表格显示名称 |
| `asc_changeTableRange(tableName, range)` | tableName: string, range: object | void | 更改表格范围 |
| `asc_convertTableToRange(tableName)` | tableName: string | void | 将表格转换为范围 |

#### 查找替换

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_findText(options, callback)` | options: object, callback: function | void | 查找文本 |
| `asc_replaceText(options)` | options: object | void | 替换文本 |
| `asc_endFindText()` | 无 | void | 结束查找 |
| `asc_findCell(reference)` | reference: string | void | 查找单元格 |
| `asc_StartTextAroundSearch()` | 无 | void | 开始搜索上下文 |
| `asc_SelectSearchElement(sId)` | sId: string | void | 选择搜索元素 |

#### 定义名称

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getDefinedNames(defNameListId, excludeErrorRefNames)` | defNameListId: number, excludeErrorRefNames: boolean | array | 获取定义名称列表 |
| `asc_setDefinedNames(defName)` | defName: object | void | 设置定义名称 |
| `asc_editDefinedNames(oldName, newName)` | oldName: string, newName: string | void | 编辑定义名称 |
| `asc_delDefinedNames(oldName)` | oldName: string | void | 删除定义名称 |
| `asc_checkDefinedName(checkName, scope)` | checkName: string, scope: number | boolean | 检查定义名称 |
| `asc_getDefaultDefinedName()` | 无 | object | 获取默认定义名称 |

#### 图表操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getChartObject(bNoLock)` | bNoLock: boolean | object | 获取图表对象 |
| `asc_addChartDrawingObject(chart)` | chart: object | void | 添加图表 |
| `asc_editChartDrawingObject(chart)` | chart: object | void | 编辑图表 |
| `asc_getWordChartObject()` | 无 | object | 获取Word图表对象 |
| `asc_checkDataRange(dialogType, dataRange, fullCheck, isRows, chartType)` | dialogType: number, dataRange: string, fullCheck: boolean, isRows: boolean, chartType: number | number | 检查数据范围 |

#### 图片和形状操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_addImageDrawingObject(urls, imgProp, token)` | urls: array, imgProp: object, token: string | void | 添加图片 |
| `asc_showImageFileDialog()` | 无 | void | 显示图片文件对话框 |
| `asc_changeImageFromFile()` | 无 | void | 从文件更改图片 |
| `asc_changeShapeImageFromFile(type)` | type: number | void | 从文件更改形状图片 |
| `asc_getOriginalImageSize()` | 无 | object | 获取原始图片尺寸 |
| `asc_startAddShape(sPreset)` | sPreset: string | void | 开始添加形状 |
| `asc_endAddShape()` | 无 | void | 结束添加形状 |
| `asc_addShapeOnSheet(sPreset)` | sPreset: string | void | 在工作表上添加形状 |
| `asc_changeShapeType(value)` | value: string | void | 更改形状类型 |
| `asc_getGraphicObjectProps()` | 无 | object | 获取图形对象属性 |
| `asc_setGraphicObjectProps(props)` | props: object | void | 设置图形对象属性 |
| `asc_getSelectedDrawingObjectsCount()` | 无 | number | 获取选中绘图对象数量 |
| `asc_setSelectedDrawingObjectLayer(layerType)` | layerType: number | void | 设置选中绘图对象图层 |
| `asc_setSelectedDrawingObjectAlign(alignType)` | alignType: number | void | 设置选中绘图对象对齐 |
| `asc_DistributeSelectedDrawingObjectHor()` | 无 | void | 水平分布选中绘图对象 |
| `asc_DistributeSelectedDrawingObjectVer()` | 无 | void | 垂直分布选中绘图对象 |
| `asc_canEditCrop()` | 无 | boolean | 是否可以裁剪 |
| `asc_startEditCrop()` | 无 | void | 开始裁剪 |
| `asc_endEditCrop()` | 无 | void | 结束裁剪 |
| `asc_cropFit()` | 无 | void | 裁剪适应 |
| `asc_cropFill()` | 无 | void | 裁剪填充 |
| `asc_canEditGeometry()` | 无 | boolean | 是否可以编辑几何形状 |
| `asc_editPointsGeometry()` | 无 | void | 编辑几何形状点 |
| `asc_canGroupGraphicsObjects()` | 无 | boolean | 是否可以组合图形对象 |
| `asc_groupGraphicsObjects()` | 无 | void | 组合图形对象 |
| `asc_canUnGroupGraphicsObjects()` | 无 | boolean | 是否可以取消组合 |
| `asc_unGroupGraphicsObjects()` | 无 | void | 取消组合图形对象 |
| `asc_canAddShapeHyperlink()` | 无 | boolean | 是否可以添加形状超链接 |

#### 文本艺术字

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_addTextArt(nStyle)` | nStyle: number | void | 添加文本艺术字 |
| `asc_setInterfaceDrawImagePlaceTextArt(elementId)` | elementId: string | void | 设置文本艺术字绘制位置 |
| `asc_changeArtImageFromFile(type)` | type: number | void | 从文件更改艺术字图片 |

#### 数学公式

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_AddMath(Type)` | Type: number | void | 添加数学公式 |
| `asc_AddMath2(Type)` | Type: number | void | 添加数学公式(扩展) |
| `asc_ConvertMathView(isToLinear, isAll)` | isToLinear: boolean, isAll: boolean | void | 转换数学公式视图 |
| `asc_SetMathProps(MathProps)` | MathProps: object | void | 设置数学公式属性 |

#### 注释

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_addComment(oComment)` | oComment: object | void | 添加注释 |
| `asc_changeComment(id, oComment)` | id: string, oComment: object | void | 修改注释 |
| `asc_selectComment(id)` | id: string | void | 选择注释 |
| `asc_showComment(id, bNew)` | id: string, bNew: boolean | void | 显示注释 |
| `asc_findComment(id)` | id: string | object | 查找注释 |
| `asc_removeComment(id)` | id: string | void | 删除注释 |
| `asc_RemoveAllComments(isMine, isCurrent)` | isMine: boolean, isCurrent: boolean | void | 删除所有注释 |
| `asc_ResolveAllComments(isMine, isCurrent, arrIds)` | isMine: boolean, isCurrent: boolean, arrIds: array | void | 解决所有注释 |
| `asc_showComments(isShowSolved)` | isShowSolved: boolean | void | 显示注释 |
| `asc_hideComments()` | 无 | void | 隐藏注释 |
| `asc_GetCommentLogicPositionv(sId)` | sId: string | object | 获取注释逻辑位置 |

#### OLE对象

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_addOleObjectAction(sLocalUrl, sData, sApplicationId, fWidth, fHeight, nWidthPix, nHeightPix, bSelect, arrImagesForAddToHistory)` | ... | void | 添加OLE对象 |
| `asc_editOleObjectAction(oOleObject, sImageUrl, sData, fWidth, fHeight, nPixWidth, nPixHeight, arrImagesForAddToHistory)` | ... | void | 编辑OLE对象 |
| `asc_startEditCurrentOleObject()` | 无 | void | 开始编辑当前OLE对象 |
| `asc_doubleClickOnTableOleObject(obj)` | obj: object | void | 双击表格OLE对象 |
| `asc_addTableOleObjectInOleEditor(oOleObjectInfo)` | oOleObjectInfo: object | void | 在OLE编辑器中添加表格OLE对象 |
| `asc_getBinaryInfoOleObject()` | 无 | object | 获取OLE对象二进制信息 |
| `asc_toggleChangeVisibleAreaOleEditor(bForceValue)` | bForceValue: boolean | void | 切换OLE编辑器可见区域 |
| `asc_toggleShowVisibleAreaOleEditor(bForceValue)` | bForceValue: boolean | void | 切换显示OLE编辑器可见区域 |

#### 签名

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_addSignatureLine(oPr, Width, Height, sImgUrl)` | oPr: object, Width: number, Height: number, sImgUrl: string | void | 添加签名行 |
| `asc_getAllSignatures()` | 无 | array | 获取所有签名 |
| `asc_CallSignatureDblClickEvent(sGuid)` | sGuid: string | void | 调用签名双击事件 |

#### 宏

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getCurrentDrawingMacrosName()` | 无 | string | 获取当前绘图宏名称 |
| `asc_assignMacrosToCurrentDrawing(sName)` | sName: string | void | 为当前绘图分配宏 |

#### 打印设置

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_setPageOptions(options, index)` | options: object, index: number | void | 设置页面选项 |
| `asc_getPageOptions(index, initPrintTitles, opt_copy)` | index: number, initPrintTitles: boolean, opt_copy: boolean | object | 获取页面选项 |
| `asc_setPageOption(func, val, index)` | func: function, val: any, index: number | void | 设置页面选项 |
| `asc_savePagePrintOptions(arrPagesPrint)` | arrPagesPrint: array | void | 保存页面打印选项 |
| `asc_changeDocSize(width, height, index)` | width: number, height: number, index: number | void | 更改文档尺寸 |
| `asc_changePageMargins(left, right, top, bottom, index)` | left/right/top/bottom: number, index: number | void | 更改页边距 |
| `asc_changePageOrient(isPortrait, index)` | isPortrait: boolean, index: number | void | 更改页面方向 |
| `asc_SetPrintHeadings(val, index)` | val: boolean, index: number | void | 设置打印标题 |
| `asc_SetPrintGridlines(val, index)` | val: boolean, index: number | void | 设置打印网格线 |
| `asc_changePrintTitles(cols, rows, index)` | cols: object, rows: object, index: number | void | 更改打印标题 |
| `asc_getPrintTitlesRange(prop, byHeight, index)` | prop: number, byHeight: boolean, index: number | object | 获取打印标题范围 |
| `asc_ChangePrintArea(type)` | type: number | void | 更改打印区域 |
| `asc_CanAddPrintArea()` | 无 | boolean | 是否可以添加打印区域 |
| `asc_SetPrintScale(width, height, scale)` | width: number, height: number, scale: number | void | 设置打印缩放 |
| `asc_initPrintPreview(containerId, options)` | containerId: string, options: object | void | 初始化打印预览 |
| `asc_updatePrintPreview(options)` | options: object | void | 更新打印预览 |
| `asc_drawPrintPreview(index, indexSheet)` | index: number, indexSheet: number | void | 绘制打印预览 |
| `asc_closePrintPreview()` | 无 | void | 关闭打印预览 |

#### 视图设置

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getZoom()` | 无 | number | 获取缩放比例 |
| `asc_setZoom(scale)` | scale: number | void | 设置缩放比例 |
| `asc_Resize()` | 无 | void | 调整大小 |
| `asc_getSheetViewSettings()` | 无 | object | 获取工作表视图设置 |
| `asc_setDisplayGridlines(value)` | value: boolean | void | 设置显示网格线 |
| `asc_setDisplayHeadings(value)` | value: boolean | void | 设置显示行列标题 |
| `asc_setShowZeros(value)` | value: boolean | void | 设置显示零值 |
| `asc_setShowFormulas(value)` | value: boolean | void | 设置显示公式 |
| `asc_getShowFormulas()` | 无 | boolean | 获取是否显示公式 |
| `asc_setDate1904(value)` | value: boolean | void | 设置1904日期系统 |
| `asc_getDate1904()` | 无 | boolean | 获取1904日期系统 |
| `asc_setR1C1Mode(value)` | value: boolean | void | 设置R1C1引用模式 |
| `asc_getFrozenPaneBorderType()` | 无 | number | 获取冻结窗格边框类型 |
| `asc_setFrozenPaneBorderType(nType)` | nType: number | void | 设置冻结窗格边框类型 |
| `asc_getHeaderFooterMode()` | 无 | number | 获取页眉页脚模式 |

#### 拼写检查

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_setDefaultLanguage(val)` | val: number | void | 设置默认语言 |
| `asc_nextWord()` | 无 | void | 下一个单词 |
| `asc_replaceMisspelledWord(newWord, variantsFound, replaceAll)` | newWord: string, variantsFound: array, replaceAll: boolean | void | 替换拼写错误单词 |
| `asc_replaceMisspelledWords(options)` | options: object | void | 替换拼写错误单词(批量) |
| `asc_ignoreMisspelledWord(spellCheckProperty, ignoreAll)` | spellCheckProperty: object, ignoreAll: boolean | void | 忽略拼写错误单词 |
| `asc_ignoreNumbers(isIgnore)` | isIgnore: boolean | void | 忽略数字 |
| `asc_ignoreUppercase(isIgnore)` | isIgnore: boolean | void | 忽略大写 |
| `asc_cancelSpellCheck()` | 无 | void | 取消拼写检查 |

#### 剪贴板

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_Copy()` | 无 | void | 复制 |
| `asc_Paste()` | 无 | void | 粘贴 |
| `asc_Cut()` | 无 | void | 剪切 |
| `asc_SelectionCut()` | 无 | void | 选择剪切 |
| `asc_PasteData(_format, data1, data2, text_data)` | _format: string, data1: string, data2: string, text_data: string | void | 粘贴数据 |
| `asc_SpecialPaste(props)` | props: object | void | 特殊粘贴 |
| `asc_SpecialPasteData(props)` | props: object | void | 特殊粘贴数据 |
| `asc_ShowSpecialPasteButton(props)` | props: object | void | 显示特殊粘贴按钮 |
| `asc_UpdateSpecialPasteButton(props)` | props: object | void | 更新特殊粘贴按钮 |
| `asc_HideSpecialPasteButton()` | 无 | void | 隐藏特殊粘贴按钮 |
| `asc_CheckCopy(_clipboard, _formats)` | _clipboard: object, _formats: array | boolean | 检查复制 |
| `asc_bIsEmptyClipboard()` | 无 | boolean | 剪贴板是否为空 |
| `asc_canPaste()` | 无 | boolean | 是否可以粘贴 |

#### 导入导出

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_TextImport(options, callback, bPaste)` | options: object, callback: function, bPaste: boolean | void | 导入文本 |
| `asc_TextFromFileOrUrl(options, callback, url)` | options: object, callback: function, url: string | void | 从文件或URL导入文本 |
| `asc_TextToColumns(options, opt_text, opt_activeRange)` | options: object, opt_text: string, opt_activeRange: object | void | 文本分列 |
| `asc_ImportXmlStart(callback)` | callback: function | void | 开始导入XML |
| `asc_ImportXmlEnd(stream, dataRef, newSheetName)` | stream: object, dataRef: string, newSheetName: string | void | 结束导入XML |
| `asc_getBinaryFileWriter()` | 无 | object | 获取二进制文件写入器 |

#### 数据透视表

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_canGroupPivot()` | 无 | boolean | 是否可以分组数据透视表 |
| `asc_groupPivot(opt_rangePr, opt_dateTypes)` | opt_rangePr: object, opt_dateTypes: array | void | 分组数据透视表 |
| `asc_ungroupPivot()` | 无 | void | 取消分组数据透视表 |
| `asc_getTablePictures(props, pivot)` | props: object, pivot: boolean | object | 获取表格图片 |
| `asc_getSlicerPictures()` | 无 | object | 获取切片器图片 |

#### 迷你图

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_setSparklineGroup(id, oSparklineGroup)` | id: string, oSparklineGroup: object | void | 设置迷你图组 |

#### 撤销重做

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_Undo()` | 无 | void | 撤销 |
| `asc_Redo()` | 无 | void | 重做 |

#### 回调注册

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_registerCallback(name, callback, replaceOldCallback)` | name: string, callback: function, replaceOldCallback: boolean | void | 注册回调函数 |
| `asc_unregisterCallback(name, callback)` | name: string, callback: function | void | 注销回调函数 |

---

## 高级API类 (ApiBuilder)

### Api

全局API类，提供更简洁的链式调用接口。

**属性：**

| 属性 | 类型 | 说明 |
|------|------|------|
| `Sheets` | ApiWorksheet[] | 返回所有工作表集合 |
| `ActiveSheet` | ApiWorksheet | 返回活动工作表 |
| `Selection` | ApiRange | 返回选中的范围 |
| `Comments` | ApiComment[] | 返回所有注释 |

**方法：**

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `AddSheet(sName)` | sName: string | void | 添加新工作表 |
| `GetSheets()` | 无 | ApiWorksheet[] | 获取所有工作表 |
| `GetSheet(nameOrIndex)` | nameOrIndex: string/number | ApiWorksheet | 获取指定工作表 |
| `GetActiveSheet()` | 无 | ApiWorksheet | 获取活动工作表 |
| `SetLocale(LCID)` | LCID: number | void | 设置区域设置 |
| `GetLocale()` | 无 | number | 获取区域设置 |
| `GetThemesColors()` | 无 | string[] | 获取主题颜色列表 |
| `SetThemeColors(sTheme)` | sTheme: string | boolean | 设置主题颜色 |
| `CreateNewHistoryPoint()` | 无 | void | 创建新历史点 |
| `CreateColorFromRGB(r, g, b)` | r/g/b: number | ApiColor | 创建RGB颜色 |
| `CreateColorByName(sPresetColor)` | sPresetColor: string | ApiColor | 创建预设颜色 |
| `Format(expression, format)` | expression: any, format: string | string | 格式化表达式 |

### ApiWorksheet

工作表类。

**属性：**

| 属性 | 类型 | 说明 |
|------|------|------|
| `Visible` | boolean | 工作表可见性 |
| `Active` | number | 设置为活动工作表 |
| `ActiveCell` | ApiRange | 活动单元格 |
| `Selection` | ApiRange | 选中的范围 |
| `Cells` | ApiRange | 所有单元格 |
| `Rows` | ApiRange | 所有行 |
| `Cols` | ApiRange | 所有列 |
| `UsedRange` | ApiRange | 已使用的范围 |
| `Name` | string | 工作表名称 |
| `Index` | number | 工作表索引 |
| `LeftMargin` | number | 左边距 |
| `RightMargin` | number | 右边距 |
| `TopMargin` | number | 上边距 |
| `BottomMargin` | number | 下边距 |
| `PageOrientation` | string | 页面方向 |
| `PrintHeadings` | boolean | 打印标题 |
| `PrintGridlines` | boolean | 打印网格线 |
| `Defnames` | ApiName[] | 定义名称列表 |
| `Comments` | ApiComment[] | 注释列表 |

### ApiRange

范围类。

**属性：**

| 属性 | 类型 | 说明 |
|------|------|------|
| `Row` | number | 行号 |
| `Col` | number | 列号 |
| `Rows` | ApiRange | 行范围 |
| `Cols` | ApiRange | 列范围 |
| `Cells` | ApiRange | 单元格范围 |
| `Count` | number | 数量 |
| `Address` | string | 地址 |
| `Value` | string | 值 |
| `Formula` | string | 公式 |
| `Value2` | string | 值(无格式) |
| `Text` | string | 文本 |
| `FontColor` | ApiColor | 字体颜色 |
| `Hidden` | boolean | 是否隐藏 |
| `ColumnWidth` | number | 列宽 |
| `Width` | number | 宽度 |
| `RowHeight` | number | 行高 |
| `Height` | number | 高度 |
| `FontSize` | number | 字体大小 |
| `FontName` | string | 字体名称 |
| `AlignVertical` | string | 垂直对齐 |
| `AlignHorizontal` | string | 水平对齐 |
| `Bold` | boolean | 粗体 |
| `Italic` | boolean | 斜体 |
| `Underline` | string | 下划线类型 |
| `Strikeout` | boolean | 删除线 |
| `WrapText` | boolean | 自动换行 |
| `FillColor` | ApiColor | 填充颜色 |
| `NumberFormat` | string | 数字格式 |
| `MergeArea` | ApiRange | 合并区域 |
| `Worksheet` | ApiWorksheet | 所属工作表 |
| `DefName` | ApiName | 定义名称 |
| `Comments` | ApiComment | 注释 |
| `Orientation` | string | 文字方向 |
| `Areas` | ApiAreas | 区域集合 |
| `Characters` | ApiCharacters | 字符对象 |

### ApiColor

颜色类。

### ApiName

定义名称类。

**属性：**

| 属性 | 类型 | 说明 |
|------|------|------|
| `Name` | string | 名称 |
| `RefersTo` | string | 引用公式 |
| `RefersToRange` | ApiRange | 引用范围 |

### ApiComment

注释类。

**属性：**

| 属性 | 类型 | 说明 |
|------|------|------|
| `Text` | string | 注释文本 |

### ApiChart

图表类。

### ApiShape

形状类。

### ApiImage

图片类。

### ApiOleObject

OLE对象类。

---

## 枚举常量

### c_oAscMergeOptions

合并选项。

| 值 | 名称 | 说明 |
|----|------|------|
| -1 | Disabled | 禁用 |
| 0 | None | 无 |
| 1 | Merge | 合并 |
| 2 | MergeCenter | 合并并居中 |
| 3 | MergeAcross | 跨越合并 |

### c_oAscSortOptions

排序选项。

| 值 | 名称 | 说明 |
|----|------|------|
| 1 | Ascending | 升序 |
| 2 | Descending | 降序 |
| 3 | ByColorFill | 按填充颜色 |
| 4 | ByColorFont | 按字体颜色 |
| 5 | ByIcon | 按图标 |
| 6 | ByValue | 按值 |

### c_oAscBorderOptions

边框选项。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | Top | 上边框 |
| 1 | Right | 右边框 |
| 2 | Bottom | 下边框 |
| 3 | Left | 左边框 |
| 4 | DiagD | 对角线(下) |
| 5 | DiagU | 对角线(上) |
| 6 | InnerV | 内部垂直 |
| 7 | InnerH | 内部水平 |

### c_oAscCleanOptions

清除选项。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | All | 全部 |
| 1 | Text | 文本 |
| 2 | Format | 格式 |
| 4 | Formula | 公式 |
| 5 | Comments | 注释 |
| 6 | Hyperlinks | 超链接 |
| 7 | Sparklines | 迷你图 |
| 8 | SparklineGroups | 迷你图组 |

### c_oAscCellEditorState

单元格编辑器状态。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | editEnd | 编辑结束 |
| 1 | editStart | 编辑开始 |
| 2 | editEmptyCell | 编辑空单元格 |
| 3 | editText | 编辑文本 |
| 4 | editFormula | 编辑公式 |
| 5 | editInFormulaBar | 在公式栏编辑 |
| 6 | editInCell | 在单元格中编辑 |

### c_oAscHyperlinkType

超链接类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 1 | WebLink | 网页链接 |
| 2 | RangeLink | 范围链接 |

### c_oAscFindLookIn

查找范围。

| 值 | 名称 | 说明 |
|----|------|------|
| 1 | Formulas | 公式 |
| 2 | Value | 值 |
| 3 | Annotations | 批注 |

### c_oAscPaneState

窗格状态。

| 值 | 名称 | 说明 |
|----|------|------|
| "frozen" | Frozen | 冻结 |
| "frozenSplit" | FrozenSplit | 冻结拆分 |
| "split" | Split | 拆分 |

### c_oAscSparklineType

迷你图类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | Line | 折线图 |
| 1 | Column | 柱形图 |
| 2 | Stacked | 堆积图 |

### c_oAscAutoFilterTypes

自动筛选类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | ColorFilter | 颜色筛选 |
| 1 | CustomFilters | 自定义筛选 |
| 2 | DynamicFilter | 动态筛选 |
| 3 | Top10 | 前10项 |
| 4 | Filters | 筛选 |
| 5 | None | 无 |

### c_oAscSelectionDialogType

选择对话框类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | None | 无 |
| 1 | FormatTable | 格式化表格 |
| 2 | Chart | 图表 |
| 4 | FormatTableChangeRange | 更改表格范围 |
| 5 | CustomSort | 自定义排序 |
| 6 | PivotTableData | 数据透视表数据 |
| 7 | PivotTableReport | 数据透视表报表 |
| 8 | PrintTitles | 打印标题 |
| 9 | Function | 函数 |
| 10 | DataValidation | 数据验证 |
| 11 | ConditionalFormattingRule | 条件格式规则 |
| 12 | ImportXml | 导入XML |

### c_oAscHeaderFooterField

页眉页脚字段。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | pageNumber | 页码 |
| 1 | pageCount | 总页数 |
| 2 | sheetName | 工作表名称 |
| 3 | fileName | 文件名 |
| 4 | filePath | 文件路径 |
| 5 | date | 日期 |
| 6 | time | 时间 |
| 7 | lineBreak | 换行 |
| 8 | picture | 图片 |
| 9 | text | 文本 |

### c_oAscPageHFType

页眉页脚类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | firstHeader | 首页页眉 |
| 1 | oddHeader | 奇数页页眉 |
| 2 | evenHeader | 偶数页页眉 |
| 3 | firstFooter | 首页页脚 |
| 4 | oddFooter | 奇数页页脚 |
| 5 | evenFooter | 偶数页页脚 |

---

## 回调事件

通过 `asc_registerCallback` 方法注册的事件回调。

### 文档事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onDocumentModifiedChanged` | bIsModified: boolean | 文档修改状态改变 |
| `asc_onError` | errorId: number, errorLevel: number | 发生错误 |
| `asc_onStartAction` | type: number, id: number | 开始操作 |
| `asc_onEndAction` | type: number, id: number | 结束操作 |
| `asc_onOpenDocumentProgress` | progress: object | 打开文档进度 |

### 工作表事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onSheetsChanged` | 无 | 工作表列表改变 |
| `asc_onActiveSheetChanged` | index: number | 活动工作表改变 |

### 选择事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onSelectionChanged` | cellInfo: asc_CCellInfo | 选择改变 |
| `asc_onSelectionNameChanged` | name: string | 选择名称改变 |
| `asc_onEditorSelectionChanged` | cellXfs: object | 编辑器选择改变 |

### 编辑事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onEditCell` | state: number | 编辑单元格状态改变 |
| `asc_onCanUndoChanged` | bCanUndo: boolean | 可撤销状态改变 |
| `asc_onCanRedoChanged` | bCanRedo: boolean | 可重做状态改变 |

### 视图事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onZoomChanged` | zoom: number | 缩放改变 |
| `asc_onMouseMove` | mouseData: asc_CMouseMoveData | 鼠标移动 |

### 其他事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onInitEditorFonts` | fonts: object | 初始化编辑器字体 |
| `asc_onInitEditorStyles` | styles: object | 初始化编辑器样式 |
| `asc_onHyperlinkClick` | url: string | 超链接点击 |
| `asc_onCoAuthoringDisconnect` | 无 | 协作断开连接 |
| `asc_onAdvancedOptions` | id: number, options: object | 高级选项 |
| `asc_onSaveUrl` | url: string, callback: function | 保存URL |
| `asc_onPrintPreviewSheetChanged` | index: number | 打印预览工作表改变 |
| `asc_onPrintPreviewPageChanged` | index: number | 打印预览页改变 |

---

## 使用示例

### 初始化编辑器

```javascript
// 创建API实例
var api = new Asc.spreadsheet_api({
  'id-input': 'formulaInput'  // 公式输入框ID
});

// 注册回调
api.asc_registerCallback('asc_onSelectionChanged', function(cellInfo) {
  console.log('选择改变:', cellInfo);
});

api.asc_registerCallback('asc_onActiveSheetChanged', function(index) {
  console.log('活动工作表改变:', index);
});
```

### 工作表操作

```javascript
// 获取工作表数量
var count = api.asc_getWorksheetsCount();

// 获取活动工作表索引
var activeIndex = api.asc_getActiveWorksheetIndex();

// 添加工作表
api.asc_addWorksheet('新工作表');

// 重命名工作表
api.asc_renameWorksheet('新名称');

// 删除工作表
api.asc_deleteWorksheet([0, 1]);  // 删除索引为0和1的工作表
```

### 单元格操作

```javascript
// 获取单元格信息
var cellInfo = api.asc_getCellInfo();

// 设置单元格值
api.asc_setCellFormat('0.00');  // 数字格式
api.asc_setCellBold(true);      // 粗体
api.asc_setCellItalic(true);    // 斜体

// 设置字体
api.asc_setCellFontName('Arial');
api.asc_setCellFontSize(12);

// 设置颜色
var color = new Asc.asc_CColor();
color.r = 255;
color.g = 0;
color.b = 0;
api.asc_setCellTextColor(color);  // 文字颜色
api.asc_setCellBackgroundColor(color);  // 背景颜色

// 合并单元格
api.asc_mergeCells({type: Asc.c_oAscMergeOptions.Merge});

// 插入单元格
api.asc_insertCells({type: 0});  // 0=右移, 1=下移

// 删除单元格
api.asc_deleteCells({type: 0});  // 0=左移, 1=上移
```

### 行列操作

```javascript
// 设置列宽
api.asc_setColumnWidth(15);  // 15个字符宽

// 自动调整列宽
api.asc_autoFitColumnWidth();

// 设置行高
api.asc_setRowHeight(20);  // 20磅

// 隐藏列/行
api.asc_hideColumns();
api.asc_hideRows();

// 显示列/行
api.asc_showColumns();
api.asc_showRows();

// 分组
api.asc_group(1);  // 1=行分组, 0=列分组
```

### 筛选操作

```javascript
// 添加自动筛选
api.asc_addAutoFilter('TableStyleMedium9', null);

// 应用筛选
api.asc_applyAutoFilter(filterObject);

// 清除筛选
api.asc_clearFilter();
```

### 查找替换

```javascript
// 查找文本
api.asc_findText({
  Text: '搜索内容',
  MatchCase: false,
  WholeWords: false,
  LookIn: Asc.c_oAscFindLookIn.Formulas
}, function(result) {
  console.log('找到:', result);
});

// 替换文本
api.asc_replaceText({
  Text: '原内容',
  ReplaceWith: '新内容',
  MatchCase: false
});
```

### 使用高级API

```javascript
// 获取活动工作表
var sheet = Api.GetActiveSheet();

// 获取单元格范围
var range = sheet.GetRange('A1:B10');

// 设置值
range.Value = 'Hello World';

// 设置公式
range.Formula = '=SUM(A1:A10)';

// 设置格式
range.FontName = 'Arial';
range.FontSize = 12;
range.Bold = true;

// 获取值
var value = range.Value;

// 遍历工作表
var sheets = Api.GetSheets();
for (var i = 0; i < sheets.length; i++) {
  console.log('工作表名称:', sheets[i].Name);
}
```

### 图表操作

```javascript
// 获取图表对象
var chart = api.asc_getChartObject();

// 添加图表
api.asc_addChartDrawingObject({
  type: Asc.c_oAscChartTypeSettings.bar,
  range: 'A1:B10',
  inColumns: true
});
```

---

## 注意事项

1. Excel API 中的坐标从0开始，但显示时从1开始
2. 行高单位为磅(points)，列宽单位为字符宽度
3. 大部分方法需要等待编辑器初始化完成后才能调用
4. 回调函数的注册应在文档加载前完成
5. 部分功能需要服务器端支持

---

*文档版本: 1.0.0*
*基于 SE Office 项目整理*
