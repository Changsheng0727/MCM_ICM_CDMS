# 美赛培训使用的代码
- 目前更新到第二讲
- 请勿转发
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
