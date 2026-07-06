# MCM/ICM CDMS

> 面向 MCM/ICM 数学建模竞赛的 Python/Jupyter 培训资料与课程建设计划。

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#)
[![Jupyter](https://img.shields.io/badge/Jupyter-notebooks-orange)](notebooks/README.md)
[![MCM/ICM](https://img.shields.io/badge/MCM%2FICM-modeling-green)](#)
[![Lessons](https://img.shields.io/badge/curriculum-18_lessons-orange)](docs/training-plan/06-18-lesson-syllabus.md)
[![Docs](https://img.shields.io/badge/docs-training_plan-lightgrey)](docs/training-plan/README.md)

本仓库用于沉淀美赛培训课件、Python/Jupyter 示例、课程路线和学员作业模板。它的目标不是只讲单个算法，而是训练一条完整的竞赛工作链：

```text
读题与数据理解 -> 数据清洗与可视化 -> 建模与求解 -> 结果解释 -> 论文支撑
```

> 资料仅供培训项目内部使用，请勿转发。

## 目录

- [项目亮点](#项目亮点)
- [当前内容](#当前内容)
- [18 讲课程体系](#18-讲课程体系)
- [快速开始](#快速开始)
- [仓库结构](#仓库结构)
- [使用建议](#使用建议)
- [建设路线](#建设路线)
- [参考资料](#参考资料)

## 项目亮点

- **完整课程线**：已规划并落成 18 讲 Jupyter Notebook，从竞赛流程、Python 数据处理，到模型、优化、仿真、论文和模拟赛。
- **可运行示例**：18 个 Notebook 均包含可执行 Python 示例代码，并通过 `nbclient` 执行验证。
- **训练闭环**：每讲都围绕课堂目标、课堂练习、课后作业和验收标准组织。
- **面向比赛交付**：强调图表、结果表、模型解释和论文支撑，而不只是代码运行。
- **可继续扩展**：后续可以继续补充真实数据集、优秀作业、模拟赛题和论文示例。

## 当前内容

| 文件 | 主题 | 对应课程 |
| --- | --- | --- |
| `notebooks/` | 18 讲 Python/Jupyter 示例代码 | 第 1-18 讲 |
| `m_Sai_02_2.mlx` | 早期 MATLAB 数据结构课件，作为迁移参考保留 | 第 2 讲 |
| `m_Sai_02_1.mlx` | 早期 MATLAB 数据处理课件，作为迁移参考保留 | 第 3-4 讲 |
| `m_Sai_03_1.mlx` | 早期回归、聚类、PCA 课件，作为迁移参考保留 | 第 5-6 讲 |
| `m_Sai_04_1.mlx` | 早期优化模型课件，作为迁移参考保留 | 第 10-11 讲 |

## 18 讲课程体系

完整大纲见：[docs/training-plan/06-18-lesson-syllabus.md](docs/training-plan/06-18-lesson-syllabus.md)

单讲设计索引见：[docs/training-plan/lessons/README.md](docs/training-plan/lessons/README.md)

Notebook 入口见：[notebooks/README.md](notebooks/README.md)

| 阶段 | 讲次 | 能力目标 |
| --- | --- | --- |
| 竞赛理解 | 第 1 讲 | 理解 MCM/ICM 流程、题型和团队分工 |
| Python 数据处理 | 第 2-4 讲 | 完成数据组织、清洗、统计和可视化 |
| 基础模型 | 第 5-9 讲 | 掌握回归、聚类、PCA、评价、预测和分类模型 |
| 优化与仿真 | 第 10-14 讲 | 掌握规划、图论、仿真、敏感性和鲁棒性分析 |
| 论文与模拟赛 | 第 15-18 讲 | 完成论文表达、图表叙事和综合模拟赛 |

## 快速开始

### 1. 克隆仓库

```bash
git clone git@github.com:Changsheng0727/MCM_ICM_CDMS.git
cd MCM_ICM_CDMS
```

### 2. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

### 3. 打开 Notebook

```bash
jupyter notebook notebooks
```

也可以直接验证全部 18 讲：

```bash
python tools/validate_notebooks.py
```

### 4. 阅读培训计划

建议从这里开始：

1. [培训项目计划总览](docs/training-plan/README.md)
2. [18 讲课程大纲](docs/training-plan/06-18-lesson-syllabus.md)
3. [Python/Jupyter Notebook 索引](notebooks/README.md)
4. [单讲课程设计索引](docs/training-plan/lessons/README.md)
5. [路线选择与执行节奏](docs/training-plan/05-roadmap-and-cadence.md)

## 仓库结构

```text
MCM_ICM_CDMS/
  README.md
  m_Sai_02_1.mlx
  m_Sai_02_2.mlx
  m_Sai_03_1.mlx
  m_Sai_04_1.mlx
  requirements.txt
  notebooks/
    lesson-01-competition-workflow.ipynb
    ...
    lesson-18-mini-contest-report-review.ipynb
  tools/
    generate_jupyter_lessons.py
    validate_notebooks.py
  docs/
    training-plan/
      README.md
      00-project-backbone.md
      01-course-delivery-track.md
      02-modeling-method-track.md
      03-matlab-reproducibility-track.md
      04-student-assessment-track.md
      05-roadmap-and-cadence.md
      06-18-lesson-syllabus.md
      lessons/
      templates/
```

## 使用建议

### 对讲师

- 先读 [18 讲课程大纲](docs/training-plan/06-18-lesson-syllabus.md)，确认本轮培训覆盖范围。
- 每次授课前打开对应的 [Notebook](notebooks/README.md) 和 [单讲设计](docs/training-plan/lessons/README.md)，检查课堂目标、练习和作业。
- 课后根据 [周复盘模板](docs/training-plan/templates/weekly-review-template.md) 更新下一讲重点。

### 对学员

- 先跑通对应 Notebook，不急着改复杂模型。
- 每讲至少提交一个可检查交付件：代码、图表、结果表或解释段落。
- 学到模型后必须练习“结果怎么写进论文”，不要只停在运行代码。

## 建设路线

| 优先级 | 任务 | 目标 |
| --- | --- | --- |
| P0 | 用 Notebook 持续打磨第 7-18 讲示例 | 建立完整模型、论文与模拟赛闭环 |
| P1 | 持续把原 `.mlx` 参考内容吸收到 Python Notebook | 保持无 MATLAB 依赖的主路线 |
| P1 | 新增 `data/`、`src/`、`outputs/` 目录 | 形成从数据到结果的标准链路 |
| P2 | 补充评价、预测、分类、图论、仿真案例 | 扩展题型覆盖面 |
| P2 | 增加优秀作业和论文片段示例 | 提升学员结果表达能力 |

## 参考资料

README 的结构参考了：

- [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
- [awesome-readme](https://github.com/matiassingers/awesome-readme)

课程计划入口：

- [培训项目计划总览](docs/training-plan/README.md)
- [18 讲课程大纲](docs/training-plan/06-18-lesson-syllabus.md)
- [单讲课程设计索引](docs/training-plan/lessons/README.md)
- [Python/Jupyter Notebook 索引](notebooks/README.md)
