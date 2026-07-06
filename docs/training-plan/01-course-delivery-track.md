# 01 授课交付线

## 这条线解决什么

授课交付线关注的是：每一讲如何从“老师能讲”变成“学生能学、能练、能交付”。

目标不是把课件做长，而是把每讲做成一个闭环：

```text
课前准备 -> 课堂演示 -> 课堂练习 -> 课后作业 -> 结果验收
```

## 每讲标准结构

| 模块 | 内容 |
| --- | --- |
| 课前目标 | 学员上课前需要知道什么 |
| 课堂目标 | 这节课结束后必须能做什么 |
| 核心概念 | 本讲最重要的 3-5 个概念 |
| 代码演示 | 课堂必须跑通的 Python/Jupyter 片段 |
| 实战练习 | 学员当场完成的小任务 |
| 课后作业 | 可独立完成的交付件 |
| 验收标准 | 如何判断学员真的会了 |

## 已有课程如何整理

完整 18 讲课程设计入口：[lessons/README.md](lessons/README.md)。

### 第 2-4 讲：Python 数据处理与 EDA

对应文件：

- [notebooks/lesson-02-python-data-structures.ipynb](../../notebooks/lesson-02-python-data-structures.ipynb)
- [notebooks/lesson-03-data-cleaning-visualization.ipynb](../../notebooks/lesson-03-data-cleaning-visualization.ipynb)
- [notebooks/lesson-04-eda-visual-storytelling.ipynb](../../notebooks/lesson-04-eda-visual-storytelling.ipynb)

重点交付：

- 学员能理解 Python 常见数据类型
- 学员能用 `pandas.DataFrame` 组织混合数据
- 学员能处理缺失值、筛选数据、保存清洗结果
- 学员能画出直方图、箱线图、散点图和基础统计图

课后作业：

- 给一份 CSV 数据，完成导入、清洗、描述统计和 3 张图

### 第 5-6 讲：基础建模算法

对应文件：

- [notebooks/lesson-05-regression-diagnostics.ipynb](../../notebooks/lesson-05-regression-diagnostics.ipynb)
- [notebooks/lesson-06-clustering-pca.ipynb](../../notebooks/lesson-06-clustering-pca.ipynb)

重点交付：

- 学员能完成线性回归建模
- 学员能解释回归系数、拟合效果和残差
- 学员能完成 K-means 聚类并解释聚类结果
- 学员能用 PCA 做降维可视化

课后作业：

- 给一份多变量数据，完成回归、聚类、PCA 三个小模型，并写出结果解释

### 第 10-11 讲：数学规划与优化模型

对应文件：

- [notebooks/lesson-10-linear-programming.ipynb](../../notebooks/lesson-10-linear-programming.ipynb)
- [notebooks/lesson-11-integer-multiobjective.ipynb](../../notebooks/lesson-11-integer-multiobjective.ipynb)

重点交付：

- 学员能把实际问题写成决策变量、目标函数、约束条件
- 学员能用 `scipy.optimize.linprog` 求解线性规划
- 学员能通过枚举、小规模搜索或 MILP 工具理解整数规划和 0-1 规划
- 学员能理解非线性规划和多目标优化的基本场景

课后作业：

- 给一个生产计划或资源分配问题，建立优化模型并给出结果解释

## 授课节奏建议

每讲建议拆成 90-120 分钟：

| 时间 | 内容 |
| --- | --- |
| 0-10 分钟 | 回顾上一讲作业和常见问题 |
| 10-30 分钟 | 新概念和问题背景 |
| 30-65 分钟 | 代码演示 |
| 65-95 分钟 | 学员现场练习 |
| 95-115 分钟 | 结果讲评和误区修正 |
| 最后 5 分钟 | 明确课后作业和提交要求 |

## 讲师检查清单

- [ ] 本讲是否有明确的学员交付件
- [ ] 代码是否能从干净环境跑通
- [ ] 示例数据是否随仓库提供或说明来源
- [ ] 图表是否能保存为文件
- [ ] 学员是否知道结果应该怎么写进论文
