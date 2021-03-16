## 一、拉普拉斯变换

### 1. 傅里叶变换

$$
    \begin{array}{l}
        f(x) = \int_{-\infty}^{\infty} c(\omega) e^{i \omega x} \mathrm{d} \omega\\
        c(\omega) = \frac{1}{ 2 \pi} \int_{-\infty}^{\infty} f(x) e^{-i \omega x} \mathrm{d}x
    \end{array} \tag{1.1}
$$

**局限性：**
> &emsp;&emsp;当$x \rightarrow \infin, f(x) \rightarrow \infin$时，傅里叶变换失效。

### 2. 拉普拉斯变换

&emsp;&emsp; 引入一个修正数: $e^{- \delta x}, \delta \ge 0$，将$f(x)$从$\infin$拉回有限，进而继续使用傅里叶变换进行处理。

$$
    \begin{array}{l}
        F(\omega) = \int_{0}^{+\infty} f(x) e^{- \delta x} e^{-i \omega x} \mathrm{d}x
    \end{array} \tag{1.2}
$$
> **注**: 积分范围是$0 \rightarrow + \infin$；因为当$x$为负号时，$e^{- \delta x}$就将原来的$f(x)$继续放大了。

其中$e^{- \delta x} e^{- i \omega x} = e^{- (\delta + i \omega)x}$，得到拉普拉斯算子$s$

$$
s = \delta + iw , \delta \ge 0 \tag{1.3}
$$

&emsp;&emsp;引入拉普拉斯算子，获得拉普拉斯变换:
$$
\mathscr{L}[ f(t) ] = \int_{0}^{+\infty} f(t) e^{-st} \mathrm{d}t \tag{1.4}
$$

## 二、拉普拉斯变换性质

### 1. 线性叠加定理
$$
\mathscr{L}[a f(t) + b g(t)] = a \mathscr{L}[f(t)] + b \mathscr{L}[g(t)] \tag{2.1}
$$

### 2. 卷积定理

$$
\mathscr{L}[f(t) * g(t)] = \mathscr{L}[f(t)] \mathscr{L}[g(t)] \tag{2.2}
$$

### 3. 其他公式
&emsp;&emsp;[Laplace Transform(拉普拉斯变换)](https://zhuanlan.zhihu.com/p/152647974)