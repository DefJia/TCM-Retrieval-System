# 中医智能检索系统 TCM-Retrieval-System

[TOC]

## 简介

## 功能设计

### 录入基本信息

### 药方检索

### 记录诊断信息

## 代码结构

## 数据库设计

### 中药

- ID

- 药名
- 属性
  - 先煎
  - 后煎

### 中药 - 别名（预留） 

- ID
- 别名
- 对应中药正名ID

### 药方

- ID
- 药方名
- 对应中药ID以及克数的集合

### 病

- ID
- 病症名
- 对应药方ID的集合

### 症状

- ID
- 症状名
- 对应病的ID



------

Collaborators: [alanlinzy](https://github.com/alanlinzy), [brahamack](https://github.com/brahamack), [Defjia](https://github.com/DefJia)