---
theme: summary
---
# Linear Programming duality

<div class="author">

Cristiano Migali

</div>

## Introduction

The central idea of **Linear Programming duality** (_and duality in general_) is the following: to any minimization (maximization) LP we can associate a closely related maximization (minimization) LP based on the same parameters. The two problems will have different feasible regions and objective functions, but we are guaranteed that the **optimal objective function values coincide**.

### Heuristic motivation

Consider the following (general) maximization LP:

<div class="centered-definition-expression">

$\max z = \sum_{j=1}^{n} c_j x_j$

s. t.

$\sum_{j=1}^n a_{1j} x_j \leq b_1$ ,
...,
$\sum_{j=1}^n a_{mj} x_j \leq b_m$ ,

$x_j \geq 0 \forall j \in \{ 1, ..., n \}$
</div>

Suppose that we want to **estimate** the **optimal objective function** value $z^*$ by providing better and better **upper bounds**. Let's see how we can do so:

- consider the linear combination (with non-negative coefficients) of the constraints of the LP, that is:

<div class="centered-definition-expression">

$(\sum_{i=1}^m \alpha_i a_{i1}) x_1 + ... +  (\sum_{i=1}^m \alpha_i a_{in}) x_n =$

$= \alpha_1 \sum_{j=1}^n a_{1j} x_j + ... + \alpha_m \sum_{j=1}^n a_{mj} x_j \leq$

$\leq \alpha_1 b_1 + ... + \alpha_m b_m$

where $\alpha_1, ..., \alpha_m \geq 0$ ;

</div>

- 