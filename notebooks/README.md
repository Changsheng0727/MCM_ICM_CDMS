# Python/Jupyter 18 讲课程 Notebook

> 返回：[项目 README](../README.md)

本目录保存 18 讲课程体系对应的 Jupyter Notebook 课件。每一讲都包含课件导学、资料链接、可运行示例、实战环节、课后挑战和验收清单，用于替代原 MATLAB 依赖，让培训项目可以基于 Python 继续推进。

## 运行方式

安装依赖：

```bash
pip install -r requirements.txt
```

启动 Jupyter：

```bash
jupyter notebook
```

或验证全部 Notebook：

```bash
python tools/validate_notebooks.py
```

每个 Notebook 默认会把图表、表格或报告片段输出到：

```text
outputs/lesson-xx/
```

课程化版本还会额外保存：

- `lesson_resources.csv`：本讲参考资料和阅读抓手
- `lesson_deliverables.csv`：本讲交付物清单
- `lesson_checklist.csv`：课堂/课后验收清单

## 18 讲 Notebook 索引

| 讲次 | Notebook | 主题 |
| --- | --- | --- |
| 第 1 讲 | [lesson-01-competition-workflow.ipynb](lesson-01-competition-workflow.ipynb) | 美赛流程、题型与团队分工 |
| 第 2 讲 | [lesson-02-python-data-structures.ipynb](lesson-02-python-data-structures.ipynb) | Python 数据结构与 DataFrame |
| 第 3 讲 | [lesson-03-data-cleaning-visualization.ipynb](lesson-03-data-cleaning-visualization.ipynb) | 数据导入、清洗与基础可视化 |
| 第 4 讲 | [lesson-04-eda-visual-storytelling.ipynb](lesson-04-eda-visual-storytelling.ipynb) | 探索性数据分析与可视化表达 |
| 第 5 讲 | [lesson-05-regression-diagnostics.ipynb](lesson-05-regression-diagnostics.ipynb) | 回归模型与拟合诊断 |
| 第 6 讲 | [lesson-06-clustering-pca.ipynb](lesson-06-clustering-pca.ipynb) | 聚类分析与 PCA 降维 |
| 第 7 讲 | [lesson-07-evaluation-models.ipynb](lesson-07-evaluation-models.ipynb) | 综合评价模型 |
| 第 8 讲 | [lesson-08-forecasting-models.ipynb](lesson-08-forecasting-models.ipynb) | 预测模型基础 |
| 第 9 讲 | [lesson-09-classification-models.ipynb](lesson-09-classification-models.ipynb) | 分类模型与机器学习入门 |
| 第 10 讲 | [lesson-10-linear-programming.ipynb](lesson-10-linear-programming.ipynb) | 线性规划与资源分配 |
| 第 11 讲 | [lesson-11-integer-multiobjective.ipynb](lesson-11-integer-multiobjective.ipynb) | 整数规划、0-1 规划与多目标优化 |
| 第 12 讲 | [lesson-12-graph-network-models.ipynb](lesson-12-graph-network-models.ipynb) | 图论与网络模型 |
| 第 13 讲 | [lesson-13-monte-carlo-simulation.ipynb](lesson-13-monte-carlo-simulation.ipynb) | 仿真模型与蒙特卡洛 |
| 第 14 讲 | [lesson-14-sensitivity-robustness.ipynb](lesson-14-sensitivity-robustness.ipynb) | 敏感性、鲁棒性与模型检验 |
| 第 15 讲 | [lesson-15-paper-structure-latex.ipynb](lesson-15-paper-structure-latex.ipynb) | 论文结构、数学表达与 LaTeX |
| 第 16 讲 | [lesson-16-result-narrative.ipynb](lesson-16-result-narrative.ipynb) | 图表叙事与结果解释 |
| 第 17 讲 | [lesson-17-mini-contest-modeling.ipynb](lesson-17-mini-contest-modeling.ipynb) | 综合模拟赛 I：读题、建模与代码 |
| 第 18 讲 | [lesson-18-mini-contest-report-review.ipynb](lesson-18-mini-contest-report-review.ipynb) | 综合模拟赛 II：论文打磨与复盘 |

## 维护说明

Notebook 由脚本生成：

```bash
python tools/generate_jupyter_lessons.py
```

如果需要批量修改课程结构，优先修改生成器，再重新生成 Notebook，避免手工改 18 个文件导致结构漂移。
