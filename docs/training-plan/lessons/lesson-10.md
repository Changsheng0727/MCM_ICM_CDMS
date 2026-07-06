# 第 10 讲：线性规划与资源分配

## 课程定位

这一讲主入口是 [lesson-10-linear-programming.ipynb](../../../notebooks/lesson-10-linear-programming.ipynb)，训练优化建模基本功。早期 `m_Sai_04_1.mlx` 仅作为迁移参考保留。

## 课堂目标

- 能从实际问题中定义决策变量
- 能写出目标函数和线性约束
- 能用 `scipy.optimize.linprog` 求解
- 能解释最优解和可行域

## 核心概念

- 决策变量
- 目标函数
- 约束条件
- 可行域
- 最优解

## 课堂演示

使用生产计划问题演示：

- 参数整理
- `scipy.optimize.linprog` 求解
- 二维可行域可视化
- 最优解解释

## 课堂练习

学员把一个资源分配问题写成标准线性规划形式。

## 课后作业

提交：

- 模型三要素
- Python/Jupyter 求解代码
- 最优解表
- 可行域或结果图

## 验收标准

| 项目 | 标准 |
| --- | --- |
| 变量 | 决策变量定义清楚 |
| 目标 | 目标函数方向正确 |
| 约束 | 约束完整 |
| 解释 | 最优解有业务含义 |

## 后续建设建议

把 Notebook 中 LP 案例沉淀为 `lesson10_linear_programming.py`。
