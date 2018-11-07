# 开发者文档

[TOC]

## 开发规范

### 文件存放位置

- 所有文档位于Document/
- UI文件及生成的Python文件位于文件夹UI/下
- 暂时用不到的文件与相关备份位于Backup/下

### 操作说明

- Control.py包含与界面显示有关的方法
- Front.py包含前端方法，负责处理被触发的请求并修改界面内容
- Back.py包含与数据库调用相关的内容，API文档可见API.md
- 数据库文件为Data/Main.db，生成的sql语句为Data/init.sql
  - 在测试阶段，修改数据库或添加数据，直接在语句中修改，然后重新跑一遍覆盖原有数据库
- .config.ini是与环境有关的配置文件

### 命名规范

#### PyQt组件名

- 采用驼峰命名法，控件类型+名称，如lineSymptom

#### Python代码命名

- 类的命名，首字母大写
- 方法函数的命名，除特殊函数外，用三个以下英文单词表述其功能，用下划线连接，均小写。

#### 数据库命名

- 数据库名一律小写
- 字段名称一律小写

## 数据库设计

### 中药(Medicine)

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