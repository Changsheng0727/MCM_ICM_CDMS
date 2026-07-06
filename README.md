# 美赛培训使用的代码
- 目前仓库包含第 2-4 讲相关 MATLAB Live Script
- 请勿转发

## 培训项目计划

本仓库已经补充 GitHub 版培训计划，入口见：

- [docs/training-plan/README.md](docs/training-plan/README.md)
- [18 讲课程大纲](docs/training-plan/06-18-lesson-syllabus.md)

该计划把当前 MATLAB Live Script 课件整理为四条建设线：

- 授课交付线
- 建模方法线
- MATLAB 代码与复现线
- 学员作业与评估线

并已经扩展为 18 讲课程体系，提供每讲课程设计、8 周建设节奏、每日推进记录模板、周复盘模板、单讲课程设计模板和学员作业模板。

## 本周关键词：线性模型
The  linear model is given by

$$
y_i=\beta_0+\beta_1x_i+\epsilon_i
$$

## 最小二乘法
>这里以一元线性模型为例

$$
Q\left(\beta_0, \beta_1\right)=\sum_{i=1}^n\left(y_i-\beta_0-\beta_1 x_i\right)^2 .
$$


Define

$$
\begin{gathered}
\ell_{x x}=\sum_{i=1}^n\left(x_i-\bar{x}\right)^2, \\
\ell_{y y}=\sum_{i=1}^n\left(y_i-\bar{y}\right)^2, \\
\ell_{x y}=\sum_{i=1}^n\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right) .
\end{gathered}
$$

We thus have

$$
\hat{\beta}_1=\frac{\sum_{i=1}^n\left(y_i-\bar{y}\right)\left(x_i-\bar{x}\right)}{\sum_{i=1}^n\left(x_i-\bar{x}\right)\left(x_i-\bar{x}\right)}=\frac{\ell_{x y}}{\ell_{x x}}=\frac{1}{\ell_{x x}} \sum_{i=1}^n\left(x_i-\bar{x}\right) y_i .
$$
