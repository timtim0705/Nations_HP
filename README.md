PyCGE and Nations' HP Evaluation
==================================

*Objectives*
- Develop a `Python` based optimization modeling workflow for solving linear & nonlinear programming problems, e.g., `CGE`;<br>
- Provide a method to evaluate gains and losses as a single value for policy simulations. 


*Contents*
>[Py-IO model](#py-io-model)
>>[IO Model](#io-model)<br>
>>[A Python Based IO Model Simulation](#a-python-based-io-model-simulation)

>[PyCGE Workflow](#pycge-workflow)
>>[A Python Based CGE Model](#a-python-based-cge-model)

>[Nation Utility Function](#nation-utility-function)
>>[Economic Interests](#economic-interests)<br>
>>[Political Interests](#political-interests)

>[HP Function](#hp-function)

--------------

### Py-IO model

#### IO Model
Input-Output table represents the ecomony in a matrix form. Here, a single nation IO table from National Bureau of Statistics of China is introduced to model the relationship between input and output among 153 industries. 

A Leontief model:

Let 

```math
Z = \begin{bmatrix}
z_{11} & \dots & z_{1n}\\
\vdots & \ddots & \vdots\\
z_{n1} & \dots & z_{nn}\\
\end{bmatrix},\: 
F = \begin{bmatrix}
f_{11} & \dots & f_{1m}\\
\vdots & \ddots & \vdots\\
f_{n1} & \dots & f_{nm}\\
\end{bmatrix},\: 
M = \begin{bmatrix} 
m_{1}\\ \vdots\\ m_{n} 
\end{bmatrix},\:
Q = \begin{bmatrix} 
q_{1}\\ \vdots\\ q_{n} 
\end{bmatrix}
```

where $Z$ is a matrix of intermediate use of inputs, with columns (*j*) representing inputs and rows (*i*) representing outputs, $F$ is a matrix of final demands, including private households and Government final consumption, gross fixed capital formation, changes in inventories and valuables, exports, et cl. $M$ and $Q$ are column vectors representing the import and the output of each sector. 

The direct consumption coefficients are given by $a_{ij} = z_{ij}/Q_{j}$.

```math
A = \begin{bmatrix}
a_{11} & \dots & a_{1n}\\
\vdots & a_{ij} & \vdots\\
a_{n1} & \dots & a_{nn}\\
\end{bmatrix},\: 
```
Given that sector inputs are equal to sector outputs, output value distribution can be represented as a system of linear equations

```math
\begin{equation} 
Q = AQ + F - M
\end{equation} 
```

It follows that 

```math
F = Q + M - AQ = (I - A)Q + M \Rightarrow Q = (I - A)^{-1}(F - M)
```
Here, $(I - A)^{-1}$ is the so-called Leontief inverse.

2 forms of the IO-row model:

- sales ------> production prospect:

$$
Q = \left( I - A \right)^{-1} \left( F - M \right)
$$

- production ------> sales prospects:

$$
F = \left( I - A \right) Q + M 
$$


#### A Python Based IO Model Simulation

Requirements: `python-3.x` <br>

Packages:<br>
~~`Pyomo`: a Python-based open-source software package that supports a diverse set of optimization capabilities for formulating, solving, and analyzing optimization models.~~<br>




### PyCGE Workflow

#### A Python Based CGE Model
<p align="center">
TODO
</p>

### Nation Utility Function
Based on the form of Cobb-Douglas function, national utility is defined as the summation of 4 reletive benefits with different weights(national preference):  current economic relative benefit, expected economic r.b., current political r.b., and expected political r.b.<br>

$$
U_t = \left(\frac{C_t} {C_t^{ * }}\right) ^ {\alpha_1} 
\lbrace\frac{1}{N}\sum_{s=1}^N\rho_C^s\left[E_t\frac{C_{t+s}}{C_{t+s}^{ * }}\right]\rbrace^{\alpha_2}
\left(\frac{P_t} {P_t^{ * }}\right) ^ {\beta_1}
\lbrace\frac{1}{N}\sum_{s=1}^N\rho_P^s\left[E_t\frac{P_{t+s}}{P_{t+s}^{ * }}\right]\rbrace^{\beta_2}
$$

which can be simplified to<br>

$$
U_t = \left(\widetilde{C_t}\right)^{\alpha_1} \left(\widetilde{EC_t}\right)^{\alpha_2} \left(\widetilde{P_t}\right)^{\beta_1} \left(\widetilde{EP_t}\right)^{\beta_2}
$$

Thus, the maximum national utility on a given set ${\tau}$ of strategies is <br>

$$
V_t = \mathop{Max}\limits_{\tau}U_t = \mathop{Max}\limits_{\tau}\left[\left(\widetilde{C_t}\right)^{\alpha_1}\left(\widetilde{EC_t}\right)^{\alpha_2}\left(\widetilde{P_t}\right)^{\beta_1}\left(\widetilde{EP_t}\right)^{\beta_2}\right]
$$

$$
h:\tau \rightarrow \{(\widetilde{C_t}),(\widetilde{EC_t}),(\widetilde{P_t}),(\widetilde{EP_t})\}
$$
<br/>

#### Economic Interests

The economic benefits of a given strategy is generated from the CGE model, evaluated by the following variables.
<br>
|Variables|Unit|Description|
|:--:|:--:|:---|
|GDP|%change|国民生产总值，是一个国家（地区）所有常住单位在一定时期内生产活动的最终成果，是国民经济的核心指标，也是衡量一个国家或地区经济状况和发展水平的重要指标。|
|Social Welfare(EV)|million dollars|CGE中的社会福利采用希克斯等价变差来表征，以政策实施前的商品价格为基础，测算居民在政策实施后的效用水平的变化情况。变动为正，说明居民福利在政策实施后得到改善，反之表示政策实施将损害居民福利。|
|Balance of Trade|million dollars|衡量贸易逆差或顺差的大小。|
|Import/Export|%change|进/出口额。|

##### 经济指标权重决定
&emsp;&emsp;CGE模型的众多预测变量具有不同的量纲，首先需要对其进行无量纲化处理。根据成本型指标和效益型指标不同的转换公式对其进行压缩。<br>
&emsp;&emsp;**（1）变异系数法**<br>
&emsp;&emsp;特点：根据各变量对结果的影响程度对指标进行打分，相对客观，且能根据策略的不同进行灵活调整，但可靠性较差。<br>


&emsp;&emsp;**（2）层次分析法**<br>
&emsp;&emsp;特点：让专家根据知识和经验对指标进行打分，相对主管，不能根据生成策略的不同进行及时调整，但可靠性较高。<br>


##### 经济利益计算函数
<p align="center">
TODO
</p>


#### Political Interests

&emsp;&emsp;可考虑的指标有：<br>
&emsp;&emsp;社会动荡指数（Social Unrest Index，新版为Reported SUI）：月度数据，每6月一发布。由国际国币基金组织（IMF）研究人员根据相关媒体报道的数量提出。覆盖130个国家 — 经初步查找，仅公布了中东国家数据。<br>
&emsp;&emsp;国家脆弱性指数（Fragile Status Index）：年度数据，由一个叫和平基金（FFP）的NGO公布。包含178个国家，每个国家获得一个FSI评分，并根据国家面临的影响其脆弱程度的不同压力进行排名。<br>
&emsp;&emsp;国家全球jun力指数（Global Firepower Index）：年度数据。该指标来源于“全球火力网”，尽管其数据被部分网络媒体、研究学者引用，但在外网上，其可信度备受争议。该指标利用其独家计算公式，考虑60多种影响因子，将各国j事力量进行排名。在最新的2024年排名中，共有145个国家上榜。<br>
&emsp;&emsp;由于社会动荡指数缺乏中美等经济体的数据，全球jun力指数可信度有存在质疑，因此选取国家脆弱指数作为zz利益的衡量指标。

##### 国家脆弱性指数预测-Baseline
&emsp;&emsp;国家脆弱性指数（FSI）为年度数据，包含160多个国家自2006年至2023年的数据。为了构建国家策略模拟的baseline，需要对FSI在2024年至2030年的变化趋势进行预测。<br>
&emsp;&emsp;由于[原始可获得数据](FSIpred/oridata/)存在样本较少、信息不完备等特征，故使用灰色预测法对其进行预测，相关代码保存在[FSI_prediction](FSIpred/FSI_prediction.ipynb)中。<br>
&emsp;&emsp;GM(1,1)模型是一种单变量的灰色预测模型，可以通过过少量的、不完全的信息，建立数据模型做出预测的一种预测方法。适用于非线性、非平稳的系统，在趋势分析方面有着广泛的应用。

&emsp;&emsp;**GM(1,1)模型原理**：
设有数列 $X^{\left( 0 \right)} \left( k \right)$ ，其一次累加生成数列为 $X^{\left( 1 \right)}$ :<br>

$$
X^{\left( 1 \right)} \left( k \right)=\sum^{k}_{i=1}X^{\left( 0 \right)} \left( k \right) \left( k=1,2,...n \right)
$$

&emsp;&emsp;对 $X^{\left( 1 \right)}$ 建立一阶线性微分方程，即GM(1,1)模型：<br>

$$
\frac{dX^{\left( 1 \right)}}{dt}+aX^{\left( 1 \right)}=\mu
$$

&emsp;&emsp;解微分方程可以求得：<br>

$$
\hat{X}^{\left( 1 \right)} \left( k+1 \right)=\left[ X^{\left( 0 \right)} \left( 1 \right) - \frac{\mu}{a} \right] e^{-at} + \frac{\mu}{a}
$$

$$
\left( k=1,2,...,n-1 \right)
$$

&emsp;&emsp;由于GM(1,1)模型得到的是一次累加量，则将 $\hat{X}^{\left( 1 \right)} \left( k+1 \right)$ 经过累减还原为：<br>

$$
\hat{X}^{\left( 0 \right)} \left( k+1 \right)=\left( e^{-\hat{a}} -1 \right) \left[ X^{\left( 0 \right)} \left( n \right) - \frac{\hat{\mu}}{\hat{a}} \right] e^{\hat{a}t}
$$

&emsp;&emsp;以美国和中国为例，国家脆弱性指数的预测结果如下：<br>

<p align="center">
<img src="FSIpred/RegFile/USA_pred_line_graph.jpg">
</p>

![image](FSIpred/RegFile/CHN_pred_line.jpg)

&emsp;&emsp;该模型的检验结果如下：<br>

|指标|美国模型|中国模型|
|:--:|:--:|:--:|
|MSE(Mean Square Error):|4.519503|3.197299|
|RMSE(Root Mean Square Error):|2.125912|1.788099|
|MAE(Mean Absolute Error):|1.823222|1.354114|
|MRE(Mean Relative Error):|0.002045|0.000685|
|R-Square:|0.652785|0.891409|

##### 国家脆弱性指数变动-Policy Simulation
&emsp;&emsp;为了模拟政策的冲击效果对国家脆弱性指数的影响，考虑将国家脆弱性指数建模到CGE模型中。<br>

<p align="center">
TODO
</p>

### HP Function
<p align="center">
TODO
</p>
