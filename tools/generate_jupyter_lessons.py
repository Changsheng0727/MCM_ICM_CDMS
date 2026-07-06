"""Generate the Python/Jupyter lesson notebooks for the MCM/ICM CDMS course."""

from __future__ import annotations

from pathlib import Path

import nbformat as nbf


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = REPO_ROOT / "notebooks"


COMMON_SETUP = r"""
from pathlib import Path
import os
import math
import itertools
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
plt.rcParams["figure.figsize"] = (8, 5)
plt.rcParams["axes.grid"] = True

REPO_ROOT = Path.cwd().resolve()
if REPO_ROOT.name == "notebooks":
    REPO_ROOT = REPO_ROOT.parent

OUTPUT_ROOT = Path(os.environ.get("COURSE_OUTPUT_DIR", REPO_ROOT / "outputs")) / LESSON_ID
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(42)
print(f"Output directory: {OUTPUT_ROOT}")
"""


def md(text: str):
    return nbf.v4.new_markdown_cell(text.strip())


def code(text: str):
    return nbf.v4.new_code_cell(text.strip())


def notebook(title: str, lesson_id: str, objective: str, cells: list):
    nb = nbf.v4.new_notebook()
    nb["metadata"] = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    }
    nb.cells = [
        md(f"# {title}\n\n> {objective}"),
        md(
            "## 使用说明\n\n"
            "- 先从上到下运行全部单元。\n"
            "- 每讲都会生成一个 `outputs/lesson-xx/` 目录，用于保存图表、表格或报告片段。\n"
            "- 示例数据均为教学用合成数据，真实比赛中应替换为题目附件数据。"
        ),
        code(f'LESSON_ID = "{lesson_id}"\n' + COMMON_SETUP),
    ]
    nb.cells.extend(cells)
    return nb


LESSONS = [
    {
        "file": "lesson-01-competition-workflow.ipynb",
        "id": "lesson-01",
        "title": "第 1 讲：美赛流程、题型与团队分工",
        "objective": "用 Python 把比赛流程、角色分工和交付物管理结构化，建立可复用的项目管理表。",
        "cells": [
            md("## 1. 比赛工作流拆解"),
            code(
                r"""
workflow = pd.DataFrame({
    "阶段": ["读题", "拆题", "数据审计", "建模", "求解", "图表", "写作", "检查提交"],
    "核心问题": [
        "题目到底要求什么？",
        "每个子问题的输入输出是什么？",
        "数据是否完整、可信、可用？",
        "每个子问题对应什么模型？",
        "代码能否复现关键结果？",
        "图表是否支撑结论？",
        "模型是否被清楚写进论文？",
        "格式、页数、匿名性、附件是否合规？",
    ],
    "负责人": ["全队", "建模手", "数据手", "建模手", "编程手", "编程手", "论文手", "全队"],
})
workflow
"""
            ),
            code(
                r"""
roles = pd.DataFrame({
    "角色": ["队长/集成", "数据手", "建模手", "编程手", "论文手"],
    "主要职责": [
        "拆题、控进度、最终整合",
        "数据审计、清洗、变量说明",
        "假设、模型、算法路线",
        "代码实现、图表、结果表",
        "结构、表达、摘要和排版",
    ],
    "关键交付": [
        "任务看板与最终提交清单",
        "数据字典和清洗报告",
        "模型建立与求解方案",
        "可复现脚本和结果文件",
        "论文正文和图表解释",
    ],
})
roles.to_csv(OUTPUT_ROOT / "team_roles.csv", index=False, encoding="utf-8-sig")
roles
"""
            ),
            md("## 2. 课堂交付\n\n用上面的表格为一个历年题目建立自己的队伍分工表。"),
        ],
    },
    {
        "file": "lesson-02-python-data-structures.ipynb",
        "id": "lesson-02",
        "title": "第 2 讲：Python 数据结构与 DataFrame",
        "objective": "用 pandas 训练 Python 数据结构和 DataFrame，掌握比赛中最常用的数据容器。",
        "cells": [
            md("## 1. 构建混合类型数据表"),
            code(
                r"""
students = pd.DataFrame({
    "team": ["A", "A", "B", "B", "C", "C"],
    "role": pd.Categorical(["modeler", "coder", "writer", "coder", "leader", "modeler"]),
    "math_score": [86, 78, 91, 75, 88, 82],
    "coding_score": [70, 92, 65, 89, 80, 77],
    "available_hours": [18, 22, 15, 20, 24, 16],
})
students["total_score"] = students["math_score"] * 0.45 + students["coding_score"] * 0.35 + students["available_hours"] * 0.20
students
"""
            ),
            code(
                r"""
summary = students.groupby("team", observed=True).agg(
    members=("team", "size"),
    avg_score=("total_score", "mean"),
    max_hours=("available_hours", "max"),
)
summary.to_csv(OUTPUT_ROOT / "team_summary.csv", encoding="utf-8-sig")
summary
"""
            ),
            md("## 2. 课堂交付\n\n把自己的队伍成员信息整理成 DataFrame，并输出分工建议表。"),
        ],
    },
    {
        "file": "lesson-03-data-cleaning-visualization.ipynb",
        "id": "lesson-03",
        "title": "第 3 讲：数据导入、清洗与基础可视化",
        "objective": "用 Python 完成数据清洗流程，输出缺失值处理、描述统计和基础图表。",
        "cells": [
            code(
                r"""
n = 160
data = pd.DataFrame({
    "age": rng.integers(18, 75, n),
    "bmi": rng.normal(25, 4, n),
    "glucose": rng.normal(110, 22, n),
    "blood_pressure": rng.normal(78, 10, n),
    "risk_group": rng.choice(["low", "medium", "high"], n, p=[0.45, 0.35, 0.20]),
})
for col in ["bmi", "glucose", "blood_pressure"]:
    miss_idx = rng.choice(data.index, size=8, replace=False)
    data.loc[miss_idx, col] = np.nan
raw_path = OUTPUT_ROOT / "raw_health_data.csv"
data.to_csv(raw_path, index=False, encoding="utf-8-sig")
data.head()
"""
            ),
            code(
                r"""
clean = data.copy()
numeric_cols = clean.select_dtypes(include=np.number).columns
for col in numeric_cols:
    clean[col] = clean[col].fillna(clean[col].median())

summary = clean[numeric_cols].describe().T[["mean", "std", "min", "max"]]
summary.to_csv(OUTPUT_ROOT / "descriptive_summary.csv", encoding="utf-8-sig")
summary
"""
            ),
            code(
                r"""
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
clean["glucose"].hist(ax=axes[0], bins=18)
axes[0].set_title("Glucose distribution")
clean.boxplot(column="bmi", by="risk_group", ax=axes[1])
axes[1].set_title("BMI by risk group")
axes[1].figure.suptitle("")
axes[2].scatter(clean["age"], clean["glucose"], alpha=0.7)
axes[2].set_title("Age vs glucose")
for ax in axes:
    ax.set_xlabel("")
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "basic_visualization.png", dpi=160)
plt.show()
"""
            ),
        ],
    },
    {
        "file": "lesson-04-eda-visual-storytelling.ipynb",
        "id": "lesson-04",
        "title": "第 4 讲：探索性数据分析与可视化表达",
        "objective": "从图表中发现模式，并训练把图表转成建模假设和文字解释。",
        "cells": [
            code(
                r"""
n = 180
df = pd.DataFrame({
    "income": rng.normal(6000, 1200, n),
    "education_years": rng.normal(15, 2.2, n),
    "commute_time": rng.normal(42, 15, n),
    "satisfaction": rng.normal(70, 8, n),
})
df["satisfaction"] += 0.002 * df["income"] + 1.2 * (df["education_years"] - 15) - 0.18 * df["commute_time"]
df["commute_time"] = df["commute_time"].clip(lower=5)
df["satisfaction"] = df["satisfaction"].clip(lower=0, upper=100)
corr = df.corr(numeric_only=True)
corr.to_csv(OUTPUT_ROOT / "eda_correlation.csv", encoding="utf-8-sig")
corr
"""
            ),
            code(
                r"""
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
im = axes[0].imshow(corr, vmin=-1, vmax=1, cmap="coolwarm")
axes[0].set_xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
axes[0].set_yticks(range(len(corr.columns)), corr.columns)
axes[0].set_title("Correlation heatmap")
fig.colorbar(im, ax=axes[0], fraction=0.046)
axes[1].scatter(df["commute_time"], df["satisfaction"], alpha=0.7)
axes[1].set_title("Commute time vs satisfaction")
axes[1].set_xlabel("Commute time")
axes[1].set_ylabel("Satisfaction")
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "eda_story.png", dpi=160)
plt.show()
"""
            ),
            code(
                r"""
interpretation = pd.DataFrame({
    "图表": ["Correlation heatmap", "Commute scatter"],
    "观察": ["satisfaction 与 commute_time 呈负相关", "通勤时间越长，满意度整体越低"],
    "建模启发": ["后续模型应纳入 commute_time", "可以检验通勤时间的边际影响"],
})
interpretation.to_csv(OUTPUT_ROOT / "figure_interpretation.csv", index=False, encoding="utf-8-sig")
interpretation
"""
            ),
        ],
    },
    {
        "file": "lesson-05-regression-diagnostics.ipynb",
        "id": "lesson-05",
        "title": "第 5 讲：回归模型与拟合诊断",
        "objective": "用 scikit-learn 重构回归模型教学，输出系数、残差和拟合诊断。",
        "cells": [
            code(
                r"""
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

n = 220
X = pd.DataFrame({
    "age": rng.integers(18, 75, n),
    "bmi": rng.normal(25, 4, n),
    "exercise_hours": rng.normal(4, 1.5, n).clip(0, None),
})
y = 65 + 0.42 * X["age"] + 1.9 * X["bmi"] - 2.5 * X["exercise_hours"] + rng.normal(0, 8, n)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)
coef = pd.DataFrame({"feature": X.columns, "coefficient": model.coef_})
metrics = pd.DataFrame({"MAE": [mean_absolute_error(y_test, pred)], "R2": [r2_score(y_test, pred)]})
coef.to_csv(OUTPUT_ROOT / "regression_coefficients.csv", index=False, encoding="utf-8-sig")
metrics.to_csv(OUTPUT_ROOT / "regression_metrics.csv", index=False, encoding="utf-8-sig")
coef, metrics
"""
            ),
            code(
                r"""
residual = y_test - pred
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].scatter(y_test, pred, alpha=0.7)
axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
axes[0].set_title("Observed vs predicted")
axes[0].set_xlabel("Observed")
axes[0].set_ylabel("Predicted")
axes[1].scatter(pred, residual, alpha=0.7)
axes[1].axhline(0, color="r", linestyle="--")
axes[1].set_title("Residual diagnostics")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Residual")
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "regression_diagnostics.png", dpi=160)
plt.show()
"""
            ),
        ],
    },
    {
        "file": "lesson-06-clustering-pca.ipynb",
        "id": "lesson-06",
        "title": "第 6 讲：聚类分析与 PCA 降维",
        "objective": "用 K-means 和 PCA 训练无监督建模，输出聚类画像和降维图。",
        "cells": [
            code(
                r"""
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

n = 240
features = pd.DataFrame({
    "spending": rng.normal(500, 120, n),
    "visits": rng.normal(12, 4, n),
    "service_time": rng.normal(30, 8, n),
    "satisfaction": rng.normal(75, 10, n),
})
scaled = StandardScaler().fit_transform(features)
inertia = []
for k in range(2, 8):
    inertia.append(KMeans(n_clusters=k, random_state=42, n_init=10).fit(scaled).inertia_)
pd.DataFrame({"k": range(2, 8), "inertia": inertia}).to_csv(OUTPUT_ROOT / "k_selection.csv", index=False)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10).fit(scaled)
features["cluster"] = kmeans.labels_
profile = features.groupby("cluster").mean()
profile.to_csv(OUTPUT_ROOT / "cluster_profile.csv", encoding="utf-8-sig")
profile
"""
            ),
            code(
                r"""
pca = PCA(n_components=2, random_state=42)
score = pca.fit_transform(scaled)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(range(2, 8), inertia, marker="o")
axes[0].set_title("Elbow method")
axes[0].set_xlabel("k")
axes[0].set_ylabel("Inertia")
scatter = axes[1].scatter(score[:, 0], score[:, 1], c=features["cluster"], cmap="viridis", alpha=0.75)
axes[1].set_title("PCA view of clusters")
axes[1].set_xlabel("PC1")
axes[1].set_ylabel("PC2")
fig.colorbar(scatter, ax=axes[1])
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "clustering_pca.png", dpi=160)
plt.show()
print("Explained variance:", pca.explained_variance_ratio_)
"""
            ),
        ],
    },
    {
        "file": "lesson-07-evaluation-models.ipynb",
        "id": "lesson-07",
        "title": "第 7 讲：综合评价模型",
        "objective": "落成评价模型示例代码：指标标准化、熵权法、TOPSIS 和排名解释。",
        "cells": [
            code(
                r"""
alternatives = [f"方案{i}" for i in range(1, 7)]
X = pd.DataFrame({
    "成本": [72, 65, 80, 68, 75, 70],
    "效率": [88, 82, 91, 85, 89, 83],
    "可靠性": [0.92, 0.88, 0.95, 0.90, 0.93, 0.86],
    "建设周期": [14, 10, 18, 12, 16, 11],
}, index=alternatives)
directions = {"成本": "min", "效率": "max", "可靠性": "max", "建设周期": "min"}

def minmax_normalize(df, directions):
    out = pd.DataFrame(index=df.index)
    for col in df.columns:
        cmin, cmax = df[col].min(), df[col].max()
        if directions[col] == "max":
            out[col] = (df[col] - cmin) / (cmax - cmin)
        else:
            out[col] = (cmax - df[col]) / (cmax - cmin)
    return out

norm = minmax_normalize(X, directions)
P = norm / norm.sum(axis=0)
eps = 1e-12
entropy = -(P * np.log(P + eps)).sum(axis=0) / np.log(len(norm))
weights = (1 - entropy) / (1 - entropy).sum()
weights.to_csv(OUTPUT_ROOT / "entropy_weights.csv", encoding="utf-8-sig")
weights
"""
            ),
            code(
                r"""
weighted = norm * weights
positive = weighted.max(axis=0)
negative = weighted.min(axis=0)
d_pos = np.sqrt(((weighted - positive) ** 2).sum(axis=1))
d_neg = np.sqrt(((weighted - negative) ** 2).sum(axis=1))
score = d_neg / (d_pos + d_neg)
ranking = pd.DataFrame({"TOPSIS_score": score}).sort_values("TOPSIS_score", ascending=False)
ranking["rank"] = range(1, len(ranking) + 1)
ranking.to_csv(OUTPUT_ROOT / "topsis_ranking.csv", encoding="utf-8-sig")
ranking
"""
            ),
            code(
                r"""
fig, ax = plt.subplots(figsize=(8, 4))
ranking["TOPSIS_score"].sort_values().plot(kind="barh", ax=ax)
ax.set_title("TOPSIS comprehensive ranking")
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "topsis_ranking.png", dpi=160)
plt.show()
"""
            ),
        ],
    },
    {
        "file": "lesson-08-forecasting-models.ipynb",
        "id": "lesson-08",
        "title": "第 8 讲：预测模型基础",
        "objective": "落成预测模型示例代码：趋势外推、回归预测和 GM(1,1) 灰色预测。",
        "cells": [
            code(
                r"""
from sklearn.metrics import mean_absolute_percentage_error

t = np.arange(1, 37)
series = pd.Series(80 + 2.2 * t + 8 * np.sin(t / 3) + rng.normal(0, 3, len(t)), index=t, name="demand")
train = series.iloc[:28]
test = series.iloc[28:]

coef = np.polyfit(train.index, train.values, deg=1)
linear_pred = pd.Series(np.polyval(coef, test.index), index=test.index)
rolling_pred = pd.Series([train.tail(4).mean()] * len(test), index=test.index)

def gm11_forecast(x0, steps):
    x0 = np.array(x0, dtype=float)
    x1 = np.cumsum(x0)
    z1 = 0.5 * (x1[1:] + x1[:-1])
    B = np.column_stack([-z1, np.ones(len(z1))])
    Y = x0[1:]
    a, b = np.linalg.lstsq(B, Y, rcond=None)[0]
    def x1_hat(k):
        return (x0[0] - b / a) * np.exp(-a * k) + b / a
    x_hat = np.array([x1_hat(k) - x1_hat(k - 1) for k in range(1, len(x0) + steps)])
    return x_hat[-steps:]

gm_pred = pd.Series(gm11_forecast(train.values, len(test)), index=test.index)
metrics = pd.DataFrame({
    "model": ["linear_trend", "rolling_mean", "GM11"],
    "MAPE": [
        mean_absolute_percentage_error(test, linear_pred),
        mean_absolute_percentage_error(test, rolling_pred),
        mean_absolute_percentage_error(test, gm_pred),
    ],
})
metrics.to_csv(OUTPUT_ROOT / "forecast_metrics.csv", index=False, encoding="utf-8-sig")
metrics
"""
            ),
            code(
                r"""
fig, ax = plt.subplots(figsize=(9, 5))
series.plot(ax=ax, label="observed")
linear_pred.plot(ax=ax, label="linear trend")
rolling_pred.plot(ax=ax, label="rolling mean")
gm_pred.plot(ax=ax, label="GM(1,1)")
ax.axvline(test.index[0], color="gray", linestyle="--", label="test start")
ax.set_title("Forecasting model comparison")
ax.legend()
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "forecast_comparison.png", dpi=160)
plt.show()
"""
            ),
        ],
    },
    {
        "file": "lesson-09-classification-models.ipynb",
        "id": "lesson-09",
        "title": "第 9 讲：分类模型与机器学习入门",
        "objective": "落成分类模型示例代码：训练/测试划分、逻辑回归、决策树和混淆矩阵。",
        "cells": [
            code(
                r"""
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

X_arr, y = make_classification(
    n_samples=320, n_features=5, n_informative=3, n_redundant=1,
    weights=[0.62, 0.38], random_state=42
)
X = pd.DataFrame(X_arr, columns=[f"x{i}" for i in range(1, 6)])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
models = {
    "logistic": LogisticRegression(max_iter=1000),
    "decision_tree": DecisionTreeClassifier(max_depth=4, random_state=42),
}
rows = []
for name, clf in models.items():
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    rows.append({"model": name, "accuracy": accuracy_score(y_test, pred), "recall": recall_score(y_test, pred)})
metrics = pd.DataFrame(rows)
metrics.to_csv(OUTPUT_ROOT / "classification_metrics.csv", index=False)
metrics
"""
            ),
            code(
                r"""
best = DecisionTreeClassifier(max_depth=4, random_state=42).fit(X_train, y_train)
pred = best.predict(X_test)
cm = confusion_matrix(y_test, pred)
pd.DataFrame(cm, index=["actual_0", "actual_1"], columns=["pred_0", "pred_1"]).to_csv(OUTPUT_ROOT / "confusion_matrix.csv")
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues")
plt.title("Decision tree confusion matrix")
plt.tight_layout()
plt.savefig(OUTPUT_ROOT / "confusion_matrix.png", dpi=160)
plt.show()
"""
            ),
        ],
    },
    {
        "file": "lesson-10-linear-programming.ipynb",
        "id": "lesson-10",
        "title": "第 10 讲：线性规划与资源分配",
        "objective": "用 scipy.optimize.linprog 重构线性规划教学，输出最优生产方案和可行域图。",
        "cells": [
            code(
                r"""
from scipy.optimize import linprog

# maximize 3*x1 + 5*x2 -> minimize negative profit
c = [-3, -5]
A = [[2, 1], [1, 3], [0, 1]]
b = [100, 150, 40]
bounds = [(0, None), (0, None)]
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
solution = pd.DataFrame({
    "product": ["A", "B"],
    "quantity": res.x,
})
summary = pd.DataFrame({"max_profit": [-res.fun], "success": [res.success], "message": [res.message]})
solution.to_csv(OUTPUT_ROOT / "lp_solution.csv", index=False, encoding="utf-8-sig")
summary.to_csv(OUTPUT_ROOT / "lp_summary.csv", index=False, encoding="utf-8-sig")
solution, summary
"""
            ),
            code(
                r"""
x = np.linspace(0, 80, 300)
y1 = 100 - 2*x
y2 = (150 - x) / 3
y3 = np.full_like(x, 40)
y = np.minimum.reduce([y1, y2, y3])
y = np.maximum(y, 0)
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, y1, label="2x1 + x2 <= 100")
ax.plot(x, y2, label="x1 + 3x2 <= 150")
ax.plot(x, y3, label="x2 <= 40")
ax.fill_between(x, 0, y, where=y>=0, alpha=0.25)
ax.scatter(res.x[0], res.x[1], color="red", s=80, label="optimum")
ax.set_xlim(0, 80)
ax.set_ylim(0, 60)
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_title("Linear programming feasible region")
ax.legend()
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "lp_feasible_region.png", dpi=160)
plt.show()
"""
            ),
        ],
    },
    {
        "file": "lesson-11-integer-multiobjective.ipynb",
        "id": "lesson-11",
        "title": "第 11 讲：整数规划、0-1 规划与多目标优化",
        "objective": "用枚举法实现小规模 0-1 规划，并展示多目标权衡。",
        "cells": [
            code(
                r"""
projects = pd.DataFrame({
    "project": ["P1", "P2", "P3", "P4", "P5"],
    "benefit": [16, 22, 18, 12, 20],
    "cost": [8, 11, 9, 6, 10],
    "risk": [5, 7, 4, 3, 6],
})
budget = 24
rows = []
for bits in itertools.product([0, 1], repeat=len(projects)):
    chosen = np.array(bits)
    cost = (chosen * projects["cost"]).sum()
    if cost <= budget:
        rows.append({
            "selection": "".join(map(str, bits)),
            "benefit": (chosen * projects["benefit"]).sum(),
            "cost": cost,
            "risk": (chosen * projects["risk"]).sum(),
        })
solutions = pd.DataFrame(rows)
best = solutions.sort_values(["benefit", "risk"], ascending=[False, True]).head(1)
solutions.to_csv(OUTPUT_ROOT / "binary_solutions.csv", index=False)
best
"""
            ),
            code(
                r"""
weights = np.linspace(0, 1, 21)
frontier = []
for w in weights:
    tmp = solutions.copy()
    tmp["score"] = w * tmp["benefit"] - (1 - w) * tmp["risk"]
    row = tmp.sort_values("score", ascending=False).iloc[0]
    frontier.append({"benefit_weight": w, "selection": row["selection"], "benefit": row["benefit"], "risk": row["risk"]})
frontier = pd.DataFrame(frontier)
frontier.to_csv(OUTPUT_ROOT / "multiobjective_tradeoff.csv", index=False)
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(solutions["risk"], solutions["benefit"], alpha=0.5, label="feasible")
ax.plot(frontier["risk"], frontier["benefit"], "r-o", label="weighted choices")
ax.set_xlabel("Risk")
ax.set_ylabel("Benefit")
ax.set_title("Benefit-risk tradeoff")
ax.legend()
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "multiobjective_tradeoff.png", dpi=160)
frontier.head()
"""
            ),
        ],
    },
    {
        "file": "lesson-12-graph-network-models.ipynb",
        "id": "lesson-12",
        "title": "第 12 讲：图论与网络模型",
        "objective": "用 networkx 落成最短路、最大流和网络中心性示例。",
        "cells": [
            code(
                r"""
import networkx as nx

edges = [
    ("A", "B", 4), ("A", "C", 2), ("B", "D", 5), ("C", "D", 8),
    ("C", "E", 10), ("D", "E", 2), ("D", "F", 6), ("E", "F", 3),
]
G = nx.Graph()
G.add_weighted_edges_from(edges)
path = nx.shortest_path(G, "A", "F", weight="weight")
dist = nx.shortest_path_length(G, "A", "F", weight="weight")
centrality = pd.Series(nx.betweenness_centrality(G, weight="weight"), name="betweenness")
centrality.to_csv(OUTPUT_ROOT / "node_centrality.csv", encoding="utf-8-sig")
print("Shortest path:", path, "distance:", dist)
centrality.sort_values(ascending=False)
"""
            ),
            code(
                r"""
pos = nx.spring_layout(G, seed=42)
fig, ax = plt.subplots(figsize=(7, 5))
nx.draw_networkx(G, pos=pos, ax=ax, node_color="lightblue", node_size=900)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
ax.set_title("Weighted network")
ax.axis("off")
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "weighted_network.png", dpi=160)
plt.show()
"""
            ),
            code(
                r"""
DG = nx.DiGraph()
DG.add_edge("S", "A", capacity=10)
DG.add_edge("S", "B", capacity=8)
DG.add_edge("A", "C", capacity=5)
DG.add_edge("A", "D", capacity=6)
DG.add_edge("B", "C", capacity=4)
DG.add_edge("B", "D", capacity=4)
DG.add_edge("C", "T", capacity=8)
DG.add_edge("D", "T", capacity=9)
flow_value, flow_dict = nx.maximum_flow(DG, "S", "T")
pd.DataFrame(flow_dict).fillna(0).to_csv(OUTPUT_ROOT / "max_flow.csv", encoding="utf-8-sig")
flow_value, flow_dict
"""
            ),
        ],
    },
    {
        "file": "lesson-13-monte-carlo-simulation.ipynb",
        "id": "lesson-13",
        "title": "第 13 讲：仿真模型与蒙特卡洛",
        "objective": "用蒙特卡洛处理不确定性，输出结果分布、置信区间和决策建议。",
        "cells": [
            code(
                r"""
def simulate_inventory(order_qty, n_sim=5000):
    demand = rng.normal(100, 18, n_sim).clip(0, None)
    price, cost, salvage, shortage_penalty = 12, 7, 3, 2
    sales = np.minimum(order_qty, demand)
    leftover = np.maximum(order_qty - demand, 0)
    shortage = np.maximum(demand - order_qty, 0)
    profit = price * sales + salvage * leftover - cost * order_qty - shortage_penalty * shortage
    return profit

quantities = np.arange(60, 151, 5)
rows = []
for q in quantities:
    profit = simulate_inventory(q)
    rows.append({
        "order_qty": q,
        "mean_profit": profit.mean(),
        "p05": np.percentile(profit, 5),
        "p95": np.percentile(profit, 95),
    })
result = pd.DataFrame(rows)
best = result.loc[result["mean_profit"].idxmax()]
result.to_csv(OUTPUT_ROOT / "monte_carlo_inventory.csv", index=False)
best
"""
            ),
            code(
                r"""
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(result["order_qty"], result["mean_profit"], marker="o", label="mean profit")
ax.fill_between(result["order_qty"], result["p05"], result["p95"], alpha=0.2, label="90% interval")
ax.axvline(best["order_qty"], color="red", linestyle="--", label="best")
ax.set_xlabel("Order quantity")
ax.set_ylabel("Profit")
ax.set_title("Monte Carlo inventory decision")
ax.legend()
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "monte_carlo_inventory.png", dpi=160)
plt.show()
"""
            ),
        ],
    },
    {
        "file": "lesson-14-sensitivity-robustness.ipynb",
        "id": "lesson-14",
        "title": "第 14 讲：敏感性、鲁棒性与模型检验",
        "objective": "对模型关键参数做扰动，检查结论是否稳定。",
        "cells": [
            code(
                r"""
from scipy.optimize import linprog

profits = np.arange(3.0, 6.1, 0.25)
rows = []
for p2 in profits:
    res = linprog([-3, -p2], A_ub=[[2, 1], [1, 3], [0, 1]], b_ub=[100, 150, 40], bounds=[(0, None), (0, None)], method="highs")
    rows.append({"profit_B": p2, "x1": res.x[0], "x2": res.x[1], "objective": -res.fun})
sensitivity = pd.DataFrame(rows)
sensitivity.to_csv(OUTPUT_ROOT / "lp_sensitivity.csv", index=False)
sensitivity.head()
"""
            ),
            code(
                r"""
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(sensitivity["profit_B"], sensitivity["x1"], label="x1")
axes[0].plot(sensitivity["profit_B"], sensitivity["x2"], label="x2")
axes[0].set_title("Decision variables under profit_B changes")
axes[0].legend()
axes[1].plot(sensitivity["profit_B"], sensitivity["objective"], color="darkgreen")
axes[1].set_title("Objective sensitivity")
for ax in axes:
    ax.set_xlabel("profit_B")
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "lp_sensitivity.png", dpi=160)
plt.show()
"""
            ),
            code(
                r"""
stable_choice = sensitivity[["x1", "x2"]].round(3).drop_duplicates().shape[0] <= 3
pd.DataFrame({"结论": ["模型在利润参数变化下的解结构是否稳定"], "是否稳定": [stable_choice]}).to_csv(
    OUTPUT_ROOT / "robustness_statement.csv", index=False, encoding="utf-8-sig"
)
stable_choice
"""
            ),
        ],
    },
    {
        "file": "lesson-15-paper-structure-latex.ipynb",
        "id": "lesson-15",
        "title": "第 15 讲：论文结构、数学表达与 LaTeX",
        "objective": "用 Python 生成论文模型段落骨架、符号表和 LaTeX 公式片段。",
        "cells": [
            code(
                r"""
symbols = pd.DataFrame({
    "符号": ["x_i", "c_i", "a_{ij}", "b_j", "Z"],
    "含义": ["第 i 个方案的决策变量", "第 i 个方案收益", "资源 j 的消耗系数", "资源 j 的上限", "总收益"],
    "单位": ["-", "元", "单位", "单位", "元"],
})
symbols.to_csv(OUTPUT_ROOT / "symbol_table.csv", index=False, encoding="utf-8-sig")
markdown_table = "| 符号 | 含义 | 单位 |\n| --- | --- | --- |\n" + "\n".join(
    f"| {row['符号']} | {row['含义']} | {row['单位']} |" for _, row in symbols.iterrows()
)
(OUTPUT_ROOT / "symbol_table.md").write_text(markdown_table, encoding="utf-8")
symbols
"""
            ),
            code(
                r"""
latex_model = r'''
Maximize:
\[
Z=\sum_{i=1}^{n} c_i x_i
\]

Subject to:
\[
\sum_{i=1}^{n} a_{ij}x_i \le b_j,\quad j=1,2,\ldots,m
\]
\[
x_i \ge 0,\quad i=1,2,\ldots,n
\]
'''
(OUTPUT_ROOT / "model_latex_snippet.tex").write_text(latex_model, encoding="utf-8")
print(latex_model)
"""
            ),
            code(
                r"""
paragraph = "本模型将每个候选方案的实施规模定义为决策变量，以总收益最大化为目标函数，并将资源容量、时间预算和非负性要求作为约束条件。该结构能够直接对应资源分配类问题，并为后续灵敏度分析提供清晰的参数入口。"
(OUTPUT_ROOT / "model_description.md").write_text(paragraph, encoding="utf-8")
paragraph
"""
            ),
        ],
    },
    {
        "file": "lesson-16-result-narrative.ipynb",
        "id": "lesson-16",
        "title": "第 16 讲：图表叙事与结果解释",
        "objective": "把图表、指标和结论连接起来，生成论文式结果解释模板。",
        "cells": [
            code(
                r"""
result_table = pd.DataFrame({
    "模型": ["线性回归", "灰色预测", "TOPSIS评价"],
    "关键输出": ["R2=0.82", "MAPE=6.4%", "方案3排名第一"],
    "支持图表": ["拟合诊断图", "预测曲线图", "综合排名条形图"],
    "结论": ["变量解释能力较强", "短期预测误差可接受", "方案3综合表现最好"],
})
result_table.to_csv(OUTPUT_ROOT / "result_narrative_table.csv", index=False, encoding="utf-8-sig")
result_table
"""
            ),
            code(
                r"""
templates = []
for _, row in result_table.iterrows():
    templates.append(
        f"对于{row['模型']}，{row['支持图表']}显示{row['关键输出']}。"
        f"这说明{row['结论']}，因此该结果可以支撑对应子问题的模型结论。"
    )
report = "\n\n".join(templates)
(OUTPUT_ROOT / "figure_table_narrative.md").write_text(report, encoding="utf-8")
print(report)
"""
            ),
        ],
    },
    {
        "file": "lesson-17-mini-contest-modeling.ipynb",
        "id": "lesson-17",
        "title": "第 17 讲：综合模拟赛 I：读题、建模与代码",
        "objective": "用一个综合小题串起数据处理、评价模型和优化模型，产出初版结果。",
        "cells": [
            code(
                r"""
cities = pd.DataFrame({
    "city": [f"C{i}" for i in range(1, 9)],
    "demand": rng.integers(80, 180, 8),
    "cost": rng.integers(40, 90, 8),
    "accessibility": rng.uniform(0.5, 0.95, 8),
    "risk": rng.uniform(0.05, 0.30, 8),
})
directions = {"demand": "max", "cost": "min", "accessibility": "max", "risk": "min"}
def normalize(df, directions):
    out = pd.DataFrame(index=df.index)
    for col, direction in directions.items():
        if direction == "max":
            out[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
        else:
            out[col] = (df[col].max() - df[col]) / (df[col].max() - df[col].min())
    return out
norm = normalize(cities.set_index("city"), directions)
weights = pd.Series({"demand": 0.35, "cost": 0.25, "accessibility": 0.25, "risk": 0.15})
cities["score"] = (norm * weights).sum(axis=1).values
cities.sort_values("score", ascending=False).to_csv(OUTPUT_ROOT / "site_scores.csv", index=False, encoding="utf-8-sig")
cities.sort_values("score", ascending=False)
"""
            ),
            code(
                r"""
budget = 220
best = None
for bits in itertools.product([0, 1], repeat=len(cities)):
    chosen = np.array(bits)
    total_cost = (chosen * cities["cost"]).sum()
    if total_cost <= budget and chosen.sum() > 0:
        total_score = (chosen * cities["score"]).sum()
        if best is None or total_score > best["total_score"]:
            best = {"selection": bits, "total_cost": total_cost, "total_score": total_score}
selected = cities.loc[np.array(best["selection"]) == 1, ["city", "cost", "score"]]
selected.to_csv(OUTPUT_ROOT / "selected_sites.csv", index=False, encoding="utf-8-sig")
best, selected
"""
            ),
            code(
                r"""
fig, ax = plt.subplots(figsize=(8, 4))
cities.sort_values("score").plot.barh(x="city", y="score", ax=ax, legend=False)
ax.set_title("Mini contest site evaluation")
fig.tight_layout()
fig.savefig(OUTPUT_ROOT / "mini_contest_scores.png", dpi=160)
plt.show()
"""
            ),
        ],
    },
    {
        "file": "lesson-18-mini-contest-report-review.ipynb",
        "id": "lesson-18",
        "title": "第 18 讲：综合模拟赛 II：论文打磨与复盘",
        "objective": "把综合模拟赛结果整理成短报告、检查清单和复盘表。",
        "cells": [
            code(
                r"""
sections = pd.DataFrame({
    "章节": ["摘要", "问题分析", "模型假设", "模型建立", "模型求解", "模型检验", "结论"],
    "检查点": [
        "是否交代问题、方法和关键结果",
        "是否逐个子问题分析",
        "假设是否合理且不过度",
        "变量、目标、约束是否完整",
        "结果是否有图表和代码支撑",
        "是否包含敏感性或鲁棒性分析",
        "是否回到题目目标",
    ],
})
sections.to_csv(OUTPUT_ROOT / "paper_checklist.csv", index=False, encoding="utf-8-sig")
sections
"""
            ),
            code(
                r"""
mini_report = "\n".join([
    "# 模拟赛短报告骨架",
    "",
    "## 摘要",
    "本文围绕资源有限条件下的站点选择问题，建立综合评价与预算约束优化模型。",
    "",
    "## 模型方法",
    "首先对需求、成本、可达性和风险指标进行标准化处理；随后使用加权综合评价得到候选站点评分；最后在预算约束下枚举可行组合，选择总评分最高的站点集合。",
    "",
    "## 结果解释",
    "最终方案应同时报告被选择站点、总成本、综合得分和风险解释，并配套排名图或选择表。",
    "",
    "## 复盘",
    "后续应补充权重敏感性分析，并比较不同预算水平下的方案变化。",
])
(OUTPUT_ROOT / "mini_report.md").write_text(mini_report, encoding="utf-8")
print(mini_report)
"""
            ),
            code(
                r"""
review = pd.DataFrame({
    "维度": ["代码复现", "图表质量", "模型解释", "论文结构", "团队协作"],
    "评分1-5": [4, 4, 3, 4, 4],
    "改进动作": [
        "固定随机种子并保存中间表",
        "统一图表标题和单位",
        "补充敏感性分析",
        "将结果放到对应子问题下",
        "提前确定最终整合负责人",
    ],
})
review.to_csv(OUTPUT_ROOT / "team_review.csv", index=False, encoding="utf-8-sig")
review
"""
            ),
        ],
    },
]


def main() -> None:
    NOTEBOOK_DIR.mkdir(parents=True, exist_ok=True)
    for item in LESSONS:
        nb = notebook(item["title"], item["id"], item["objective"], item["cells"])
        path = NOTEBOOK_DIR / item["file"]
        nbf.write(nb, path)
        print(f"wrote {path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
