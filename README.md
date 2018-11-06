# 中医智能检索系统 TCM-Retrieval-System

[TOC]

## 简介

​	中医智能检索系统是一款辅助中医医生开药方的桌面软件，包含录入和检索症状、病症、药方、药材的功能，也具备文献检索功能。	

## 文档

- [使用说明](Document/Usage.md)
- [开发文档](Document/Dev.md)
- [录入模式UML图](Document/录入活动图.pdf)
- [问诊模式UML图](Document/问诊活动图.pdf)

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

## 功能设计

### 录入基本信息

### 药方检索

### 记录诊断信息

## 交互设计

------

Collaborators: [Alanlinzy](https://github.com/alanlinzy), [Brahamack](https://github.com/brahamack), [Defjia](https://github.com/DefJia)