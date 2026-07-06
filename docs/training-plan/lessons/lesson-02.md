# 第 2 讲：Python 数据结构与 DataFrame

## 课程定位

这一讲主入口是 [lesson-02-python-data-structures.ipynb](../../../notebooks/lesson-02-python-data-structures.ipynb)，目标是让学员能正确组织比赛数据。早期 `m_Sai_02_2.mlx` 仅作为迁移参考保留。

## 课堂目标

- 掌握数值、字符串、布尔值、分类变量等基础类型
- 掌握列表、字典、数组和 `pandas.DataFrame`
- 理解为什么 `DataFrame` 是美赛数据处理的常用结构

## 核心概念

- `int`、`float`
- `category`
- `DataFrame`
- 索引与切片
- 数据类型转换

## 课堂演示

基于 Notebook 演示：

- 创建不同类型数据
- 构建混合类型表格
- 进行筛选、分组和类型转换

## 课堂练习

给一份包含数值、文本、类别字段的小数据，让学员创建 `DataFrame` 并完成筛选。

## 课后作业

提交一个 Python Notebook 或脚本：

- 创建一份包含至少 4 个变量的数据表
- 包含至少 1 个分类变量
- 完成 2 个筛选条件
- 输出筛选后的结果

## 验收标准

| 项目 | 标准 |
| --- | --- |
| 数据结构 | 正确使用 `DataFrame` |
| 类型转换 | 至少完成一次类型转换 |
| 筛选逻辑 | 筛选条件正确 |
| 代码清晰 | 变量命名可读 |

## 后续建设建议

把 Notebook 中的数据结构练习沉淀为 `src/lesson02_data_types/` 下的独立 Python 脚本。
