# 中医智能检索系统 TCM-Retrieval-System

[TOC]

## 简介

​	中医智能检索系统是一款辅助中医医生开药方的桌面软件，包含录入和检索症状、病症、药方、药材的功能，也具备文献检索功能。	

## 文档

- [使用说明](Document/Usage.md)
- [开发文档](Document/Dev.md)
- [接口文档](Document/API.md)
- [录入模式UML图](Document/录入活动图.pdf)
- [问诊模式UML图](Document/问诊活动图.pdf)

## 界面设计

![深度截图_Control.py_20181107190137](Backup/深度截图_Control.py_20181107190137.png)

## 开发进程

### UI界面

- [ ] 修改下拉框的命名方式，同时修改代码中相关的变量
- [x] **在检索模式下，隐藏+号**
- [ ] 在录入模式下，应有编辑和删除按钮
- [x] **去掉其他三个的表头**
- [x] 模式选择按钮貌似改成RadioButton这样的多选框比较好？
- [x] 在开方工作区下添加清空和保存按钮
- [x] **另外可以考虑加个标题**
- [ ] 录入药需要选择属性
- [x] **去掉表头*3**
- [ ] 统一组件名称命名方法并同步修改代码中变量
- [ ] **添加当前位置的文本框（我好像给删了）**

- [ ] radiobutton替换成标签页/或界面变化更明显一点
- [ ] 录入框中修改，可删除
- [ ] 录入模式——按钮——建立病症药方关系；开放模式——按钮——导入药方
### Control类

- [ ] 完善相关功能
- [x] RadioButtom使加号消失
- [ ] 以列表的形式添加数据到 tablewidgetXXX里面
- [ ] symptom ---> disease 里面查询(按匹配程度排序)
- [ ] 点击disease，prescript变化
- [ ] 点击药方，药变化
- [ ] 点 录入 药方下移
- [ ] 修改 药克 数以及用法，可删除，添加
### Front类

- [x] set_table函数应该只显示一列
- [ ] 添加成功后最好可以弹框提示
- [ ] 完善相关功能

### Back类

- [ ] 完善相关功能
- [ ] 病名命中次数排序/ 

### 数据库

- [ ] 修改medicine表结构，添加属性
- [ ] 新建药方表

### information 界面
- [ ] 添加过程可能有bug
- [ ] 主诉，点击option出现bug
- [ ] 查询功能没有测试
- [ ] 界面，6个框

------

Collaborators: [Alanlinzy](https://github.com/alanlinzy), [Brahamack](https://github.com/brahamack), [Defjia](https://github.com/DefJia)
