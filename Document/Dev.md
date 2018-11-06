# 开发者文档

[TOC]

## 开发规范

### 文件存放位置

- 文档位于Document/
- UI文件及生成的Python文件位于文件夹UI/下
- 暂时用不到的文件与相关备份位于Backup/下

### 操作说明

- Control.py包含与界面显示有关的方法
- Front.py包含前端方法，负责处理被触发的请求并修改界面内容
- Back.py包含与数据库调用相关的内容，API文档可见API.md
- .config.ini是与环境有关的配置文件

### 命令规范

#### PyQt组件名

- 采用驼峰命名法，控件类型+名称，如lineSymptom

## 数据库设计

数据库名一律小写。

### 中药(Medicine)

- 序号[id, PK, int(4)]
- 药名[name]
- 属性[attr]
  - 先煎
  - 后煎

### 药方(Anagraph)

- 药方名[name, PK]
- 对应中药ID以及克数的集合[info]

### 病(Illness)

- 序号[id, PK, int(4)]
- 病症名[name]
- 对应药方ID的集合[ana_id]

### 症状(symptom)

- 序号[id, PK, int(4)]
- 症状名[name]
- 对应病的ID[ill_id]