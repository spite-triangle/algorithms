<h1>卡尔曼滤波</h1>

***
[toc]
***

## 一、卡尔曼滤波思想

&emsp;&emsp;将带有噪声的实际测量值$m_k$与模型估计值$x_k$进行数据融合，从而获得更精确的估计值。**核心是对$k_k$进行求解**。

$$
\begin{aligned}
    x_k &= x_{k-1} + k_k (m_k - x_{k - 1}) \\
        &= k_k m_k + (1 - k_k) x_{k - 1} \\
    k_k &= \frac{e_{EST_{k - 1}}}{e_{EST_{k - 1}} + e_{MEA_{k}}}
\end{aligned}
\tag{1.1}
$$

&emsp;&emsp;卡尔曼滤波只涉及：上一次的估计值$x_{k-1}$；当前测量值$m_k$；卡尔曼滤波系数$k_k$。$k_k$由上一次估计误差$e_{EST_{k - 1}}$与当前的测量误差$e_{MEA_{k - 1}}$组成。

$$
\begin{array}{l}
    e_{EST} = 估计值 - 真实值 \\
    e_{MEA} = 测量值 - 真实值 \\
\end{array}
\tag{1.2}
$$

## 二、前提概念

### 1. 数据融合

**目标**：将两组测量数据合并，得到一个方差更小更精确的数据：$\delta$ 小于 $\delta_1$ 和 $\delta_2$

$$
\left \{
\begin{aligned}
    m_1(z_1,\delta_1) \\
    m_2(z_2,\delta_2) \\
\end{aligned}
=>
m(z,\delta)
\right .
\tag{2.1}
$$

**步骤**：
> 1. 引用卡尔曼思路：令$z = z_1 + k(z_2 - z_1)$；
> 1. 将上式进行方差计算：$\delta^2(z) = var(z_1 + k(z_2 - z_1)) = (1 - k)^2 \delta_1^2 + (k \delta_2)^2$
> 1. 求令$\delta$最小的k：$\frac{\mathbf{d} \delta^2}{\mathbf{d} k} = 0$；计算出k值。

### 2. 协方差矩阵

**概念**：

1. 方差(variance)：体现的是数据偏离期望值(均值)的程度

    $$
    \delta^2_x = \frac{1}{n}[(x_1 - \overline{x})^2 + (x_2 - \overline{x})^2 + \dotsm +(x_n - \overline{x})^2 ]
    \tag{2.2}
    $$

1. 协方差(Covariance)：衡量两个变量的总体误差
    $$
    \delta_{xy}^2 = \frac{1}{n}[(x_1 - \overline{x})(y_2 - \overline{y}) + \dotsm +(x_n - \overline{x})(y_n - \overline{y}) ]
    \tag{2.3}
    $$

1. 协方差矩阵：囊括了多个变量的方差和协方差
    $$
    \begin{array}{r}
    x \qquad y \qquad z \qquad \\
    \begin{array}{l}
        x \\
        y \\
        z \\
    \end{array}
    \begin{bmatrix}
        \delta_x^2 & \delta_{xy}^2 & \delta_{xz}^2 \\
        \delta_{yx}^2 &  \delta_y^2 & \delta_{yz}^2 \\
        \delta_{zx}^2 & \delta_{zy}^2 & \delta_z^2
    \end{bmatrix}
    \end{array}
    \tag{2.4}
    $$

**计算**：以三个变量为例
> 1. 过度矩阵
    $$
        a =
        \begin{bmatrix}
            x_1 & y_1 & z_1 \\
            x_2 & y_2 & z_2 \\
            x_3 & y_3 & z_3 
        \end{bmatrix}
        - \frac{1}{3}
        \begin{bmatrix}
            1 & 1 & 1 \\    
            1 & 1 & 1 \\    
            1 & 1 & 1 \\    
        \end{bmatrix}
        \begin{bmatrix}
            x_1 & y_1 & z_1 \\
            x_2 & y_2 & z_2 \\
            x_3 & y_3 & z_3 
        \end{bmatrix}
    $$
> 1. 协方差矩阵：$p = \frac{1}{3}a^Ta$


### 3. 离散的状态方程

&emsp;&emsp;**卡尔曼滤波只能应用于线性模型**。
$$
\left \{
\begin{aligned}
    x_k &= A x_{k-1} + B u_k + w_{k} \\
    m_k &= H x_k + v_k
\end{aligned}
\right .
\tag{2.5}
$$

$w_{k}$为数学模型的噪声，满足$P(w) \sim (0,Q)$；$v_{k}$为数学模型的噪声，满足$P(v) \sim (0,R)$。**其中Q与R为协方差矩阵**。

### 4. 先验与后验

以状态方程为例：

1. 先验：由于$w_k$不可测，通过模型能计算的值是先验值$\hat{x}_k^-$。
$$
\hat{x}_k^- = A \hat{x}_{k-1} + B u_k
\tag{2.6}
$$

1. 后验：最终通过卡尔曼滤波估计到的值$\hat{x}_k$

## 三、卡尔曼滤波公式

### 1. 前提
> * 未知误差，均满足正太分布；
> * 问题模型为线性的。

### 2. 推导

1）问题描述

先验估计值：$\hat{x}_k^- = A \hat{x}_{k-1} + B u_k$
测量估计值：$\hat{x}_E=H^{-1}z_k$
后验估计值：$\hat{x}_k = \hat{x}_k^- + G(H^{-1}z_k - \hat{x}_k^-)$；令$G = k_kH$，得$\hat{x}_k = \hat{x}_k^- + k_k(z_k - H\hat{x}_k^-)$
目标：求出$k_k$实现$e_k^- = \hat{x}_k - x_k => 0$

> **注意**
> &emsp;&emsp;**对于后验估计：**$\hat{x}_k = \hat{x}_k^- + k_k(z_k - \hat{z}_k^-)$, $\hat{z}_k^- = H\hat{x}_k^-$ **是通过过测量值的偏差进行数据修正的。因此就能进行模型的参数估计（参数辨识），用于外推预测。**

2）目标具体化

假设$e_k$满足正太分布：$P(e) \sim (0,P_e)$。
问题的目标是让$e_k \rightarrow 0$。**根据正太分布假设，就是要 $tr(P_e)$最小**。
$$
tr(P_e) = \delta_{e1}^2 + \delta_{e2}^2 + \dotsm
\tag{3.1}
$$

3）计算 $P_{ek} = E(ee^T)$
$$
\begin{aligned}
P_{ek} &= (P_{ek}^- - k_k H P_{ek}^-)(I -  H^T k_k^T) + k_k R k_k^T \\
&带入后面的 k_k \\
       &= P_{ek}^- - k_k H P_{ek}^-
\end{aligned}
\tag{3.2}
$$

4）计算 $\frac{\mathbf{d}tr(P_{ek})}{\mathbf{d}k_k} = 0$

$$k_k = \frac{P_{ek}^-H^T}{HP_{ek}^-H^T + R} \tag{3.3}$$

5）计算$P_{ek}^- = E(e_k^-e_k^{-T})$
$$
P_{ek}^- = A P_{e \ k-1}A^T + Q \tag{3.4}
$$

### 3. 卡尔曼滤波流程

> **预测部分**:
> * 先验估计值： $\hat{x}_k^- = A \hat{x}_{k-1} + B u_k$
> * 先验估计协方差：$P_{ek}^- = A P_{e \ k-1}A^T + Q$
> 
> **校正部分**：
> * 卡尔曼系数：$k_k = \frac{P_{ek}^-H^T}{HP_{ek}^-H^T + R}$
> * 后验估计值：$\hat{x}_k = \hat{x}_k^- + k_k(z_k - H\hat{x}_k^-)$
> * 更新误差协方差：$P_{ek} = P_{ek}^- - k_k H P_{ek}^-$

## 参考
> [卡尔曼滤波器](https://www.bilibili.com/video/BV1ez4y1X7eR)