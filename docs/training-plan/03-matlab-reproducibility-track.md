# 03 MATLAB 代码与复现线

## 这条线解决什么

MATLAB 代码与复现线关注的是：课件代码能不能从教学演示变成比赛可复用资产。

Live Script 很适合讲课，但真正比赛时还需要更清晰的文件组织：

```text
raw data -> preprocessing -> model -> figures/tables -> result summary
```

## 当前仓库状态

当前仓库主要由 `.mlx` 文件组成：

- `m_Sai_02_1.mlx`
- `m_Sai_02_2.mlx`
- `m_Sai_03_1.mlx`
- `m_Sai_04_1.mlx`

建议保留 `.mlx` 作为课堂材料，同时逐步补充：

- `data/`：示例数据
- `src/`：可复用脚本和函数
- `outputs/`：图表和结果表
- `docs/`：课程计划、作业、说明

## 推荐目录结构

```text
MCM_ICM_CDMS/
  data/
    raw/
    processed/
  src/
    lesson02_data_processing/
    lesson03_modeling/
    lesson04_optimization/
  outputs/
    figures/
    tables/
  docs/
    training-plan/
```

18 讲扩展后，建议同步建立：

```text
src/
  lesson01_competition_workflow/
  lesson02_data_types/
  ...
  lesson18_final_review/
```

单讲设计索引见：[lessons/README.md](lessons/README.md)。

## 代码规范

### 文件命名

- 课件：`m_Sai_02_1.mlx`
- 脚本：`lesson02_data_cleaning.m`
- 函数：`clean_missing_values.m`
- 图表：`lesson03_regression_fit.png`
- 表格：`lesson04_optimization_result.csv`

### 每个脚本必须包含

- 输入数据说明
- 关键参数说明
- 输出文件说明
- 运行方式说明
- 结果解释入口

### 每个结果必须可追踪

论文或讲义里出现的数值，必须能追溯到：

- MATLAB 输出
- 保存的表格
- 保存的图
- 或明确的计算公式

## 第 2 讲代码复现要求

最低要求：

- 从 CSV 或 Excel 导入数据
- 处理缺失值
- 输出描述统计表
- 输出至少 3 张图
- 保存清洗后的数据

建议输出：

- `outputs/tables/lesson02_summary.csv`
- `outputs/figures/lesson02_histogram.png`
- `outputs/figures/lesson02_boxplot.png`
- `outputs/figures/lesson02_scatter.png`

## 第 3 讲代码复现要求

最低要求：

- 回归模型可复现
- 聚类结果可复现
- PCA 可视化可复现
- 模型评价指标可复现

建议输出：

- `outputs/tables/lesson03_regression_coefficients.csv`
- `outputs/tables/lesson03_cluster_profile.csv`
- `outputs/figures/lesson03_regression_fit.png`
- `outputs/figures/lesson03_pca_clusters.png`

## 第 4 讲代码复现要求

最低要求：

- 线性规划模型参数清晰
- 整数规划模型参数清晰
- 可行域或结果图可保存
- 最优解和目标函数值可追踪

建议输出：

- `outputs/tables/lesson04_lp_solution.csv`
- `outputs/tables/lesson04_ip_solution.csv`
- `outputs/figures/lesson04_feasible_region.png`

## 运行前检查

- [ ] 代码能从仓库根目录运行
- [ ] 数据路径使用相对路径
- [ ] 不依赖本机绝对路径
- [ ] 输出目录不存在时能自动创建
- [ ] 图表和表格能被保存
- [ ] 关键结论有对应输出文件支撑
