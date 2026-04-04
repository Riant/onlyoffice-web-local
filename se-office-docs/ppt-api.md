# SE Office PowerPoint JavaScript API 文档

本文档整理自 SE Office 项目中 ONLYOFFICE PowerPoint 编辑器的 JavaScript API，用于二次开发扩展。

## 目录

- [核心API类](#核心api类)
- [属性类](#属性类)
- [枚举常量](#枚举常量)
- [回调事件](#回调事件)
- [使用示例](#使用示例)

---

## 核心API类

### asc_docs_api (Presentation)

PowerPoint演示文稿编辑器的核心API类，提供演示文稿操作的所有方法。

#### 初始化方法

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_setLocale(val)` | val: number | void | 设置区域设置 |
| `asc_getLocale()` | 无 | number | 获取当前区域设置 |
| `asc_setViewMode(isViewMode)` | isViewMode: boolean | void | 设置视图模式 |

#### 演示文稿操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_DownloadAs(options)` | options: asc_CDownloadOptions | void | 下载文档为指定格式 |
| `asc_Save()` | 无 | void | 保存文档 |
| `asc_isDocumentModified()` | 无 | boolean | 文档是否已修改 |
| `asc_isDocumentCanSave()` | 无 | boolean | 文档是否可保存 |
| `asc_getDocumentName()` | 无 | string | 获取文档名称 |
| `asc_getAppProps()` | 无 | object | 获取应用程序属性 |
| `asc_getCoreProps()` | 无 | object | 获取核心属性 |
| `asc_setCoreProps(oProps)` | oProps: object | void | 设置核心属性 |

#### 幻灯片操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getFirstSlideNumber()` | 无 | number | 获取第一个幻灯片编号 |
| `asc_IsSlideSelected(nIdx)` | nIdx: number | boolean | 指定幻灯片是否选中 |
| `asc_IsFirstSlideSelected()` | 无 | boolean | 第一个幻灯片是否选中 |
| `asc_IsLastSlideSelected()` | 无 | boolean | 最后一个幻灯片是否选中 |
| `asc_moveSelectedSlidesToEnd()` | 无 | void | 移动选中幻灯片到最后 |
| `asc_moveSelectedSlidesToStart()` | 无 | void | 移动选中幻灯片到开头 |
| `asc_moveSlidesNextPos()` | 无 | void | 移动幻灯片到下一位置 |
| `asc_moveSlidesPrevPos()` | 无 | void | 移动幻灯片到上一位置 |
| `asc_HideSlides(isHide)` | isHide: boolean | void | 隐藏幻灯片 |
| `asc_addSlideNumber()` | 无 | void | 添加幻灯片编号 |
| `asc_addDateTime(oPr)` | oPr: object | void | 添加日期时间 |
| `asc_setDefaultDateTimeFormat(aFormat)` | aFormat: array | void | 设置默认日期时间格式 |
| `asc_FitImagesToSlide()` | 无 | void | 图片适应幻灯片 |
| `asc_getCurSlideObjectsNames()` | 无 | array | 获取当前幻灯片对象名称 |
| `asc_AddToLayout()` | 无 | void | 添加到版式 |

#### 幻灯片切换

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_setLoopShow(isLoop)` | isLoop: boolean | void | 设置循环放映 |
| `asc_GoToInternalHyperlink(url)` | url: string | void | 跳转到内部超链接 |

#### 动画操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_AddAnimation(nPresetClass, nPresetId, nPresetSubtype, bReplace, bPreview)` | nPresetClass: number, nPresetId: number, nPresetSubtype: number, bReplace: boolean, bPreview: boolean | void | 添加动画 |
| `asc_SetAnimationProperties(oPr)` | oPr: object | void | 设置动画属性 |
| `asc_StartAnimationPreview()` | 无 | void | 开始动画预览 |
| `asc_StopAnimationPreview()` | 无 | void | 停止动画预览 |
| `asc_canStartAnimationPreview()` | 无 | boolean | 是否可以开始动画预览 |
| `asc_canMoveAnimationEarlier()` | 无 | boolean | 是否可以向前移动动画 |
| `asc_canMoveAnimationLater()` | 无 | boolean | 是否可以向后移动动画 |
| `asc_moveAnimationEarlier()` | 无 | void | 向前移动动画 |
| `asc_moveAnimationLater()` | 无 | void | 向后移动动画 |
| `asc_onShowAnimTab(bShow)` | bShow: boolean | void | 显示/隐藏动画选项卡 |

#### 形状和绘图对象

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getSelectedDrawingObjectsCount()` | 无 | number | 获取选中绘图对象数量 |
| `asc_canEditGeometry()` | 无 | boolean | 是否可以编辑几何形状 |
| `asc_editPointsGeometry()` | 无 | void | 编辑几何形状点 |
| `asc_canEditCrop()` | 无 | boolean | 是否可以裁剪 |
| `asc_startEditCrop()` | 无 | void | 开始裁剪 |
| `asc_endEditCrop()` | 无 | void | 结束裁剪 |
| `asc_cropFit()` | 无 | void | 裁剪适应 |
| `asc_cropFill()` | 无 | void | 裁剪填充 |

#### 图表操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getChartObject(type)` | type: number | object | 获取图表对象 |
| `asc_addChartDrawingObject(chartBinary, Placeholder)` | chartBinary: object, Placeholder: object | void | 添加图表 |
| `asc_editChartDrawingObject(chartBinary)` | chartBinary: object | void | 编辑图表 |
| `asc_onCloseChartFrame()` | 无 | void | 关闭图表框架 |

#### 图片操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_addImage(urls)` | urls: array | void | 添加图片 |

#### OLE对象

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_addOleObjectAction(sLocalUrl, Data, sApplicationId, fWidth, fHeight, nWidthPix, nHeightPix, bSelect, arrImagesForAddToHistory)` | ... | void | 添加OLE对象 |
| `asc_editOleObjectAction(oOleObject, sImageUrl, sData, fWidth, fHeight, nPixWidth, nPixHeight, arrImagesForAddToHistory)` | ... | void | 编辑OLE对象 |
| `asc_startEditCurrentOleObject()` | 无 | void | 开始编辑当前OLE对象 |
| `asc_doubleClickOnTableOleObject(obj)` | obj: object | void | 双击表格OLE对象 |

#### 签名

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_addSignatureLine(oPr, Width, Height, sImgUrl)` | oPr: object, Width: number, Height: number, sImgUrl: string | void | 添加签名行 |
| `asc_getAllSignatures()` | 无 | array | 获取所有签名 |
| `asc_CallSignatureDblClickEvent(sGuid)` | sGuid: string | void | 调用签名双击事件 |

#### 注释

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_addComment(oComment)` | oComment: object | void | 添加注释 |
| `asc_changeComment(id, oComment)` | id: string, oComment: object | void | 修改注释 |
| `asc_removeComment(id)` | id: string | void | 删除注释 |
| `asc_RemoveAllComments(isMine, isCurrent)` | isMine: boolean, isCurrent: boolean | void | 删除所有注释 |
| `asc_ResolveAllComments(isMine, isCurrent, arrIds)` | isMine: boolean, isCurrent: boolean, arrIds: array | void | 解决所有注释 |
| `asc_selectComment(id)` | id: string | void | 选择注释 |
| `asc_showComment(id)` | id: string | void | 显示注释 |
| `asc_showComments(isShowSolved)` | isShowSolved: boolean | void | 显示注释 |
| `asc_hideComments()` | 无 | void | 隐藏注释 |
| `asc_getMasterCommentId(id)` | id: string | string | 获取主注释ID |
| `asc_GetCommentLogicPosition(sId)` | sId: string | object | 获取注释逻辑位置 |
| `asc_getAnchorPosition()` | 无 | object | 获取锚点位置 |

#### 查找替换

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_findText(oProps, isNext, callback)` | oProps: object, isNext: boolean, callback: function | void | 查找文本 |
| `asc_replaceText(oProps, replaceWith, isReplaceAll)` | oProps: object, replaceWith: string, isReplaceAll: boolean | void | 替换文本 |
| `asc_endFindText()` | 无 | void | 结束查找 |
| `asc_StartTextAroundSearch()` | 无 | void | 开始搜索上下文 |
| `asc_SelectSearchElement(sId)` | sId: string | void | 选择搜索元素 |

#### 拼写检查

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_replaceMisspelledWord(Word, SpellCheckProperty)` | Word: string, SpellCheckProperty: object | void | 替换拼写错误单词 |
| `asc_ignoreMisspelledWord(SpellCheckProperty, bAll)` | SpellCheckProperty: object, bAll: boolean | void | 忽略拼写错误单词 |
| `asc_spellCheckClearDictionary()` | 无 | void | 清除拼写检查字典 |
| `asc_setDefaultLanguage(Lang)` | Lang: number | void | 设置默认语言 |
| `asc_getDefaultLanguage()` | 无 | number | 获取默认语言 |
| `asc_getKeyboardLanguage()` | 无 | number | 获取键盘语言 |
| `asc_setSpellCheck(isOn)` | isOn: boolean | void | 开启/关闭拼写检查 |
| `asc_restartCheckSpelling()` | 无 | void | 重新开始拼写检查 |
| `asc_setSpellCheckSettings(oSettings)` | oSettings: object | void | 设置拼写检查设置 |
| `asc_getSpellCheckSettings()` | 无 | object | 获取拼写检查设置 |

#### 视图设置

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_setShowSmartGuides(isShow)` | isShow: boolean | void | 设置显示智能参考线 |
| `asc_getShowSmartGuides()` | 无 | boolean | 获取是否显示智能参考线 |
| `asc_setShowGuides(isShow)` | isShow: boolean | void | 设置显示参考线 |
| `asc_getShowGuides()` | 无 | boolean | 获取是否显示参考线 |
| `asc_getGuidesCount()` | 无 | number | 获取参考线数量 |
| `asc_setShowGridlines(isShow)` | isShow: boolean | void | 设置显示网格线 |
| `asc_getShowGridlines()` | 无 | boolean | 获取是否显示网格线 |
| `asc_setGridSpacing(nSpacing)` | nSpacing: number | void | 设置网格间距 |
| `asc_getGridSpacing()` | 无 | number | 获取网格间距 |
| `asc_setSnapToGrid(bVal)` | bVal: boolean | void | 设置对齐网格 |
| `asc_getSnapToGrid()` | 无 | boolean | 获取是否对齐网格 |
| `asc_addHorizontalGuide()` | 无 | void | 添加水平参考线 |
| `asc_addVerticalGuide()` | 无 | void | 添加垂直参考线 |
| `asc_canClearGuides()` | 无 | boolean | 是否可以清除参考线 |
| `asc_clearGuides()` | 无 | void | 清除参考线 |
| `asc_deleteGuide(sId)` | sId: string | void | 删除参考线 |

#### 主题和配色

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_ChangeColorSchemeByIdx(nIdx)` | nIdx: number | void | 按索引更改配色方案 |

#### 自动更正

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_SetAutomaticBulletedLists(isAuto)` | isAuto: boolean | void | 设置自动项目符号列表 |
| `asc_SetAutomaticNumberedLists(isAuto)` | isAuto: boolean | void | 设置自动编号列表 |
| `asc_SetAutoCorrectSmartQuotes(isSmartQuotes)` | isSmartQuotes: boolean | void | 设置智能引号 |
| `asc_SetAutoCorrectHyphensWithDash(isReplace)` | isReplace: boolean | void | 设置连字符替换 |
| `asc_SetAutoCorrectFirstLetterOfSentences(isCorrect)` | isCorrect: boolean | void | 设置句首字母大写 |
| `asc_SetAutoCorrectHyperlinks(isCorrect)` | isCorrect: boolean | void | 设置自动超链接 |
| `asc_SetAutoCorrectFirstLetterOfCells(isCorrect)` | isCorrect: boolean | void | 设置单元格首字母大写 |
| `asc_SetAutoCorrectDoubleSpaceWithPeriod(isCorrect)` | isCorrect: boolean | void | 设置双空格替换为句号 |
| `asc_SetFirstLetterAutoCorrectExceptions(exceptions, lang)` | exceptions: array, lang: number | void | 设置首字母大写例外 |
| `asc_GetFirstLetterAutoCorrectExceptions(lang)` | lang: number | array | 获取首字母大写例外 |
| `asc_GetAutoCorrectSettings()` | 无 | object | 获取自动更正设置 |

#### 文本操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_GetSelectedText(bClearText, select_Pr)` | bClearText: boolean, select_Pr: object | string | 获取选中文本 |
| `asc_enterText(codePoints)` | codePoints: array | void | 输入文本 |
| `asc_correctEnterText(oldValue, newValue)` | oldValue: string, newValue: string | void | 更正输入文本 |
| `asc_ChangeTextCase(nType)` | nType: number | void | 更改文本大小写 |

#### 表格操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_DistributeTableCells(isHorizontally)` | isHorizontally: boolean | void | 平均分布表格单元格 |
| `asc_GetDefaultTableStyles()` | 无 | array | 获取默认表格样式 |
| `asc_getTableStylesPreviews(bUseDefault, arrIds)` | bUseDefault: boolean, arrIds: array | array | 获取表格样式预览 |
| `asc_generateTableStylesPreviews(bUseDefault)` | bUseDefault: boolean | void | 生成表格样式预览 |

#### 页眉页脚

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getHeaderFooterProperties()` | 无 | object | 获取页眉页脚属性 |
| `asc_setHeaderFooterProperties(oProps, bAll)` | oProps: object, bAll: boolean | void | 设置页眉页脚属性 |

#### 打印

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_initPrintPreview(containerId, options)` | containerId: string, options: object | void | 初始化打印预览 |
| `asc_drawPrintPreview(index, paperSize)` | index: number, paperSize: object | void | 绘制打印预览 |
| `asc_closePrintPreview()` | 无 | void | 关闭打印预览 |

#### 剪贴板

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_canPaste()` | 无 | boolean | 是否可以粘贴 |
| `asc_SelectionCut()` | 无 | void | 选择剪切 |
| `asc_PasteData(_format, data1, data2, text_data)` | _format: string, data1: string, data2: string, text_data: string | void | 粘贴数据 |
| `asc_SpecialPaste(props)` | props: object | void | 特殊粘贴 |
| `asc_SpecialPasteData(props)` | props: object | void | 特殊粘贴数据 |
| `asc_ShowSpecialPasteButton(props)` | props: object | void | 显示特殊粘贴按钮 |
| `asc_UpdateSpecialPasteButton(props)` | props: object | void | 更新特殊粘贴按钮 |
| `asc_HideSpecialPasteButton()` | 无 | void | 隐藏特殊粘贴按钮 |

#### 撤销重做

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_getCanUndo()` | 无 | boolean | 是否可以撤销 |
| `asc_getCanRedo()` | 无 | boolean | 是否可以重做 |

#### 选择操作

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_EditSelectAll()` | 无 | void | 全选 |
| `asc_Remove()` | 无 | void | 删除选中内容 |

#### 回调注册

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `asc_registerCallback(name, callback)` | name: string, callback: function | void | 注册回调函数 |
| `asc_unregisterCallback(name, callback)` | name: string, callback: function | void | 注销回调函数 |
| `asc_checkNeedCallback(name)` | name: string | boolean | 检查是否需要回调 |

---

## 高级API类 (ApiBuilder)

### Api

全局API类，提供更简洁的链式调用接口。

### ApiPresentation

演示文稿类。

**方法：**

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `GetSlidesCount()` | 无 | number | 获取幻灯片数量 |
| `GetSlide(index)` | index: number | ApiSlide | 获取指定幻灯片 |
| `AddSlide(oLayout)` | oLayout: ApiLayout | ApiSlide | 添加幻灯片 |
| `RemoveSlide(index)` | index: number | boolean | 删除幻灯片 |
| `GetCurrentSlide()` | 无 | ApiSlide | 获取当前幻灯片 |
| `SetCurrentSlide(index)` | index: number | void | 设置当前幻灯片 |
| `GetMastersCount()` | 无 | number | 获取母版数量 |
| `GetMaster(index)` | index: number | ApiMaster | 获取指定母版 |
| `GetLayoutsCount()` | 无 | number | 获取版式数量 |
| `GetLayout(index)` | index: number | ApiLayout | 获取指定版式 |
| `GetTheme()` | 无 | ApiTheme | 获取主题 |
| `SetTheme(oTheme)` | oTheme: ApiTheme | void | 设置主题 |

### ApiSlide

幻灯片类。

**方法：**

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `GetObjectsCount()` | 无 | number | 获取对象数量 |
| `GetObject(index)` | index: number | ApiDrawing | 获取指定对象 |
| `AddObject(oDrawing)` | oDrawing: ApiDrawing | void | 添加对象 |
| `RemoveObject(index)` | index: number | boolean | 删除对象 |
| `GetBackground()` | 无 | ApiFill | 获取背景 |
| `SetBackground(oFill)` | oFill: ApiFill | void | 设置背景 |
| `GetLayout()` | 无 | ApiLayout | 获取版式 |
| `SetLayout(oLayout)` | oLayout: ApiLayout | void | 设置版式 |
| `GetTiming()` | 无 | ApiTiming | 获取时间设置 |
| `SetTiming(oTiming)` | oTiming: ApiTiming | void | 设置时间 |
| `GetTransition()` | 无 | ApiTransition | 获取切换效果 |
| `SetTransition(oTransition)` | oTransition: ApiTransition | void | 设置切换效果 |
| `GetNotes()` | 无 | ApiNotes | 获取备注 |
| `SetNotes(oNotes)` | oNotes: ApiNotes | void | 设置备注 |
| `IsHidden()` | 无 | boolean | 是否隐藏 |
| `SetHidden(isHidden)` | isHidden: boolean | void | 设置隐藏 |

### ApiMaster

母版类。

### ApiLayout

版式类。

### ApiTheme

主题类。

### ApiThemeColorScheme

主题配色方案类。

### ApiThemeFormatScheme

主题格式方案类。

### ApiThemeFontScheme

主题字体方案类。

### ApiDrawing

绘图对象基类。

**方法：**

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `GetPos()` | 无 | {x: number, y: number} | 获取位置 |
| `SetPos(x, y)` | x: number, y: number | void | 设置位置 |
| `GetSize()` | 无 | {width: number, height: number} | 获取尺寸 |
| `SetSize(width, height)` | width: number, height: number | void | 设置尺寸 |
| `GetAngle()` | 无 | number | 获取旋转角度 |
| `SetAngle(angle)` | angle: number | void | 设置旋转角度 |
| `Flip(type)` | type: number | void | 翻转 |
| `Select()` | 无 | void | 选中 |
| `Delete()` | 无 | void | 删除 |
| `Copy()` | 无 | ApiDrawing | 复制 |
| `Duplicate()` | 无 | ApiDrawing | 创建副本 |
| `GetLockValue()` | 无 | number | 获取锁定值 |
| `SetLockValue(value)` | value: number | void | 设置锁定值 |

### ApiShape

形状类，继承自 ApiDrawing。

**方法：**

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `GetContent()` | 无 | ApiDocumentContent | 获取内容 |
| `SetVerticalTextAlign(align)` | align: string | void | 设置垂直对齐 |
| `GetFill()` | 无 | ApiFill | 获取填充 |
| `SetFill(oFill)` | oFill: ApiFill | void | 设置填充 |
| `GetStroke()` | 无 | ApiStroke | 获取边框 |
| `SetStroke(oStroke)` | oStroke: ApiStroke | void | 设置边框 |
| `SetPresetGeometry(preset)` | preset: string | void | 设置预设几何形状 |

### ApiImage

图片类，继承自 ApiDrawing。

### ApiChart

图表类，继承自 ApiDrawing。

### ApiTable

表格类，继承自 ApiDrawing。

### ApiGroup

组合对象类，继承自 ApiDrawing。

### ApiOleObject

OLE对象类，继承自 ApiDrawing。

### ApiFill

填充类。

### ApiStroke

边框类。

### ApiParagraph

段落类。

### ApiRun

文本运行类。

---

## 枚举常量

### c_oAscSlideTransitionTypes

幻灯片切换类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | None | 无切换 |
| 1 | Fade | 淡出 |
| 2 | Push | 推进 |
| 3 | Wipe | 擦除 |
| 4 | Split | 分割 |
| 5 | UnCover | 揭开 |
| 6 | Cover | 覆盖 |
| 7 | Clock | 时钟 |
| 8 | Zoom | 缩放 |
| 9 | Morph | 变形 |

### c_oAscSlideTransitionParams

幻灯片切换参数。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | Fade_Smoothly | 平滑淡出 |
| 1 | Fade_Through_Black | 通过黑色淡出 |
| 0 | Param_Left | 从左 |
| 1 | Param_Top | 从上 |
| 2 | Param_Right | 从右 |
| 3 | Param_Bottom | 从下 |
| 4 | Param_TopLeft | 从左上 |
| 5 | Param_TopRight | 从右上 |
| 6 | Param_BottomLeft | 从左下 |
| 7 | Param_BottomRight | 从右下 |
| 8 | Split_VerticalIn | 垂直内分割 |
| 9 | Split_VerticalOut | 垂直外分割 |
| 10 | Split_HorizontalIn | 水平内分割 |
| 11 | Split_HorizontalOut | 水平外分割 |
| 0 | Clock_Clockwise | 顺时针 |
| 1 | Clock_Counterclockwise | 逆时针 |
| 2 | Clock_Wedge | 楔形 |
| 0 | Zoom_In | 放大 |
| 1 | Zoom_Out | 缩小 |
| 2 | Zoom_AndRotate | 缩放并旋转 |
| 0 | Morph_Objects | 对象变形 |
| 1 | Morph_Words | 单词变形 |
| 2 | Morph_Letters | 字母变形 |

### c_oAscSlideLayoutType

幻灯片版式类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | Blank | 空白 |
| 1 | Chart | 图表 |
| 2 | ChartAndTx | 图表和文本 |
| 3 | ClipArtAndTx | 剪贴画和文本 |
| 4 | ClipArtAndVertTx | 剪贴画和垂直文本 |
| 5 | Cust | 自定义 |
| 6 | Dgm | 图表 |
| 7 | FourObj | 四个对象 |
| 8 | MediaAndTx | 媒体和文本 |
| 9 | Obj | 对象 |
| 10 | ObjAndTwoObj | 对象和两个对象 |
| 11 | ObjAndTx | 对象和文本 |
| 12 | ObjOnly | 仅对象 |
| 13 | ObjOverTx | 对象在文本上方 |
| 14 | ObjTx | 对象文本 |
| 15 | PicTx | 图片文本 |
| 16 | SecHead | 节标题 |
| 17 | Tbl | 表格 |
| 18 | Title | 标题 |
| 19 | TitleOnly | 仅标题 |
| 20 | TwoColTx | 两列文本 |
| 21 | TwoObj | 两个对象 |
| 22 | TwoObjAndObj | 两个对象和一个对象 |
| 23 | TwoObjAndTx | 两个对象和文本 |

### c_oAscAlignShapeType

形状对齐类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | ALIGN_LEFT | 左对齐 |
| 1 | ALIGN_RIGHT | 右对齐 |
| 2 | ALIGN_TOP | 顶部对齐 |
| 3 | ALIGN_BOTTOM | 底部对齐 |
| 4 | ALIGN_CENTER | 水平居中 |
| 5 | ALIGN_MIDDLE | 垂直居中 |

### c_oAscVertAlignJc

垂直对齐方式。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | Top | 顶端对齐 |
| 1 | Center | 居中对齐 |
| 2 | Bottom | 底端对齐 |

### c_oAscAlignType

对齐类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | LEFT | 左对齐 |
| 1 | CENTER | 居中对齐 |
| 2 | RIGHT | 右对齐 |
| 3 | JUSTIFY | 两端对齐 |
| 4 | TOP | 顶部对齐 |
| 5 | MIDDLE | 垂直居中 |
| 6 | BOTTOM | 底部对齐 |

### c_oAscTableSelectionType

表格选择类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | Cell | 单元格 |
| 1 | Row | 行 |
| 2 | Column | 列 |
| 3 | Table | 整个表格 |

### c_oAscTableLayout

表格布局。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | AutoFit | 自动适应 |
| 1 | Fixed | 固定宽度 |

### c_oAscZoomType

缩放类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | Current | 当前缩放 |
| 1 | FitWidth | 适应宽度 |
| 2 | FitPage | 适应页面 |

### c_oAscColorSchemeIndex

配色方案索引。

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | Accent1 | 强调色1 |
| 1 | Accent2 | 强调色2 |
| 2 | Accent3 | 强调色3 |
| 3 | Accent4 | 强调色4 |
| 4 | Accent5 | 强调色5 |
| 5 | Accent6 | 强调色6 |
| 6 | Bg1 | 背景色1 |
| 7 | Bg2 | 背景色2 |
| 8 | Dk1 | 深色1 |
| 9 | Dk2 | 深色2 |
| 10 | FolHlink | 跟随超链接 |
| 11 | Hlink | 超链接 |
| 12 | Lt1 | 浅色1 |
| 13 | Lt2 | 浅色2 |
| 14 | PhClr | 占位符颜色 |
| 15 | Tx1 | 文本色1 |
| 16 | Tx2 | 文本色2 |

### c_oAscLockTypeElemPresentation

锁定类型。

| 值 | 名称 | 说明 |
|----|------|------|
| 1 | Object | 对象锁定 |
| 2 | Slide | 幻灯片锁定 |
| 3 | Presentation | 演示文稿锁定 |

---

## 回调事件

通过 `asc_registerCallback` 方法注册的事件回调。

### 文档事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onDocumentModifiedChanged` | bIsModified: boolean | 文档修改状态改变 |
| `asc_onDocumentCanSaveChanged` | bCanSave: boolean | 文档可保存状态改变 |
| `asc_onError` | errorId: number, errorLevel: number | 发生错误 |
| `asc_onStartAction` | type: number, id: number | 开始操作 |
| `asc_onEndAction` | type: number, id: number | 结束操作 |

### 幻灯片事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onCountPages` | count: number | 幻灯片数量改变 |
| `asc_onCurrentPage` | page: number | 当前幻灯片改变 |
| `asc_onFocusObject` | objects: array | 焦点对象改变 |

### 编辑事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onCanUndoChanged` | bCanUndo: boolean | 可撤销状态改变 |
| `asc_onCanRedoChanged` | bCanRedo: boolean | 可重做状态改变 |
| `asc_onBold` | isBold: boolean | 粗体状态改变 |
| `asc_onItalic` | isItalic: boolean | 斜体状态改变 |
| `asc_onUnderline` | isUnderline: boolean | 下划线状态改变 |
| `asc_onStrikeout` | isStrikeout: boolean | 删除线状态改变 |

### 视图事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onZoom` | zoom: number | 缩放改变 |
| `asc_onMouseMove` | mouseData: object | 鼠标移动 |

### 其他事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `asc_onInitEditorFonts` | fonts: object | 初始化编辑器字体 |
| `asc_onInitEditorStyles` | styles: object | 初始化编辑器样式 |
| `asc_onHyperlinkClick` | url: string | 超链接点击 |
| `asc_onCoAuthoringDisconnect` | 无 | 协作断开连接 |
| `asc_onAdvancedOptions` | id: number, options: object | 高级选项 |
| `asc_onContextMenu` | data: object | 上下文菜单 |

---

## 使用示例

### 初始化编辑器

```javascript
// 创建API实例
var api = new Asc.asc_docs_api({
  // 配置选项
});

// 注册回调
api.asc_registerCallback('asc_onDocumentModifiedChanged', function(isModified) {
  console.log('文档修改状态:', isModified);
});

api.asc_registerCallback('asc_onCountPages', function(count) {
  console.log('幻灯片数量:', count);
});

api.asc_registerCallback('asc_onCurrentPage', function(page) {
  console.log('当前幻灯片:', page);
});
```

### 幻灯片操作

```javascript
// 移动幻灯片
api.asc_moveSelectedSlidesToEnd();  // 移到最后
api.asc_moveSelectedSlidesToStart(); // 移到开头

// 检查幻灯片状态
var isSelected = api.asc_IsSlideSelected(0);
var isFirstSelected = api.asc_IsFirstSlideSelected();
var isLastSelected = api.asc_IsLastSlideSelected();

// 隐藏幻灯片
api.asc_HideSlides(true);

// 添加幻灯片编号
api.asc_addSlideNumber();

// 添加日期时间
api.asc_addDateTime({
  Format: 'yyyy-MM-dd',
  Position: 0
});
```

### 动画操作

```javascript
// 添加动画
api.asc_AddAnimation(0, 1, 0, true, true);  // 类别, ID, 子类型, 替换, 预览

// 预览动画
if (api.asc_canStartAnimationPreview()) {
  api.asc_StartAnimationPreview();
}

// 停止预览
api.asc_StopAnimationPreview();

// 移动动画顺序
if (api.asc_canMoveAnimationEarlier()) {
  api.asc_moveAnimationEarlier();
}

if (api.asc_canMoveAnimationLater()) {
  api.asc_moveAnimationLater();
}

// 设置动画属性
api.asc_SetAnimationProperties({
  Duration: 1000,
  Delay: 500
});
```

### 形状和图片操作

```javascript
// 获取选中对象数量
var count = api.asc_getSelectedDrawingObjectsCount();

// 裁剪图片
if (api.asc_canEditCrop()) {
  api.asc_startEditCrop();
  // ... 裁剪操作
  api.asc_endEditCrop();
}

// 图片适应幻灯片
api.asc_FitImagesToSlide();
```

### 视图设置

```javascript
// 设置参考线
api.asc_setShowGuides(true);
api.asc_setShowSmartGuides(true);

// 设置网格
api.asc_setShowGridlines(true);
api.asc_setGridSpacing(10);
api.asc_setSnapToGrid(true);

// 添加参考线
api.asc_addHorizontalGuide();
api.asc_addVerticalGuide();

// 清除参考线
if (api.asc_canClearGuides()) {
  api.asc_clearGuides();
}
```

### 查找替换

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
}, '新内容', false);  // false = 替换第一个, true = 全部替换
```

### 使用高级API

```javascript
// 获取演示文稿
var presentation = Api.GetPresentation();

// 获取幻灯片数量
var slidesCount = presentation.GetSlidesCount();

// 获取当前幻灯片
var slide = presentation.GetCurrentSlide();

// 添加新幻灯片
var newSlide = presentation.AddSlide(layout);

// 获取幻灯片上的对象
var objectsCount = slide.GetObjectsCount();
for (var i = 0; i < objectsCount; i++) {
  var obj = slide.GetObject(i);
  console.log('对象类型:', obj.GetClassType());
}

// 设置幻灯片背景
var fill = Api.CreateSolidFill(Api.CreateColorFromRGB(255, 0, 0));
slide.SetBackground(fill);

// 添加形状
var shape = slide.AddShape('rect', 100, 100, 200, 150);

// 设置形状属性
shape.SetFill(Api.CreateSolidFill(Api.CreateColorFromRGB(0, 128, 255)));
shape.SetStroke(Api.CreateStroke(1, Api.CreateSolidFill(Api.CreateColorFromRGB(0, 0, 0))));

// 添加文本
var content = shape.GetContent();
var paragraph = content.GetElement(0);
paragraph.AddText('Hello World');
```

---

## 注意事项

1. 幻灯片索引从0开始
2. 尺寸单位默认为毫米(mm)
3. 颜色使用 RGB 值，范围为 0-255
4. 大部分方法需要等待编辑器初始化完成后才能调用
5. 回调函数的注册应在文档加载前完成
6. 部分功能需要服务器端支持

---

*文档版本: 1.0.0*
*基于 SE Office 项目整理*
