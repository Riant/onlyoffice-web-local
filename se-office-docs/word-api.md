# SE Office Word JavaScript API 文档

本文档整理自 SE Office 项目中 ONLYOFFICE Word 编辑器的 JavaScript API，用于二次开发扩展。

## 目录

- [核心API类](#核心api类)
- [属性类](#属性类)
- [枚举常量](#枚举常量)
- [回调事件](#回调事件)
- [使用示例](#使用示例)

***

## 核心API类

### asc\_docs\_api

Word文档编辑器的核心API类，提供文档操作的所有方法。

#### 初始化方法

| 方法                   | 参数            | 返回值    | 说明       |
| -------------------- | ------------- | ------ | -------- |
| `Init()`             | 无             | void   | 初始化编辑器   |
| `InitEditor()`       | 无             | void   | 初始化编辑器模式 |
| `InitViewer()`       | 无             | void   | 初始化查看器模式 |
| `asc_setLocale(val)` | val: string   | void   | 设置区域设置   |
| `asc_getLocale()`    | 无             | string | 获取当前区域设置 |
| `asc_setSkin(theme)` | theme: string | void   | 设置皮肤主题   |

#### 文档操作

| 方法                                     | 参数                             | 返回值  | 说明         |
| -------------------------------------- | ------------------------------ | ---- | ---------- |
| `OpenDocument(url, gObject)`           | url: string, gObject: object   | void | 打开文档       |
| `OpenDocumentFromBin(url, gObject)`    | url: string, gObject: object   | void | 从二进制数据打开文档 |
| `OpenDocumentFromZip(data)`            | data: ArrayBuffer              | void | 从ZIP数据打开文档 |
| `asc_DownloadAs(options)`              | options: asc\_CDownloadOptions | void | 下载文档为指定格式  |
| `asc_DownloadOrigin(bIsDownloadEvent)` | bIsDownloadEvent: boolean      | void | 下载原始文档     |
| `asc_CloseFile()`                      | 无                              | void | 关闭文件       |
| `asc_Recalculate(bIsUpdateInterface)`  | bIsUpdateInterface: boolean    | void | 重新计算文档     |

#### 文档状态

| 方法                            | 参数              | 返回值     | 说明         |
| ----------------------------- | --------------- | ------- | ---------- |
| `isDocumentModified()`        | 无               | boolean | 文档是否已修改    |
| `SetDocumentModified(bValue)` | bValue: boolean | void    | 设置文档修改状态   |
| `CheckChangedDocument()`      | 无               | void    | 检查文档是否已更改  |
| `SetUnchangedDocument()`      | 无               | void    | 设置文档为未更改状态 |

#### 撤销/重做

| 方法                     | 参数 | 返回值  | 说明     |
| ---------------------- | -- | ---- | ------ |
| `asc_undoAllChanges()` | 无  | void | 撤销所有更改 |
| `asc_onUndo()`         | 无  | void | 撤销操作回调 |
| `asc_onRedo()`         | 无  | void | 重做操作回调 |

#### 文本操作

| 方法                                       | 参数                                         | 返回值    | 说明             |
| ---------------------------------------- | ------------------------------------------ | ------ | -------------- |
| `asc_AddText(sText, oSettings)`          | sText: string, oSettings: CAddTextSettings | string | 在当前位置插入文本      |
| `asc_GetSelectedText(bClearText, select_Pr)` | bClearText: boolean, select_Pr: object  | string | 获取选中的文本        |
| `asc_RemoveSelection()`                  | 无                                          | string | 移除选择           |
| `asc_EditSelectAll()`                    | 无                                          | void   | 全选文档内容         |
| `asc_enterText(value)`                   | value: string                              | boolean | 输入文本           |
| `asc_correctEnterText(oldValue, newValue)` | oldValue: string, newValue: string       | boolean | 更正输入的文本        |
| `asc_GetCurrentWord(nDirection)`         | nDirection: number                         | string | 获取当前单词         |
| `asc_ReplaceCurrentWord(nDirection, sReplace)` | nDirection: number, sReplace: string  | string | 替换当前单词         |
| `Add_CompositeText(nCharCode)`           | nCharCode: number                          | void   | 添加组合文本(输入法)    |
| `Remove_CompositeText(nCount)`           | nCount: number                             | void   | 移除组合文本         |
| `Begin_CompositeInput()`                 | 无                                          | void   | 开始组合输入(输入法)    |
| `asc_AddBlankPage()`                     | 无                                          | void   | 添加空白页          |

#### 文本属性设置

| 方法                                    | 参数                               | 返回值  | 说明            |
| ------------------------------------- | -------------------------------- | ---- | ------------- |
| `put_TextPrFontName(name)`            | name: string                     | void | 设置字体名称        |
| `put_TextPrFontSize(size)`            | size: number                     | void | 设置字体大小        |
| `put_TextPrBold(value)`               | value: boolean                   | void | 设置粗体          |
| `put_TextPrItalic(value)`             | value: boolean                   | void | 设置斜体          |
| `put_TextPrUnderline(value)`          | value: boolean                   | void | 设置下划线         |
| `put_TextPrStrikeout(value)`          | value: boolean                   | void | 设置删除线         |
| `put_TextPrDStrikeout(value)`         | value: boolean                   | void | 设置双删除线        |
| `put_TextPrSpacing(value)`            | value: number                    | void | 设置字符间距        |
| `put_TextPrCaps(value)`               | value: boolean                   | void | 设置大写          |
| `put_TextPrSmallCaps(value)`          | value: boolean                   | void | 设置小型大写        |
| `put_TextPrPosition(value)`           | value: number                    | void | 设置文字位置        |
| `put_TextPrLang(value)`               | value: number                    | void | 设置语言          |
| `put_TextPrBaseline(value)`           | value: number                    | void | 设置基线位置(上标/下标) |
| `put_TextColor(color)`                | color: asc\_CColor               | void | 设置文字颜色        |
| `put_LineHighLight(is_flag, r, g, b)` | is\_flag: boolean, r/g/b: number | void | 设置文字高亮        |

#### 段落属性设置

| 方法                                               | 参数                                                         | 返回值  | 说明          |
| ------------------------------------------------ | ---------------------------------------------------------- | ---- | ----------- |
| `put_PrAlign(value)`                             | value: number                                              | void | 设置段落对齐方式    |
| `put_PrLineSpacing(Type, Value)`                 | Type: number, Value: number                                | void | 设置行距        |
| `put_LineSpacingBeforeAfter(type, value)`        | type: number, value: number                                | void | 设置段前/段后间距   |
| `put_PrIndent(value, levelValue)`                | value: number, levelValue: number                          | void | 设置左缩进       |
| `put_PrIndentRight(value)`                       | value: number                                              | void | 设置右缩进       |
| `put_PrFirstLineIndent(value)`                   | value: number                                              | void | 设置首行缩进      |
| `put_Margins(left, top, right, bottom)`          | left/top/right/bottom: number                              | void | 设置页边距       |
| `put_PageBreak(isBreak)`                         | isBreak: boolean                                           | void | 设置分页符       |
| `put_WidowControl(bValue)`                       | bValue: boolean                                            | void | 设置孤行控制      |
| `put_KeepLines(isKeepLines)`                     | isKeepLines: boolean                                       | void | 设置段中不分页     |
| `put_KeepNext(isKeepNext)`                       | isKeepNext: boolean                                        | void | 设置与下段同页     |
| `put_AddSpaceBetweenPrg(isSpacePrg)`             | isSpacePrg: boolean                                        | void | 设置段前段后不添加空格 |
| `put_ParagraphShade(is_flag, color, isOnlyPara)` | is\_flag: boolean, color: asc\_CColor, isOnlyPara: boolean | void | 设置段落底纹      |
| `put_Style(sName)`                               | sName: string                                              | void | 应用样式        |
| `put_Borders(Obj)`                               | Obj: asc\_CParagraphBorders                                | void | 设置段落边框      |

#### 列表/编号

| 方法                                                       | 参数                                                     | 返回值    | 说明        |
| -------------------------------------------------------- | ------------------------------------------------------ | ------ | --------- |
| `put_ListType(type, subtype)`                            | type: number, subtype: number                          | void   | 设置列表类型    |
| `put_ListTypeCustom(value)`                              | value: object                                          | void   | 设置自定义列表类型 |
| `asc_GetCurrentNumberingId()`                            | 无                                                      | string | 获取当前编号ID  |
| `asc_GetCurrentNumberingLvl()`                           | 无                                                      | number | 获取当前编号级别  |
| `asc_GetCalculatedNumberingValue()`                      | 无                                                      | string | 获取计算后的编号值 |
| `asc_GetNumberingPr(sNumId)`                             | sNumId: string                                         | object | 获取编号属性    |
| `asc_AddNewNumbering(oAscNumbering, isApply)`            | oAscNumbering: object, isApply: boolean                | void   | 添加新编号     |
| `asc_ChangeNumberingLvl(sNumId, oAscNumberingLvl, nLvl)` | sNumId: string, oAscNumberingLvl: object, nLvl: number | void   | 更改编号级别    |
| `asc_SetNumberingLvl(nLvl)`                              | nLvl: number                                           | void   | 设置编号级别    |
| `asc_ContinueNumbering()`                                | 无                                                      | void   | 继续编号      |
| `asc_RestartNumbering(nRestartValue)`                    | nRestartValue: number                                  | void   | 重新开始编号    |

#### 表格操作

| 方法                                                | 参数                                         | 返回值   | 说明       |
| ------------------------------------------------- | ------------------------------------------ | ----- | -------- |
| `put_Table(col, row, sStyleId)`                   | col: number, row: number, sStyleId: string | void  | 插入表格     |
| `put_CellsMargin(left, top, right, bottom)`       | left/top/right/bottom: number              | void  | 设置单元格边距  |
| `asc_DistributeTableCells(isHorizontally)`        | isHorizontally: boolean                    | void  | 平均分布单元格  |
| `asc_RemoveTableCells()`                          | 无                                          | void  | 删除单元格    |
| `asc_getTableStylesPreviews(bUseDefault, arrIds)` | bUseDefault: boolean, arrIds: array        | array | 获取表格样式预览 |
| `asc_generateTableStylesPreviews(bUseDefault)`    | bUseDefault: boolean                       | void  | 生成表格样式预览 |
| `asc_GetDefaultTableStyles()`                     | 无                                          | array | 获取默认表格样式 |

#### 图片/形状操作

| 方法                                                                                                                                    | 参数                              | 返回值     | 说明          |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------- | ----------- |
| `put_ShapesAlign(type, alignType)`                                                                                                    | type: number, alignType: number | void    | 对齐形状        |
| `get_OriginalSizeImage()`                                                                                                             | 无                               | object  | 获取图片原始尺寸    |
| `asc_getSelectedDrawingObjectsCount()`                                                                                                | 无                               | number  | 获取选中绘图对象数量  |
| `asc_addOleObjectAction(sLocalUrl, sData, sApplicationId, fWidth, fHeight, nWidthPix, nHeightPix, bSelect, arrImagesForAddToHistory)` | ...                             | void    | 添加OLE对象     |
| `asc_editOleObjectAction(oOleObject, sImageUrl, sData, fWidthMM, fHeightMM, nPixWidth, nPixHeight, arrImagesForAddToHistory)`         | ...                             | void    | 编辑OLE对象     |
| `asc_startEditCurrentOleObject()`                                                                                                     | 无                               | void    | 开始编辑当前OLE对象 |
| `asc_canEditCrop()`                                                                                                                   | 无                               | boolean | 是否可以裁剪      |
| `asc_startEditCrop()`                                                                                                                 | 无                               | void    | 开始裁剪        |
| `asc_endEditCrop()`                                                                                                                   | 无                               | void    | 结束裁剪        |
| `asc_cropFit()`                                                                                                                       | 无                               | void    | 裁剪适应        |
| `asc_cropFill()`                                                                                                                      | 无                               | void    | 裁剪填充        |

#### 图表操作

| 方法                                        | 参数                       | 返回值    | 说明     |
| ----------------------------------------- | ------------------------ | ------ | ------ |
| `asc_getChartObject(type)`                | type: number             | object | 获取图表对象 |
| `asc_addChartDrawingObject(options)`      | options: object          | void   | 添加图表   |
| `asc_doubleClickOnChart(obj)`             | obj: object              | void   | 双击图表   |
| `asc_onCloseChartFrame()`                 | 无                        | void   | 关闭图表框架 |
| `asc_editChartDrawingObject(chartBinary)` | chartBinary: ArrayBuffer | void   | 编辑图表   |

#### 超链接

| 方法                          | 参数 | 返回值   | 说明      |
| --------------------------- | -- | ----- | ------- |
| `asc_GetHyperlinkAnchors()` | 无  | array | 获取超链接锚点 |

#### 搜索替换

| 方法                                                   | 参数                                                         | 返回值     | 说明          |
| ---------------------------------------------------- | ---------------------------------------------------------- | ------- | ----------- |
| `asc_searchEnabled(bIsEnabled)`                      | bIsEnabled: boolean                                        | void    | 启用/禁用搜索     |
| `asc_findText(oProps, isNext, callback)`             | oProps: object, isNext: boolean, callback: function        | void    | 查找文本        |
| `asc_endFindText()`                                  | 无                                                          | void    | 结束查找        |
| `asc_replaceText(oProps, replaceWith, isReplaceAll)` | oProps: object, replaceWith: string, isReplaceAll: boolean | void    | 替换文本        |
| `asc_GetErrorForReplaceString(sString)`              | sString: string                                            | boolean | 检查替换字符串是否有误 |
| `asc_isSelectSearchingResults()`                     | 无                                                          | boolean | 是否选中搜索结果    |
| `asc_StartTextAroundSearch()`                        | 无                                                          | void    | 开始搜索上下文     |
| `asc_SelectSearchElement(sId)`                       | sId: string                                                | void    | 选择搜索元素      |

#### 拼写检查

| 方法                                                    | 参数                                        | 返回值    | 说明        |
| ----------------------------------------------------- | ----------------------------------------- | ------ | --------- |
| `asc_replaceMisspelledWord(Word, SpellCheckProperty)` | Word: string, SpellCheckProperty: object  | void   | 替换拼写错误单词  |
| `asc_ignoreMisspelledWord(SpellCheckProperty, bAll)`  | SpellCheckProperty: object, bAll: boolean | void   | 忽略拼写错误    |
| `asc_spellCheckClearDictionary()`                     | 无                                         | void   | 清除拼写检查字典  |
| `asc_setDefaultLanguage(Lang)`                        | Lang: number                              | void   | 设置默认语言    |
| `asc_getDefaultLanguage()`                            | 无                                         | number | 获取默认语言    |
| `asc_getKeyboardLanguage()`                           | 无                                         | number | 获取键盘语言    |
| `asc_setSpellCheck(isOn)`                             | isOn: boolean                             | void   | 开启/关闭拼写检查 |
| `asc_restartCheckSpelling()`                          | 无                                         | void   | 重新开始拼写检查  |
| `asc_setSpellCheckSettings(oSettings)`                | oSettings: object                         | void   | 设置拼写检查设置  |
| `asc_getSpellCheckSettings()`                         | 无                                         | object | 获取拼写检查设置  |

#### 注释

| 方法                                                  | 参数                                                 | 返回值    | 说明           |
| --------------------------------------------------- | -------------------------------------------------- | ------ | ------------ |
| `asc_showComments(isShowSolved)`                    | isShowSolved: boolean                              | void   | 显示注释         |
| `asc_hideComments()`                                | 无                                                  | void   | 隐藏注释         |
| `asc_addComment(AscCommentData)`                    | AscCommentData: object                             | void   | 添加注释         |
| `asc_removeComment(Id)`                             | Id: string                                         | void   | 删除注释         |
| `asc_changeComment(Id, AscCommentData)`             | Id: string, AscCommentData: object                 | void   | 修改注释         |
| `asc_selectComment(Id)`                             | Id: string                                         | void   | 选择注释         |
| `asc_showComment(Id)`                               | Id: string                                         | void   | 显示注释         |
| `asc_GetCommentsReportByAuthors()`                  | 无                                                  | object | 获取按作者分组的注释报告 |
| `asc_RemoveAllComments(isMine, isCurrent, arrIds)`  | isMine: boolean, isCurrent: boolean, arrIds: array | void   | 删除所有注释       |
| `asc_ResolveAllComments(isMine, isCurrent, arrIds)` | isMine: boolean, isCurrent: boolean, arrIds: array | void   | 解决所有注释       |
| `asc_GetCommentLogicPosition(sId)`                  | sId: string                                        | object | 获取注释逻辑位置     |

#### 页眉页脚

| 方法                                     | 参数                           | 返回值  | 说明       |
| -------------------------------------- | ---------------------------- | ---- | -------- |
| `put_HeadersAndFootersDistance(value)` | value: number                | void | 设置页眉页脚距离 |
| `asc_RemoveHeader(pageNumber)`         | pageNumber: number           | void | 删除页眉     |
| `asc_RemoveFooter(pageNumber)`         | pageNumber: number           | void | 删除页脚     |
| `put_PageNum(where, align)`            | where: number, align: number | void | 插入页码     |

#### 节/页面设置

| 方法                                                       | 参数                                            | 返回值         | 说明      |
| -------------------------------------------------------- | --------------------------------------------- | ----------- | ------- |
| `asc_SetSectionProps(Props)`                             | Props: CAscSection                            | void        | 设置节属性   |
| `asc_GetSectionProps()`                                  | 无                                             | CAscSection | 获取节属性   |
| `asc_GetCurrentColumnWidth()`                            | 无                                             | number      | 获取当前列宽  |
| `asc_SetColumnsProps(ColumnsProps)`                      | ColumnsProps: object                          | void        | 设置分栏属性  |
| `asc_GetColumnsProps()`                                  | 无                                             | object      | 获取分栏属性  |
| `asc_SetLineNumbersProps(nApplyType, oLineNumbersProps)` | nApplyType: number, oLineNumbersProps: object | void        | 设置行号属性  |
| `asc_GetLineNumbersProps()`                              | 无                                             | object      | 获取行号属性  |
| `asc_GetWatermarkProps()`                                | 无                                             | object      | 获取水印属性  |
| `asc_SetWatermarkProps(oProps)`                          | oProps: object                                | void        | 设置水印属性  |
| `asc_WatermarkRemove(oProps)`                            | oProps: object                                | void        | 删除水印    |
| `asc_SetSectionStartPage(nStartPage)`                    | nStartPage: number                            | void        | 设置节起始页码 |
| `get_DocumentOrientation()`                              | 无                                             | boolean     | 获取文档方向  |
| `get_DocumentWidth()`                                    | 无                                             | number      | 获取文档宽度  |
| `get_DocumentHeight()`                                   | 无                                             | number      | 获取文档高度  |
| `asc_GetSectionsCount()`                                 | 无                                             | number      | 获取节数量   |

#### 脚注/尾注

| 方法                                                            | 参数                                                            | 返回值     | 说明       |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------- | -------- |
| `asc_SetFootnoteProps(oFootnotePr, bApplyToAll)`              | oFootnotePr: object, bApplyToAll: boolean                     | void    | 设置脚注属性   |
| `asc_GetFootnoteProps()`                                      | 无                                                             | object  | 获取脚注属性   |
| `asc_AddFootnote(sText)`                                      | sText: string                                                 | void    | 添加脚注     |
| `asc_RemoveAllFootnotes(bRemoveFootnotes, bRemoveEndnotes)`   | bRemoveFootnotes: boolean, bRemoveEndnotes: boolean           | void    | 删除所有脚注   |
| `asc_GotoFootnote(isNext)`                                    | isNext: boolean                                               | void    | 跳转到脚注    |
| `asc_IsCursorInFootnote()`                                    | 无                                                             | boolean | 光标是否在脚注中 |
| `asc_AddEndnote(sText)`                                       | sText: string                                                 | void    | 添加尾注     |
| `asc_GotoEndnote(isNext)`                                     | isNext: boolean                                               | void    | 跳转到尾注    |
| `asc_IsCursorInEndnote()`                                     | 无                                                             | boolean | 光标是否在尾注中 |
| `asc_SetEndnoteProps(oEndnotePr, bApplyToAll)`                | oEndnotePr: object, bApplyToAll: boolean                      | void    | 设置尾注属性   |
| `asc_GetEndnoteProps()`                                       | 无                                                             | object  | 获取尾注属性   |
| `asc_ConvertFootnoteType(isCurrent, isFootnotes, isEndnotes)` | isCurrent: boolean, isFootnotes: boolean, isEndnotes: boolean | void    | 转换脚注类型   |

#### 内容控件

| 方法                                                                     | 参数                                                                       | 返回值     | 说明           |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------- | ------------ |
| `asc_AddContentControl(nType, oContentControlPr)`                      | nType: number, oContentControlPr: object                                 | void    | 添加内容控件       |
| `asc_AddContentControlCheckBox(oPr, oInternalPr, oCommonPr)`           | oPr: object, oInternalPr: object, oCommonPr: object                      | void    | 添加复选框内容控件    |
| `asc_AddContentControlPicture(oInternalPr, oCommonPr)`                 | oInternalPr: object, oCommonPr: object                                   | void    | 添加图片内容控件     |
| `asc_AddContentControlList(isComboBox, oPr, oInternalPr, oCommonPr)`   | isComboBox: boolean, oPr: object, oInternalPr: object, oCommonPr: object | void    | 添加下拉列表内容控件   |
| `asc_AddContentControlDatePicker(oPr, oCommonPr)`                      | oPr: object, oCommonPr: object                                           | void    | 添加日期选择器内容控件  |
| `asc_RemoveContentControl(Id)`                                         | Id: string                                                               | void    | 删除内容控件       |
| `asc_RemoveContentControlWrapper(Id)`                                  | Id: string                                                               | void    | 删除内容控件包装器    |
| `asc_SetContentControlProperties(oContentControlPr, Id, isApplyToAll)` | oContentControlPr: object, Id: string, isApplyToAll: boolean             | void    | 设置内容控件属性     |
| `asc_IsContentControl()`                                               | 无                                                                        | boolean | 是否在内容控件中     |
| `asc_GetContentControlProperties()`                                    | 无                                                                        | object  | 获取内容控件属性     |
| `asc_GetCurrentContentControl()`                                       | 无                                                                        | object  | 获取当前内容控件     |
| `asc_ClearContentControl(sId)`                                         | sId: string                                                              | void    | 清除内容控件内容     |
| `asc_GetContentControlRightAnchorPosition(sId)`                        | sId: string                                                              | object  | 获取内容控件右锚点位置  |
| `asc_GetContentControlBoundingRect(sId)`                               | sId: string                                                              | object  | 获取内容控件边界矩形   |
| `asc_SetGlobalContentControlHighlightColor(r, g, b)`                   | r/g/b: number                                                            | void    | 设置内容控件高亮颜色   |
| `asc_GetGlobalContentControlHighlightColor(isDefault)`                 | isDefault: boolean                                                       | object  | 获取内容控件高亮颜色   |
| `asc_SetGlobalContentControlShowHighlight(isShow, r, g, b)`            | isShow: boolean, r/g/b: number                                           | void    | 设置是否显示内容控件高亮 |
| `asc_GetGlobalContentControlShowHighlight()`                           | 无                                                                        | boolean | 获取是否显示内容控件高亮 |
| `asc_SetContentControlCheckBoxPr(oPr)`                                 | oPr: object                                                              | void    | 设置复选框属性      |
| `asc_SetContentControlCheckBoxChecked(isChecked, sId)`                 | isChecked: boolean, sId: string                                          | void    | 设置复选框选中状态    |
| `asc_IsContentControlCheckBoxChecked(sId)`                             | sId: string                                                              | boolean | 复选框是否选中      |
| `asc_SetContentControlPictureUrl(sUrl, sId, sToken)`                   | sUrl: string, sId: string, sToken: string                                | void    | 设置内容控件图片URL  |
| `asc_SetContentControlListPr(oPr, sId)`                                | oPr: object, sId: string                                                 | void    | 设置下拉列表属性     |
| `asc_SelectContentControlListItem(sValue, sId)`                        | sValue: string, sId: string                                              | void    | 选择下拉列表项      |
| `asc_GetContentControlListCurrentValue(sId)`                           | sId: string                                                              | string  | 获取下拉列表当前值    |
| `asc_SetContentControlDatePickerPr(oPr, sId, updateDate)`              | oPr: object, sId: string, updateDate: boolean                            | void    | 设置日期选择器属性    |
| `asc_SetContentControlDatePickerDate(oPr, sId)`                        | oPr: object, sId: string                                                 | void    | 设置日期选择器日期    |
| `asc_SetContentControlTextPlaceholder(sText, sId)`                     | sText: string, sId: string                                               | void    | 设置内容控件占位文本   |
| `asc_SetContentControlText(sText, sId)`                                | sText: string, sId: string                                               | void    | 设置内容控件文本     |

#### 表单

| 方法                                                       | 参数                                                         | 返回值     | 说明            |
| -------------------------------------------------------- | ---------------------------------------------------------- | ------- | ------------- |
| `asc_GetTextFormKeys()`                                  | 无                                                          | array   | 获取文本表单键       |
| `asc_GetPictureFormKeys()`                               | 无                                                          | array   | 获取图片表单键       |
| `asc_GetCheckBoxFormKeys()`                              | 无                                                          | array   | 获取复选框表单键      |
| `asc_GetRadioButtonGroupKeys()`                          | 无                                                          | array   | 获取单选按钮组键      |
| `asc_GetFormKeysByType(type)`                            | type: number                                               | array   | 按类型获取表单键      |
| `asc_ClearAllSpecialForms()`                             | 无                                                          | void    | 清除所有特殊表单      |
| `asc_SetSpecialFormsHighlightColor(r, g, b)`             | r/g/b: number                                              | void    | 设置表单高亮颜色      |
| `asc_GetSpecialFormsHighlightColor()`                    | 无                                                          | object  | 获取表单高亮颜色      |
| `asc_SetPerformContentControlActionByClick(isPerform)`   | isPerform: boolean                                         | void    | 设置点击时执行内容控件操作 |
| `asc_GetTextFormAutoWidth(sId)`                          | sId: string                                                | number  | 获取文本表单自动宽度    |
| `asc_GetFormsCountByKey(sKey)`                           | sKey: string                                               | number  | 按键获取表单数量      |
| `asc_MoveToFillingForm(isNext, isRequired, isNotFilled)` | isNext: boolean, isRequired: boolean, isNotFilled: boolean | void    | 移动到填充表单       |
| `asc_IsAllRequiredFormsFilled()`                         | 无                                                          | boolean | 是否所有必填表单已填充   |
| `asc_SetFixedForm(sId, isFixed)`                         | sId: string, isFixed: boolean                              | void    | 设置固定表单        |
| `asc_IsHighlightRequiredFields()`                        | 无                                                          | boolean | 是否高亮必填字段      |
| `asc_SetHighlightRequiredFields(isHighlight)`            | isHighlight: boolean                                       | void    | 设置是否高亮必填字段    |
| `asc_GetAllFormsData()`                                  | 无                                                          | array   | 获取所有表单数据      |
| `asc_GetOForm()`                                         | 无                                                          | object  | 获取OForm数据     |

#### 书签

| 方法                                       | 参数                                                       | 返回值    | 说明             |
| ---------------------------------------- | -------------------------------------------------------- | ------ | -------------- |
| `asc_GetBookmarksManager()`              | 无                                                        | object | 获取书签管理器         |
| `asc_OnBookmarksUpdate()`                | 无                                                        | void   | 触发书签更新事件        |
| `asc_AddCrossRefToBookmark(sName, nType, bHyperlink, bAboveBelow, sSeparator)` | sName: string, nType: number, bHyperlink: boolean, bAboveBelow: boolean, sSeparator: string | void | 添加书签交叉引用 |

**CBookmarksManager 书签管理器方法：**

| 方法                              | 参数            | 返回值     | 说明              |
| ------------------------------- | ------------- | ------- | --------------- |
| `asc_GetCount()`                | 无             | number  | 获取书签数量          |
| `asc_GetName(nIndex)`           | nIndex: number | string  | 按索引获取书签名称       |
| `asc_GetId(nIndex)`             | nIndex: number | string  | 按索引获取书签ID       |
| `asc_AddBookmark(sName)`        | sName: string  | boolean | 添加书签            |
| `asc_RemoveBookmark(sName)`     | sName: string  | boolean | 删除书签            |
| `asc_GoToBookmark(sName)`       | sName: string  | boolean | 跳转到书签           |
| `asc_HaveBookmark(sName)`       | sName: string  | boolean | 检查书签是否存在        |
| `asc_IsHiddenBookmark(sName)`   | sName: string  | boolean | 是否为隐藏书签         |
| `asc_IsInternalUseBookmark(sName)` | sName: string | boolean | 是否为内部使用书签       |
| `asc_CheckNewBookmarkName(sName)` | sName: string | boolean | 检查新书签名称是否有效     |
| `asc_SelectBookmark(sName)`     | sName: string  | boolean | 选中书签内容          |
| `asc_IsInternalUseBookmark(sName)` | sName: string | boolean | 是否为内部使用书签       |

**CHyperlinkAnchor 超链接锚点方法（用于书签和标题）：**

| 方法                              | 返回值     | 说明              |
| ------------------------------- | ------- | --------------- |
| `asc_GetType()`                 | number  | 获取锚点类型          |
| `asc_GetBookmarkName()`         | string  | 获取书签名称          |
| `asc_GetHeadingText()`          | string  | 获取标题文本          |
| `asc_GetHeadingLevel()`         | number  | 获取标题级别          |
| `asc_GetHeadingParagraph()`     | object  | 获取标题段落对象        |

#### 修订追踪

| 方法                                            | 参数                         | 返回值     | 说明           |
| --------------------------------------------- | -------------------------- | ------- | ------------ |
| `asc_SetTrackRevisions(bTrack)`               | bTrack: boolean            | void    | 设置修订追踪       |
| `asc_IsTrackRevisions()`                      | 无                          | boolean | 是否启用修订追踪     |
| `asc_SetLocalTrackRevisions(bTrack)`          | bTrack: boolean            | void    | 设置本地修订追踪     |
| `asc_GetLocalTrackRevisions()`                | 无                          | boolean | 获取本地修订追踪状态   |
| `asc_SetGlobalTrackRevisions(bTrack)`         | bTrack: boolean            | void    | 设置全局修订追踪     |
| `asc_GetGlobalTrackRevisions()`               | 无                          | boolean | 获取全局修订追踪状态   |
| `asc_GetRevisionsChangesStack()`              | 无                          | array   | 获取修订更改栈      |
| `asc_AcceptChanges(oChange)`                  | oChange: object            | void    | 接受更改         |
| `asc_RejectChanges(oChange)`                  | oChange: object            | void    | 拒绝更改         |
| `asc_AcceptChangesBySelection(moveToNext)`    | moveToNext: boolean        | void    | 接受选中更改       |
| `asc_RejectChangesBySelection(moveToNext)`    | moveToNext: boolean        | void    | 拒绝选中更改       |
| `asc_HaveRevisionsChanges(isCheckOwnChanges)` | isCheckOwnChanges: boolean | boolean | 是否有修订更改      |
| `asc_HaveNewRevisionsChanges()`               | 无                          | boolean | 是否有新修订更改     |
| `asc_GetNextRevisionsChange()`                | 无                          | object  | 获取下一个修订更改    |
| `asc_GetPrevRevisionsChange()`                | 无                          | object  | 获取上一个修订更改    |
| `asc_AcceptAllChanges()`                      | 无                          | void    | 接受所有更改       |
| `asc_RejectAllChanges()`                      | 无                          | void    | 拒绝所有更改       |
| `asc_GetTrackRevisionsReportByAuthors()`      | 无                          | object  | 获取按作者分组的修订报告 |
| `asc_FollowRevisionMove(oChange)`             | oChange: object            | void    | 跟随修订移动       |
| `asc_BeginViewModeInReview(isFinal)`          | isFinal: boolean           | void    | 开始审阅视图模式     |
| `asc_EndViewModeInReview()`                   | 无                          | void    | 结束审阅视图模式     |
| `asc_SetDisplayModeInReview(nMode)`           | nMode: number              | void    | 设置审阅显示模式     |
| `asc_GetDisplayModeInReview()`                | 无                          | number  | 获取审阅显示模式     |

#### 样式

| 方法                                 | 参数              | 返回值     | 说明        |
| ---------------------------------- | --------------- | ------- | --------- |
| `asc_GetStyleFromFormatting()`     | 无               | object  | 从格式获取样式   |
| `asc_AddNewStyle(oStyle)`          | oStyle: object  | void    | 添加新样式     |
| `asc_RemoveStyle(sName)`           | sName: string   | void    | 删除样式      |
| `asc_RemoveAllCustomStyles()`      | 无               | void    | 删除所有自定义样式 |
| `asc_IsStyleDefault(sName)`        | sName: string   | boolean | 是否为默认样式   |
| `asc_IsDefaultStyleChanged(sName)` | sName: string   | boolean | 默认样式是否已更改 |
| `asc_GetStyleNameById(StyleId)`    | StyleId: string | string  | 按ID获取样式名称 |

#### 邮件合并

| 方法                                                                     | 参数                                                                           | 返回值    | 说明          |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------ | ----------- |
| `asc_StartMailMerge(oData)`                                            | oData: object                                                                | void   | 开始邮件合并      |
| `asc_StartMailMergeByList(aList)`                                      | aList: array                                                                 | void   | 通过列表开始邮件合并  |
| `asc_GetReceptionsCount()`                                             | 无                                                                            | number | 获取收件人数量     |
| `asc_GetMailMergeFieldsNameList()`                                     | 无                                                                            | array  | 获取邮件合并字段名列表 |
| `asc_AddMailMergeField(Name)`                                          | Name: string                                                                 | void   | 添加邮件合并字段    |
| `asc_SetHighlightMailMergeFields(Value)`                               | Value: boolean                                                               | void   | 设置高亮邮件合并字段  |
| `asc_PreviewMailMergeResult(Index)`                                    | Index: number                                                                | void   | 预览邮件合并结果    |
| `asc_EndPreviewMailMergeResult()`                                      | 无                                                                            | void   | 结束预览邮件合并结果  |
| `asc_getMailMergeData()`                                               | 无                                                                            | array  | 获取邮件合并数据    |
| `asc_setMailMergeData(aList)`                                          | aList: array                                                                 | void   | 设置邮件合并数据    |
| `asc_sendMailMergeData(oData)`                                         | oData: object                                                                | void   | 发送邮件合并数据    |
| `asc_GetMailMergeFiledValue(nIndex, sName)`                            | nIndex: number, sName: string                                                | string | 获取邮件合并字段值   |
| `asc_DownloadAsMailMerge(typeFile, StartIndex, EndIndex, bIsDownload)` | typeFile: number, StartIndex: number, EndIndex: number, bIsDownload: boolean | void   | 下载邮件合并结果    |

#### 数学公式

| 方法                                       | 参数                                  | 返回值  | 说明         |
| ---------------------------------------- | ----------------------------------- | ---- | ---------- |
| `asc_AddMath(Type)`                      | Type: number                        | void | 添加数学公式     |
| `asc_AddMath2(nType)`                    | nType: number                       | void | 添加数学公式(扩展) |
| `asc_ConvertMathView(isToLinear, isAll)` | isToLinear: boolean, isAll: boolean | void | 转换数学公式视图   |
| `asc_SetMathProps(MathProps)`            | MathProps: object                   | void | 设置数学公式属性   |

#### 视图设置

| 方法                               | 参数                  | 返回值     | 说明          |
| -------------------------------- | ------------------- | ------- | ----------- |
| `asc_SetViewRulers(bRulers)`     | bRulers: boolean    | void    | 设置显示标尺      |
| `asc_GetViewRulers()`            | 无                   | boolean | 获取是否显示标尺    |
| `asc_SetViewRulersChange()`      | 无                   | void    | 标尺视图改变      |
| `asc_SetDocumentUnits(_units)`   | \_units: number     | void    | 设置文档单位      |
| `put_ShowSnapLines(isShow)`      | isShow: boolean     | void    | 设置显示对齐线     |
| `get_ShowSnapLines()`            | 无                   | boolean | 获取是否显示对齐线   |
| `put_ShowSmartGuides(isShow)`    | isShow: boolean     | void    | 设置显示智能参考线   |
| `get_ShowSmartGuides()`          | 无                   | boolean | 获取是否显示智能参考线 |
| `put_ShowParaMarks(isShow)`      | isShow: boolean     | void    | 设置显示段落标记    |
| `get_ShowParaMarks()`            | 无                   | boolean | 获取是否显示段落标记  |
| `put_ShowTableEmptyLine(isShow)` | isShow: boolean     | void    | 设置显示表格空行    |
| `get_ShowTableEmptyLine()`       | 无                   | boolean | 获取是否显示表格空行  |
| `asc_setViewMode(isViewMode)`    | isViewMode: boolean | void    | 设置视图模式      |
| `ChangeReaderMode()`             | 无                   | void    | 切换阅读模式      |
| `SetReaderModeOnly()`            | 无                   | void    | 仅阅读模式       |
| `IncreaseReaderFontSize()`       | 无                   | void    | 增大阅读字体      |
| `DecreaseReaderFontSize()`       | 无                   | void    | 减小阅读字体      |

#### 签名

| 方法                                                  | 参数                                                          | 返回值   | 说明       |
| --------------------------------------------------- | ----------------------------------------------------------- | ----- | -------- |
| `asc_addSignatureLine(oPr, Width, Height, sImgUrl)` | oPr: object, Width: number, Height: number, sImgUrl: string | void  | 添加签名行    |
| `asc_getAllSignatures()`                            | 无                                                           | array | 获取所有签名   |
| `asc_CallSignatureDblClickEvent(sGuid)`             | sGuid: string                                               | void  | 调用签名双击事件 |
| `asc_SendForm()`                                    | 无                                                           | void  | 发送表单     |

#### 协作

| 方法                                     | 参数             | 返回值    | 说明         |
| -------------------------------------- | -------------- | ------ | ---------- |
| `asc_SetFastCollaborative(isOn)`       | isOn: boolean  | void   | 设置快速协作模式   |
| `SetCollaborativeMarksShowType(Type)`  | Type: number   | void   | 设置协作标记显示类型 |
| `GetCollaborativeMarksShowType()`      | 无              | number | 获取协作标记显示类型 |
| `Clear_CollaborativeMarks()`           | 无              | void   | 清除协作标记     |
| `asc_setDrawCollaborationMarks(bDraw)` | bDraw: boolean | void   | 设置绘制协作标记   |

#### 文档大纲

| 方法                                | 参数 | 返回值    | 说明        |
| --------------------------------- | -- | ------ | --------- |
| `asc_GetDocumentOutlineManager()` | 无  | object | 获取文档大纲管理器 |
| `asc_ShowDocumentOutline()`       | 无  | void   | 显示文档大纲    |
| `asc_HideDocumentOutline()`       | 无  | void   | 隐藏文档大纲    |

#### 剪贴板

| 方法                                                                                       | 参数                                    | 返回值     | 说明       |
| ---------------------------------------------------------------------------------------- | ------------------------------------- | ------- | -------- |
| `asc_CheckCopy(_clipboard, _formats)`                                                    | \_clipboard: object, \_formats: array | boolean | 检查复制     |
| `asc_SelectionCut()`                                                                     | 无                                     | void    | 剪切选择     |
| `asc_PasteData(_format, data1, data2, text_data, useCurrentPoint, callback, checkLocks)` | ...                                   | void    | 粘贴数据     |
| `asc_SpecialPaste(props)`                                                                | props: object                         | void    | 特殊粘贴     |
| `asc_SpecialPasteData(props)`                                                            | props: object                         | void    | 特殊粘贴数据   |
| `asc_specialPasteShowButton()`                                                           | 无                                     | void    | 显示特殊粘贴按钮 |
| `asc_ShowSpecialPasteButton(props)`                                                      | props: object                         | void    | 显示特殊粘贴按钮 |
| `asc_HideSpecialPasteButton()`                                                           | 无                                     | void    | 隐藏特殊粘贴按钮 |
| `asc_UpdateSpecialPasteButton()`                                                         | 无                                     | void    | 更新特殊粘贴按钮 |
| `asc_canPaste()`                                                                         | 无                                     | boolean | 是否可以粘贴   |

#### 回调注册

| 方法                                       | 参数                               | 返回值     | 说明       |
| ---------------------------------------- | -------------------------------- | ------- | -------- |
| `asc_registerCallback(name, callback)`   | name: string, callback: function | void    | 注册回调函数   |
| `asc_unregisterCallback(name, callback)` | name: string, callback: function | void    | 注销回调函数   |
| `asc_checkNeedCallback(name)`            | name: string                     | boolean | 检查是否需要回调 |

***

## 属性类

### CAddTextSettings

插入文本设置类，用于 `asc_AddText` 方法的参数。

```javascript
var settings = new AscCommon.CAddTextSettings();
settings.SetTextPr(oTextPr);           // 设置文本属性
settings.MoveCursorOutside(true);      // 插入后光标移到文本外部
settings.SetWrapWithSpaces(true);      // 用空格包裹文本
```

**属性：**

| 属性            | 类型       | 说明                        |
| ------------- | -------- | ------------------------- |
| `TextPr`      | object   | 文本属性（字体、颜色等）              |
| `CursorOutside` | boolean | 插入后光标是否移到文本外部（与 TextPr 配合） |
| `WrapSpaces`  | boolean  | 是否用空格包裹文本                 |

**方法：**

| 方法                              | 参数                    | 返回值     | 说明            |
| ------------------------------- | --------------------- | ------- | ------------- |
| `SetTextPr(oTextPr)`            | oTextPr: object       | void    | 设置文本属性        |
| `GetTextPr()`                   | 无                     | object  | 获取文本属性        |
| `MoveCursorOutside(isOutside)`  | isOutside: boolean    | void    | 设置光标是否移到文本外部  |
| `IsMoveCursorOutside()`         | 无                     | boolean | 获取光标是否移到文本外部  |
| `SetWrapWithSpaces(isWrap)`     | isWrap: boolean       | void    | 设置是否用空格包裹文本   |
| `IsWrapWithSpaces()`            | 无                     | boolean | 获取是否用空格包裹文本   |
| `put_WrapWithSpaces(isWrap)`    | isWrap: boolean       | void    | 设置是否用空格包裹文本（别名） |

### asc\_CColor

颜色类，用于表示RGB颜色。

```javascript
var color = new Asc.asc_CColor();
color.r = 255;      // 红色分量 (0-255)
color.g = 0;        // 绿色分量 (0-255)
color.b = 0;        // 蓝色分量 (0-255)
color.a = 255;      // 透明度 (0-255)
color.Auto = false; // 是否自动颜色
```

**方法：**

| 方法                | 返回值     | 说明        |
| ----------------- | ------- | --------- |
| `asc_getR()`      | number  | 获取红色分量    |
| `asc_putR(v)`     | void    | 设置红色分量    |
| `asc_getG()`      | number  | 获取绿色分量    |
| `asc_putG(v)`     | void    | 设置绿色分量    |
| `asc_getB()`      | number  | 获取蓝色分量    |
| `asc_putB(v)`     | void    | 设置蓝色分量    |
| `asc_getA()`      | number  | 获取透明度     |
| `asc_putA(v)`     | void    | 设置透明度     |
| `asc_getType()`   | number  | 获取颜色类型    |
| `asc_putType(v)`  | void    | 设置颜色类型    |
| `asc_getValue()`  | number  | 获取颜色值     |
| `asc_putValue(v)` | void    | 设置颜色值     |
| `asc_getHex()`    | string  | 获取十六进制颜色值 |
| `asc_getAuto()`   | boolean | 获取是否自动颜色  |
| `asc_putAuto(v)`  | void    | 设置是否自动颜色  |

### asc\_CParagraphProperty

段落属性类。

**属性：**

| 属性                  | 类型                     | 说明           |
| ------------------- | ---------------------- | ------------ |
| `ContextualSpacing` | boolean                | 删除相同样式段落间的间距 |
| `Ind`               | asc\_CParagraphInd     | 缩进属性         |
| `KeepLines`         | boolean                | 段中不分页        |
| `KeepNext`          | boolean                | 与下段同页        |
| `WidowControl`      | boolean                | 孤行控制         |
| `PageBreakBefore`   | boolean                | 段前分页         |
| `Spacing`           | asc\_CParagraphSpacing | 间距属性         |
| `Brd`               | asc\_CParagraphBorders | 边框属性         |
| `Shd`               | asc\_CParagraphShd     | 底纹属性         |
| `Tabs`              | asc\_CParagraphTabs    | 制表符属性        |
| `Jc`                | number                 | 对齐方式         |
| `Locked`            | boolean                | 是否锁定         |
| `Subscript`         | boolean                | 下标           |
| `Superscript`       | boolean                | 上标           |
| `SmallCaps`         | boolean                | 小型大写         |
| `AllCaps`           | boolean                | 全部大写         |
| `Strikeout`         | boolean                | 删除线          |
| `DStrikeout`        | boolean                | 双删除线         |
| `TextSpacing`       | number                 | 字符间距         |
| `Position`          | number                 | 文字位置         |
| `OutlineLvl`        | number                 | 大纲级别         |

**方法：**

| 方法                            | 返回值                    | 说明      |
| ----------------------------- | ---------------------- | ------- |
| `asc_getContextualSpacing()`  | boolean                | 获取上下文间距 |
| `asc_putContextualSpacing(v)` | void                   | 设置上下文间距 |
| `asc_getInd()`                | asc\_CParagraphInd     | 获取缩进    |
| `asc_putInd(v)`               | void                   | 设置缩进    |
| `asc_getJc()`                 | number                 | 获取对齐方式  |
| `asc_putJc(v)`                | void                   | 设置对齐方式  |
| `asc_getKeepLines()`          | boolean                | 获取段中不分页 |
| `asc_putKeepLines(v)`         | void                   | 设置段中不分页 |
| `asc_getKeepNext()`           | boolean                | 获取与下段同页 |
| `asc_putKeepNext(v)`          | void                   | 设置与下段同页 |
| `asc_getPageBreakBefore()`    | boolean                | 获取段前分页  |
| `asc_putPageBreakBefore(v)`   | void                   | 设置段前分页  |
| `asc_getWidowControl()`       | boolean                | 获取孤行控制  |
| `asc_putWidowControl(v)`      | void                   | 设置孤行控制  |
| `asc_getSpacing()`            | asc\_CParagraphSpacing | 获取间距    |
| `asc_putSpacing(v)`           | void                   | 设置间距    |
| `asc_getBorders()`            | asc\_CParagraphBorders | 获取边框    |
| `asc_putBorders(v)`           | void                   | 设置边框    |
| `asc_getShade()`              | asc\_CParagraphShd     | 获取底纹    |
| `asc_putShade(v)`             | void                   | 设置底纹    |
| `asc_getLocked()`             | boolean                | 获取锁定状态  |
| `asc_getTabs()`               | asc\_CParagraphTabs    | 获取制表符   |
| `asc_putTabs(v)`              | void                   | 设置制表符   |

### asc\_CParagraphInd

段落缩进属性类。

**属性：**

| 属性          | 类型     | 说明        |
| ----------- | ------ | --------- |
| `Left`      | number | 左缩进 (mm)  |
| `Right`     | number | 右缩进 (mm)  |
| `FirstLine` | number | 首行缩进 (mm) |

### asc\_CParagraphSpacing

段落间距属性类。

**属性：**

| 属性         | 类型     | 说明        |
| ---------- | ------ | --------- |
| `Line`     | number | 行距值       |
| `LineRule` | number | 行距规则      |
| `Before`   | number | 段前间距 (pt) |
| `After`    | number | 段后间距 (pt) |

### asc\_CParagraphBorders

段落边框属性类。

**属性：**

| 属性        | 类型               | 说明   |
| --------- | ---------------- | ---- |
| `Top`     | asc\_CTextBorder | 上边框  |
| `Bottom`  | asc\_CTextBorder | 下边框  |
| `Left`    | asc\_CTextBorder | 左边框  |
| `Right`   | asc\_CTextBorder | 右边框  |
| `Between` | asc\_CTextBorder | 中间边框 |

### asc\_CTextBorder

文本边框属性类。

**属性：**

| 属性      | 类型          | 说明        |
| ------- | ----------- | --------- |
| `Color` | asc\_CColor | 边框颜色      |
| `Size`  | number      | 边框宽度 (mm) |
| `Value` | number      | 边框样式      |
| `Space` | number      | 边框距离 (pt) |

### asc\_CParagraphShd

段落底纹属性类。

**属性：**

| 属性      | 类型          | 说明   |
| ------- | ----------- | ---- |
| `Value` | number      | 底纹类型 |
| `Color` | asc\_CColor | 底纹颜色 |
| `Fill`  | asc\_CColor | 填充颜色 |

### asc\_CParagraphTab

制表符属性类。

**属性：**

| 属性       | 类型     | 说明    |
| -------- | ------ | ----- |
| `Pos`    | number | 制表符位置 |
| `Value`  | number | 制表符类型 |
| `Leader` | number | 前导符   |

### asc\_CParagraphTabs

制表符集合类。

### asc\_CPaddings

内边距属性类。

**属性：**

| 属性       | 类型     | 说明   |
| -------- | ------ | ---- |
| `Left`   | number | 左内边距 |
| `Top`    | number | 上内边距 |
| `Right`  | number | 右内边距 |
| `Bottom` | number | 下内边距 |

### CTableProp

表格属性类。

**属性：**

| 属性                    | 类型             | 说明      |
| --------------------- | -------------- | ------- |
| `TableWidth`          | number         | 表格宽度    |
| `TableSpacing`        | number         | 表格间距    |
| `TableDefaultMargins` | asc\_CPaddings | 默认单元格边距 |
| `CellMargins`         | CMargins       | 单元格边距   |
| `TableAlignment`      | number         | 表格对齐方式  |
| `TableIndent`         | number         | 表格缩进    |
| `TableWrappingStyle`  | number         | 表格环绕样式  |
| `TablePaddings`       | asc\_CPaddings | 表格内边距   |
| `TableBorders`        | CBorders       | 表格边框    |
| `CellBorders`         | CBorders       | 单元格边框   |
| `TableBackground`     | CBackground    | 表格背景    |
| `CellsBackground`     | CBackground    | 单元格背景   |
| `Position`            | CPosition      | 表格位置    |
| `TableStyle`          | string         | 表格样式    |
| `TableLook`           | CTableLook     | 表格外观    |
| `RowsInHeader`        | number         | 标题行数    |
| `CellsVAlign`         | number         | 单元格垂直对齐 |
| `TableLayout`         | number         | 表格布局    |
| `Locked`              | boolean        | 是否锁定    |

### CBackground

背景属性类。

**属性：**

| 属性      | 类型          | 说明   |
| ------- | ----------- | ---- |
| `Value` | number      | 背景类型 |
| `Color` | asc\_CColor | 背景颜色 |

### CAscSection

节属性类。

**属性：**

| 属性             | 类型     | 说明   |
| -------------- | ------ | ---- |
| `PageWidth`    | number | 页面宽度 |
| `PageHeight`   | number | 页面高度 |
| `MarginLeft`   | number | 左边距  |
| `MarginRight`  | number | 右边距  |
| `MarginTop`    | number | 上边距  |
| `MarginBottom` | number | 下边距  |

### CHeaderProp

页眉页脚属性类。

**属性：**

| 属性                 | 类型      | 说明        |
| ------------------ | ------- | --------- |
| `Type`             | number  | 类型(页眉/页脚) |
| `Position`         | number  | 位置        |
| `DifferentFirst`   | boolean | 首页不同      |
| `DifferentEvenOdd` | boolean | 奇偶页不同     |
| `LinkToPrevious`   | boolean | 链接到前一节    |
| `Locked`           | boolean | 是否锁定      |
| `StartPageNumber`  | number  | 起始页码      |

### asc\_CShapeProperty

形状属性类。

### asc\_CImgProperty

图片属性类。

### asc\_CStroke

线条属性类。

### asc\_CShapeFill

填充属性类。

### asc\_CFillSolid

纯色填充类。

### asc\_CFillGrad

渐变填充类。

### asc\_CFillBlip

图片填充类。

### asc\_CFillHatch

图案填充类。

***

## 枚举常量

### c\_oAscAlignType

对齐类型。

| 值 | 名称      | 说明   |
| - | ------- | ---- |
| 0 | LEFT    | 左对齐  |
| 1 | CENTER  | 居中对齐 |
| 2 | RIGHT   | 右对齐  |
| 3 | JUSTIFY | 两端对齐 |
| 4 | TOP     | 顶部对齐 |
| 5 | MIDDLE  | 垂直居中 |
| 6 | BOTTOM  | 底部对齐 |

### c\_oAscWrapStyle2

文字环绕样式。

| 值 | 名称           | 说明     |
| - | ------------ | ------ |
| 0 | Inline       | 嵌入型    |
| 1 | Square       | 四周型    |
| 2 | Tight        | 紧密型    |
| 3 | Through      | 穿越型    |
| 4 | TopAndBottom | 上下型    |
| 5 | Behind       | 衬于文字下方 |
| 6 | InFront      | 浮于文字上方 |

### c\_oAscVertAlignJc

垂直对齐方式。

| 值 | 名称     | 说明   |
| - | ------ | ---- |
| 0 | Top    | 顶端对齐 |
| 1 | Center | 居中对齐 |
| 2 | Bottom | 底端对齐 |

### c\_oAscTableLayout

表格布局。

| 值 | 名称      | 说明   |
| - | ------- | ---- |
| 0 | AutoFit | 自动适应 |
| 1 | Fixed   | 固定宽度 |

### c\_oAscChangeLevel

图层顺序更改。

| 值 | 名称            | 说明   |
| - | ------------- | ---- |
| 0 | BringToFront  | 置于顶层 |
| 1 | BringForward  | 上移一层 |
| 2 | SendToBack    | 置于底层 |
| 3 | BringBackward | 下移一层 |

### c\_oAscZoomType

缩放类型。

| 值 | 名称       | 说明   |
| - | -------- | ---- |
| 0 | Current  | 当前缩放 |
| 1 | FitWidth | 适应宽度 |
| 2 | FitPage  | 适应页面 |

### c\_oAscTableSelectionType

表格选择类型。

| 值 | 名称     | 说明   |
| - | ------ | ---- |
| 0 | Cell   | 单元格  |
| 1 | Row    | 行    |
| 2 | Column | 列    |
| 3 | Table  | 整个表格 |

### c\_oAscCollaborativeMarksShowType

协作标记显示类型。

| 值  | 名称          | 说明      |
| -- | ----------- | ------- |
| -1 | None        | 不显示     |
| 0  | All         | 显示所有    |
| 1  | LastChanges | 仅显示最后更改 |

### c\_oAscSdtLevelType

内容控件级别类型。

| 值 | 名称     | 说明  |
| - | ------ | --- |
| 1 | Block  | 块级  |
| 2 | Inline | 行内  |
| 3 | Row    | 行   |
| 4 | Cell   | 单元格 |

### c\_oAscStyleType

样式类型。

| 值 | 名称        | 说明   |
| - | --------- | ---- |
| 1 | Paragraph | 段落样式 |
| 2 | Numbering | 编号样式 |
| 3 | Table     | 表格样式 |
| 4 | Character | 字符样式 |

### c\_oAscTOCStylesType

目录样式类型。

| 值 | 名称       | 说明  |
| - | -------- | --- |
| 0 | Current  | 当前  |
| 1 | Simple   | 简单  |
| 2 | Standard | 标准  |
| 3 | Modern   | 现代  |
| 4 | Classic  | 经典  |
| 5 | Web      | Web |

### c\_oAscFootnotePos

脚注位置。

| 值 | 名称          | 说明   |
| - | ----------- | ---- |
| 0 | BeneathText | 文字下方 |
| 1 | DocEnd      | 文档末尾 |
| 2 | PageBottom  | 页面底部 |
| 3 | SectEnd     | 节末尾  |

### c\_oAscFootnoteRestart

脚注重新编号。

| 值 | 名称         | 说明 |
| - | ---------- | -- |
| 0 | Continuous | 连续 |
| 1 | EachSect   | 每节 |
| 2 | EachPage   | 每页 |

### c\_oAscDocumentShortcutType

文档快捷键类型。

| 值  | 名称                   | 说明        |
| -- | -------------------- | --------- |
| 1  | InsertPageBreak      | 插入分页符     |
| 2  | InsertLineBreak      | 插入换行符     |
| 3  | InsertColumnBreak    | 插入分栏符     |
| 4  | ResetChar            | 重置字符      |
| 5  | NonBreakingSpace     | 不间断空格     |
| 6  | ApplyHeading1        | 应用标题1     |
| 7  | ApplyHeading2        | 应用标题2     |
| 8  | ApplyHeading3        | 应用标题3     |
| 9  | Strikeout            | 删除线       |
| 10 | ShowAll              | 显示/隐藏编辑标记 |
| 11 | EditSelectAll        | 全选        |
| 12 | Bold                 | 粗体        |
| 13 | CopyFormat           | 复制格式      |
| 14 | CopyrightSign        | 版权符号      |
| 15 | InsertEndnoteNow     | 插入尾注      |
| 16 | CenterPara           | 居中对齐      |
| 17 | EuroSign             | 欧元符号      |
| 18 | InsertFootnoteNow    | 插入脚注      |
| 19 | Italic               | 斜体        |
| 20 | JustifyPara          | 两端对齐      |
| 21 | InsertHyperlink      | 插入超链接     |
| 22 | ApplyListBullet      | 应用项目符号    |
| 23 | LeftPara             | 左对齐       |
| 24 | Indent               | 增加缩进      |
| 25 | UnIndent             | 减少缩进      |
| 26 | PrintPreviewAndPrint | 打印预览      |
| 27 | InsertPageNumber     | 插入页码      |
| 28 | RegisteredSign       | 注册符号      |
| 29 | RightPara            | 右对齐       |
| 30 | Save                 | 保存        |
| 31 | TrademarkSign        | 商标符号      |
| 32 | Underline            | 下划线       |
| 33 | PasteFormat          | 粘贴格式      |
| 34 | EditUndo             | 撤销        |
| 35 | EditRedo             | 重做        |
| 36 | EmDash               | 长破折号      |
| 37 | EnDash               | 短破折号      |
| 38 | UpdateFields         | 更新域       |
| 39 | InsertEquation       | 插入公式      |
| 40 | Superscript          | 上标        |
| 41 | NonBreakingHyphen    | 不间断连字符    |
| 42 | SoftHyphen           | 软连字符      |
| 43 | HorizontalEllipsis   | 省略号       |
| 44 | Subscript            | 下标        |
| 45 | IncreaseFontSize     | 增大字号      |
| 46 | DecreaseFontSize     | 减小字号      |

### c\_oAscEDocProtect

文档保护类型。

| 值 | 名称             | 说明      |
| - | -------------- | ------- |
| 0 | Comments       | 仅允许批注   |
| 1 | Forms          | 仅允许填写表单 |
| 2 | None           | 无保护     |
| 3 | ReadOnly       | 只读      |
| 4 | TrackedChanges | 仅允许修订   |

### c\_oAscFileType

文件类型。

| 值   | 名称   | 说明       |
| --- | ---- | -------- |
| 0   | DOCT | DOCT模板   |
| 1   | DOCX | DOCX文档   |
| 2   | XLSX | XLSX电子表格 |
| 3   | PPTX | PPTX演示文稿 |
| 4   | PDF  | PDF文档    |
| ... | ...  | ...      |

### c\_oAscPageOrientation

页面方向。

| 值 | 名称        | 说明 |
| - | --------- | -- |
| 0 | Portrait  | 纵向 |
| 1 | Landscape | 横向 |

### c\_oAscBorderStyles

边框样式。

| 值 | 名称         | 说明   |
| - | ---------- | ---- |
| 0 | None       | 无边框  |
| 1 | Single     | 单线   |
| 2 | Dotted     | 点线   |
| 3 | Dashed     | 虚线   |
| 4 | DashDot    | 点划线  |
| 5 | DashDotDot | 双点划线 |
| 6 | Double     | 双线   |

### c\_oAscTabType

制表符类型。

| 值 | 名称      | 说明    |
| - | ------- | ----- |
| 0 | Left    | 左对齐   |
| 1 | Center  | 居中对齐  |
| 2 | Right   | 右对齐   |
| 3 | Decimal | 小数点对齐 |

### c\_oAscTabLeader

制表符前导符。

| 值 | 名称         | 说明  |
| - | ---------- | --- |
| 0 | None       | 无   |
| 1 | Dot        | 点   |
| 2 | Hyphen     | 短划线 |
| 3 | Underscore | 下划线 |

***

## 回调事件

通过 `asc_registerCallback` 方法注册的事件回调。

### 文档事件

| 事件名                             | 参数                            | 说明        |
| ------------------------------- | ----------------------------- | --------- |
| `asc_onDocumentModifiedChanged` | 无                             | 文档修改状态改变  |
| `asc_onDocumentCanSaveChanged`  | canSave: boolean              | 文档可保存状态改变 |
| `asc_onCountPages`              | count: number                 | 页数改变      |
| `asc_onCurrentPage`             | page: number                  | 当前页改变     |
| `asc_onZoom`                    | zoom: number                  | 缩放改变      |
| `asc_onDocSize`                 | width: number, height: number | 文档尺寸改变    |
| `asc_onPageOrient`              | isPortrait: boolean           | 页面方向改变    |

### 编辑事件

| 事件名             | 参数               | 说明      |
| --------------- | ---------------- | ------- |
| `asc_onCanUndo` | canUndo: boolean | 可撤销状态改变 |
| `asc_onCanRedo` | canRedo: boolean | 可重做状态改变 |
| `asc_onUndo`    | 无                | 撤销操作    |
| `asc_onRedo`    | 无                | 重做操作    |
| `asc_onCopy`    | 无                | 复制操作    |
| `asc_onCut`     | 无                | 剪切操作    |
| `asc_onPaste`   | 无                | 粘贴操作    |

### 文本格式事件

| 事件名                    | 参数                         | 说明       |
| ---------------------- | -------------------------- | -------- |
| `asc_onBold`           | isBold: boolean            | 粗体状态改变   |
| `asc_onItalic`         | isItalic: boolean          | 斜体状态改变   |
| `asc_onUnderline`      | isUnderline: boolean       | 下划线状态改变  |
| `asc_onStrikeout`      | isStrikeout: boolean       | 删除线状态改变  |
| `asc_onFontFamily`     | font: asc\_CTextFontFamily | 字体改变     |
| `asc_onFontSize`       | size: number               | 字号改变     |
| `asc_onTextColor`      | color: asc\_CColor         | 文字颜色改变   |
| `asc_onTextHighLight`  | color: asc\_CColor         | 高亮颜色改变   |
| `asc_onTextSpacing`    | spacing: number            | 字符间距改变   |
| `asc_onTextDStrikeout` | value: boolean             | 双删除线状态改变 |
| `asc_onTextCaps`       | value: boolean             | 大写状态改变   |
| `asc_onTextSmallCaps`  | value: boolean             | 小型大写状态改变 |
| `asc_onTextPosition`   | value: number              | 文字位置改变   |
| `asc_onTextLanguage`   | lang: number               | 语言改变     |

### 段落格式事件

| 事件名                     | 参数                              | 说明        |
| ----------------------- | ------------------------------- | --------- |
| `asc_onPrAlign`         | align: number                   | 段落对齐改变    |
| `asc_onVerticalAlign`   | align: number                   | 垂直对齐改变    |
| `asc_onLineSpacing`     | spacing: asc\_CParagraphInd     | 行距改变      |
| `asc_onParaSpacingLine` | spacing: asc\_CParagraphSpacing | 段落间距改变    |
| `asc_onParaStyleName`   | name: string                    | 段落样式改变    |
| `asc_onPageBreak`       | isBreak: boolean                | 分页符状态改变   |
| `asc_onWidowControl`    | value: boolean                  | 孤行控制状态改变  |
| `asc_onKeepNext`        | value: boolean                  | 与下段同页状态改变 |
| `asc_onKeepLines`       | value: boolean                  | 段中不分页状态改变 |
| `asc_onShowParaMarks`   | 无                               | 显示段落标记    |
| `asc_onSpaceBetweenPrg` | 无                               | 段落间距设置    |
| `asc_onTextShd`         | shd: asc\_CParagraphShd         | 文本底纹改变    |

### 表格事件

| 事件名                        | 参数            | 说明      |
| -------------------------- | ------------- | ------- |
| `asc_onAddTable`           | 无             | 添加表格    |
| `asc_onAlignCell`          | align: number | 单元格对齐改变 |
| `asc_onInitTableTemplates` | 无             | 初始化表格模板 |

### 样式事件

| 事件名                      | 参数             | 说明       |
| ------------------------ | -------------- | -------- |
| `asc_onInitEditorStyles` | styles: object | 初始化编辑器样式 |

### 搜索事件

| 事件名                             | 参数                                         | 说明       |
| ------------------------------- | ------------------------------------------ | -------- |
| `asc_onReplaceAll`              | overallCount: number, replaceCount: number | 全部替换完成   |
| `asc_onSearchEnd`               | 无                                          | 搜索结束     |
| `asc_onSetSearchCurrent`        | current: number, overallCount: number      | 设置当前搜索结果 |
| `asc_onStartTextAroundSearch`   | 无                                          | 开始搜索上下文  |
| `asc_onEndTextAroundSearch`     | 无                                          | 结束搜索上下文  |
| `asc_onGetTextAroundSearchPack` | elements: array                            | 获取搜索上下文包 |
| `asc_onRemoveTextAroundSearch`  | ids: array                                 | 移除搜索上下文  |

### 节/页面事件

| 事件名                      | 参数                 | 说明     |
| ------------------------ | ------------------ | ------ |
| `asc_onSectionProps`     | props: CAscSection | 节属性改变  |
| `asc_onColumnsProps`     | props: object      | 分栏属性改变 |
| `asc_onLineNumbersProps` | props: object      | 行号属性改变 |

### 页眉页脚事件

| 事件名                        | 参数                                | 说明     |
| -------------------------- | --------------------------------- | ------ |
| `asc_onChangeActiveHeader` | position: number, header: CHeader | 活动页眉改变 |
| `asc_onReturnHeaders`      | headers: array                    | 返回页眉列表 |

### 协作事件

| 事件名                            | 参数                | 说明       |
| ------------------------------ | ----------------- | -------- |
| `asc_onConnectionStateChanged` | e: object         | 连接状态改变   |
| `asc_onLockCore`               | isLocked: boolean | 核心锁定状态   |
| `asc_onLockDocumentProtection` | isLocked: boolean | 文档保护锁定状态 |

### 错误事件

| 事件名           | 参数                                  | 说明   |
| ------------- | ----------------------------------- | ---- |
| `asc_onError` | errorId: number, errorLevel: number | 发生错误 |

### 其他事件

| 事件名                                | 参数                                  | 说明       |
| ---------------------------------- | ----------------------------------- | -------- |
| `asc_onFocusObject`                | objects: array, isExternal: boolean | 焦点对象改变   |
| `asc_onClearPropObj`               | prop: object                        | 清除属性对象   |
| `asc_onHyperlinkClick`             | url: string                         | 超链接点击    |
| `asc_onSave`                       | 无                                   | 保存操作     |
| `asc_onDownload`                   | 无                                   | 下载操作     |
| `asc_onShare`                      | 无                                   | 分享操作     |
| `asc_onAddURL`                     | 无                                   | 添加URL    |
| `asc_onHelp`                       | url: string                         | 帮助       |
| `asc_onCursorLock`                 | isLock: boolean                     | 光标锁定状态   |
| `asc_onAdvancedOptions`            | idOption: number                    | 高级选项     |
| `asc_onViewerBookmarksUpdate`      | structure: object                   | 查看器书签更新  |
| `asc_onViewerThumbnailsZoomUpdate` | value: number                       | 缩略图缩放更新  |
| `asc_onDocInfo`                    | info: CDocInfoProp                  | 文档信息     |
| `asc_onGetDocInfoStart`            | 无                                   | 开始获取文档信息 |
| `asc_onGetDocInfoStop`             | 无                                   | 停止获取文档信息 |
| `asc_onGetDocInfoEnd`              | 无                                   | 结束获取文档信息 |
| `asc_onAddSignature`               | id: string                          | 添加签名     |
| `asc_onShowSpecialPasteOptions`    | props: object                       | 显示特殊粘贴选项 |
| `asc_onHideSpecialPasteOptions`    | 无                                   | 隐藏特殊粘贴选项 |
| `asc_onEndAddShape`                | 无                                   | 结束添加形状   |

***

## 使用示例

### 初始化编辑器

```javascript
// 创建API实例
var api = new Asc.asc_docs_api({
  // 配置选项
});

// 初始化
api.Init();

// 注册回调
api.asc_registerCallback('asc_onDocumentModifiedChanged', function() {
  console.log('文档已修改');
});

api.asc_registerCallback('asc_onCountPages', function(count) {
  console.log('总页数:', count);
});
```

### 插入文本

```javascript
// 简单插入文本
api.asc_AddText('Hello World');

// 带格式插入文本
var settings = new AscCommon.CAddTextSettings();
settings.SetTextPr({
  Bold: true,
  Italic: true,
  FontSize: 16
});
settings.MoveCursorOutside(true);  // 插入后光标移到文本外部
api.asc_AddText('带格式的文本', settings);

// 获取选中的文本
var selectedText = api.asc_GetSelectedText();
console.log('选中的文本:', selectedText);

// 全选文档
api.asc_EditSelectAll();

// 移除选择
api.asc_RemoveSelection();

// 获取当前单词
var currentWord = api.asc_GetCurrentWord(0);
console.log('当前单词:', currentWord);

// 替换当前单词
api.asc_ReplaceCurrentWord(0, '新单词');
```

### 设置文本格式

```javascript
// 设置粗体
api.put_TextPrBold(true);

// 设置字体
api.put_TextPrFontName('Arial');

// 设置字号
api.put_TextPrFontSize(14);

// 设置文字颜色
var color = new Asc.asc_CColor();
color.r = 255;
color.g = 0;
color.b = 0;
api.put_TextColor(color);
```

### 设置段落格式

```javascript
// 设置对齐方式 (0=左, 1=中, 2=右, 3=两端)
api.put_PrAlign(1);

// 设置行距
api.put_PrLineSpacing(1, 1.5); // 类型, 值

// 设置缩进
api.put_PrIndent(10); // 左缩进 10mm
api.put_PrFirstLineIndent(5); // 首行缩进 5mm
```

### 插入表格

```javascript
// 插入 3x4 表格
api.put_Table(3, 4, 'TableGrid');
```

### 搜索替换

```javascript
// 查找文本
api.asc_findText({
  Text: '搜索内容',
  MatchCase: false,
  WholeWords: false
}, true, function(result) {
  console.log('找到:', result);
});

// 替换文本
api.asc_replaceText({
  Text: '原内容'
}, '新内容', false); // false = 替换第一个, true = 全部替换
```

### 内容控件

```javascript
// 添加内容控件
api.asc_AddContentControl(Asc.c_oAscSdtLevelType.Block, {
  Tag: 'myTag',
  Alias: '我的控件',
  Lock: Asc.c_oAscSdtLockType.Unlocked
});

// 设置内容控件文本
api.asc_SetContentControlText('内容文本', 'controlId');
```

### 修订追踪

```javascript
// 开启修订追踪
api.asc_SetTrackRevisions(true);

// 接受所有更改
api.asc_AcceptAllChanges();

// 获取修订报告
var report = api.asc_GetTrackRevisionsReportByAuthors();
```

### 导出文档

```javascript
// 下载为 DOCX
api.asc_DownloadAs(new Asc.asc_CDownloadOptions(Asc.c_oAscFileType.DOCX));

// 下载为 PDF
api.asc_DownloadAs(new Asc.asc_CDownloadOptions(Asc.c_oAscFileType.PDF));
```

***

## 注意事项

1. 所有尺寸单位默认为毫米(mm)，除非另有说明
2. 颜色使用 RGB 值，范围为 0-255
3. 大部分方法需要等待编辑器初始化完成后才能调用
4. 回调函数的注册应在文档加载前完成
5. 部分功能需要服务器端支持

***

*文档版本: 1.0.0*
*基于 SE Office 项目整理*
