---
theme: summary
---
# Convex functions and their properties

<div class="author">

Cristiano Migali

</div>

## Basic definitions

- We say that $f : A \subseteq \mathbb{R}^n \rightarrow \mathbb{R}$ is **convex** if
>> i. $A$ is convex;
>> ii. for every $\underline{x}, \underline{y} \in A$, $\lambda \in [0, 1]$:
$$
f(\lambda \underline{x} + (1-\lambda) \underline{y}) \leq \lambda f(\underline{x}) + (1-\lambda) f(\underline{y}) \text{.}
$$

> **Remark**: geometrically (ii) means that, if we pick two points on the graph of the function and draw the segment between them, then the graph of the function between those two points will lie below such segment,

- We say that $f$ is **lipschitz convex** if $f$ is convex, differentiable, and there exists $L > 0$ s.t. $||\nabla f(\underline{x})|| \leq L$ for every $\underline{x}$ in the domain of $f$.

> **Remark**: Lipschitz convexity is a strict constraint. Even the simplest quadratic function
$$
f(x) = x^2
$$
> has unbounded first derivative.

- Let $f : A \rightarrow \mathbb{R}$ with $A \subseteq \mathbb{R}^d$ opean, and $X \subseteq A$, $X$ convex. Assume also that $f$ is differentiable.
Then, we say that $f$ is **smooth with parameter $L$** $\geq 0$ over $X$ iff
$$
f(\underline{y}) \leq f(\underline{x}) + \nabla f^T(\underline{x})(\underline{y} - \underline{x}) + \frac{L}{2}||\underline{y} - \underline{x}||^2
$$
> for every $\underline{x}, \underline{y} \in X$.

> **Remark**: the definition of smoothness in optimization is different from the one from calculus.

> **Remark**: the geometric interpretation of the definition above is that the function lies below a quadratic form.


---

## Basic properties

- **Lemma (1)**: if $f : A \subset \mathbb{R}^n \rightarrow \mathbb{R}$, with $A$ open, is differentiable, then:
> - $f$ is convex
> iff
> - $A$ is convex and
$$
f(\underline{y}) \geq f(\underline{x}) + \nabla f^T(\underline{x}) (\underline{y} - \underline{x})
$$
>> for every $\underline{x}, \underline{y} \in A$.

> **Remark**: geometrically the last condition means that the function lies above its tangent hyperplane.

> **Proof**: Assume that $f$ is convex. The result is trivial if $\underline{x} = \underline{y}$, hence let $\underline{x}, \underline{y} \in A$ s.t. $\underline{x} \neq \underline{y}$. Since $f$ is convex, $A$ in convex too, hence $(1-t) \underline{x} + t \underline{y} \in A$ for every $t \in [0, 1]$. Furthermore, since $A$ is open, there exists $\alpha > 0$ s.t. if
$$
||\underline{z} - \underline{y}|| < \alpha \text{ or } ||\underline{x} - \underline{y}|| < \alpha
$$
> then, $\underline{z} \in A$.
Hence, if $0 \leq \beta < \frac{\alpha}{||\underline{x} - \underline{y}||}$,
$$
||(1-1-\beta) \underline{x} + (1+\beta) \underline{y} - \underline{y}|| = \beta||\underline{x} - \underline{y}|| < \alpha
$$
> Hence, $[1-(1+\beta)] \underline{x} + (1+\beta) \underline{y} \in A$.
Analogously, if $0 \leq \beta < \frac{\alpha}{||\underline{x} - \underline{y}||}$,
$$
||(1+\beta) \underline{x} - \beta \underline{y} - \underline{x}|| = \beta ||\underline{x} - \underline{y}|| = \beta ||\underline{x} - \underline{y}|| < \alpha \text{.}
$$
> Hence, $[1-(-\beta)]\underline{x} + (-\beta) \underline{y} \in A$.
We just prove that $(1-t) \underline{x} + t \underline{y} \in A$, for every $t \in (-\frac{\alpha}{||\underline{x} - \underline{y}||}, 1 + \frac{\alpha}{||\underline{x} - \underline{y}||})$.
Let
$$
g : (-\frac{\alpha}{||\underline{x} - \underline{y}||}, 1 + \frac{\alpha}{||\underline{x} - \underline{y}||}) \rightarrow \mathbb{R}
$$

$$
t \mapsto f((1-t) \underline{x} + t \underline{x}) \text{.}
$$
> $g$ is well-defined by the reasoning above. Furthermore $g$ is defined on an open set and it is the composition of two differentiable functions, hence, by the chain rule:
$$
g'(0) = \nabla f^T(\underline{x})(\underline{y} - \underline{x}) \text{.}
$$

---

> Furthermore, by definition
$$
g'(0) = \lim_{h \rightarrow 0}\frac{f((1-h) \underline{x} + h \underline{y}) - f(\underline{x})}{h} \text{.}
$$
> Let $\epsilon > 0$. Then there exists $\delta > 0$ s.t., if $|h| < \delta$, then
$$
|\frac{f((1-h) \underline{x} + h \underline{y}) - f(\underline{x})}{h} - \nabla f^T(\underline{x})(\underline{y} - \underline{x})| < \epsilon \text{.}
$$
> Let $h = \frac{1}{2}\min(\delta, 1)$. Then $h > 0$, $h < 1$, and $h < \delta$.
Hence
$$
\nabla f^T(\underline{x})(\underline{y} - \underline{x}) - \epsilon < \frac{f((1-h) \underline{x} + h \underline{y}) - f(\underline{x})}{h} \leq
$$

$$
\leq \frac{(1-h)f(\underline{x}) + hf(\underline{t}) - f(\underline{x})}{h} = f(\underline{y}) - f(\underline{x}) \text{ iff }
$$
$$
f(\underline{y}) \geq f(\underline{x}) + \nabla f^T(\underline{x})(\underline{y} - \underline{x}) - \epsilon \text{.}
$$
> Since the result holds for every $\epsilon > 0$, then it must be
$$
f(\underline{y}) \geq f(\underline{x}) + \nabla f^T(\underline{x}) (\underline{y} - \underline{x}) \text{.}
$$

> Conversely, assume that for every $\underline{x}, \underline{y} \in A$
$$
f(\underline{y}) \geq f(\underline{x}) + \nabla f^T(\underline{x}) (\underline{y} - \underline{x}) \text{.}
$$
> Let $\underline{x}, \underline{y} \in A$, let $\lambda \in [0, 1]$. Then
$$
\underline{z} = \lambda \underline{x} + (1-\lambda) \underline{y} \in A \text{.}
$$
> Hence
$$
f(\underline{x}) \geq f(\underline{z}) + \nabla f^T(\underline{z}) (\underline{x} - \underline{z}) \text{, and}
$$
$$
f(\underline{y}) \geq f(\underline{z}) + \nabla f^T (\underline{z})(\underline{y} - \underline{z}) \text{.}
$$
> Then
$$
\lambda f(\underline{x}) + (1-\lambda) f(\underline{y}) \geq f(\underline{z}) + \nabla f^T(\underline{z}) (\lambda \underline{x} + (1-\lambda) \underline{y} - \underline{z}) =
$$
$$
= f(\underline{z}) + \nabla f^T(\underline{z})(\underline{z} - \underline{z}) = f(\underline{z}) = f(\lambda \underline{x} + (1-\lambda) \underline{y})
$$
> as we wanted to prove.

---

> **Lemma (2)**: Let $A \subseteq \mathbb{R}^d$ open and convex, let $f : A \rightarrow \mathbb{R}$ differentiable. Let $L \geq 0$. Then the following statements are equivalent:
>> i. $f$ is smooth with parameter $L$;
>> ii.
$$
g : A \rightarrow \mathbb{R}
$$
$$
\underline{x} \mapsto \frac{L}{2} \underline{x}^T \underline{x} - f(\underline{x}) \text{.}
$$
>> is convex.

> **Proof**: observe that $g$ is differentiable. We will calculate its gradient using the properties in the cheatsheet.
$$
\nabla g(\underline{x}) = (g'(\underline{x}))^T = (\frac{L}{2} \begin{bmatrix} \underline{x}^T & \underline{x}^T \end{bmatrix} \begin{bmatrix} I_d \\ I_d \end{bmatrix} - f'(\underline{x}))^T =
$$
$$
(L \underline{x}^T - f'(\underline{x}))^T = L \underline{x} - \nabla f(\underline{x}) \text{.}
$$

> Let's prove that (i) implies (ii). Assume that $f$ is smooth.
$$
g(\underline{y}) = \frac{L}{2} \underline{y}^T \underline{y} - f(\underline{y}) \geq \frac{L}{2} \underline{y}^T \underline{y} - f(\underline{x}) - \nabla f^T(\underline{x})(\underline{y} - \underline{x}) - \frac{L}{2}||\underline{y} - \underline{x}||^2 =
$$

$$
= -\frac{L}{2} \underline{x}^T \underline{x} - f(\underline{x}) + \frac{L}{2} \underline{y}^T \underline{y} - \frac{L}{2} \underline{y}^T \underline{y} - \nabla f^T(\underline{x})(\underline{y} - \underline{x}) + L \underline{x}^T \underline{y} =
$$

$$
= \frac{L}{2} \underline{x}^T \underline{x} - f(\underline{x}) - \nabla f^T(\underline{x}) (\underline{y} - \underline{x}) + L\underline{x}^T(\underline{y} - \underline{x}) = g(\underline{x}) + \nabla g(\underline{x}) (\underline{y} - \underline{x}) \text{.}
$$
> Hence, $g$ is convex by lemma (1).

> Conversely, let's prove that (ii) implies (i).

$$
f(\underline{y}) = -g(\underline{y}) + \frac{L}{2} \underline{y}^T \underline{y} \leq -g(\underline{x}) - \nabla g^T(\underline{x}) (\underline{y} - \underline{x}) + \frac{L}{2} \underline{y}^T \underline{y} = 
$$

$$
= f(\underline{x}) - \frac{L}{2} \underline{x}^T \underline{x} - (L \underline{x}^T - \nabla f^T(\underline{x})) (\underline{y} - \underline{x}) + \frac{L}{2} \underline{y}^T \underline{y} =
$$

$$
= f(\underline{x}) + \nabla f^T(\underline{x}) (\underline{y} - \underline{x}) + \frac{L}{2} \underline{x}^T \underline{x} - L \underline{x}^T \underline{y} + \frac{L}{2} \underline{y}^T \underline{y} =
$$

$$
= f(\underline{x}) + \nabla f^T(\underline{x})(\underline{y} - \underline{x}) + \frac{L}{2}||\underline{y} - \underline{x}||^2
$$
> as we wanted to prove.

---

> **Remarks**:
>> i. If $f$ is smooth with $L = 0$, and convex, then
$$
f(\underline{x}) = f(\underline{x}_0) + \nabla f^T(\underline{x}) (\underline{x} - \underline{x}_0) \text{,}
$$
>> that is, $f$ is an affine function.

>> ii. Let $f(x) = x^2$, $L = 2$, then
$$
f(y) = y^2 = (y-x)^2 - x^2 + 2xy =
$$

$$
= x^2 + 2x(y - x) + (y-x)^2 =
$$

$$
= f(x) +f'(x)(y - x) + \frac{L}{2}(y - x)^2 \text{,}
$$
>> that is, $f$ is smooth.

>> iii.  Let $f(\underline{x}) = \underline{x}^T Q \underline{x} + \underline{b}^T \underline{x} + c$ where $Q \in \mathbb{R}^{d \times d}$ is symmetric, $\underline{b} \in \mathbb{R}^d$, and $c \in \mathbb{R}$.
Then
$$
\nabla f(\underline{x}) = 2 Q \underline{x} + \underline{b}
$$
>> as we've seen many times.
It follows that:
$$
f(\underline{y}) = \underline{y}^T Q \underline{y} + \underline{b}^T \underline{y} + c =
$$

$$
= (\underline{y} - \underline{x})^T Q (\underline{y} - \underline{x}) + \underline{x}^T Q \underline{x} - 2 \underline{x}^T Q \underline{x} + 2 \underline{y}^T Q \underline{x} + \underline{b}^T \underline{y} +c + \underline{b}^T \underline{x} + c - \underline{b}^T \underline{x} - c =
$$

$$
= \underline{x}^T Q \underline{x} + \underline{b}^T \underline{x} + c + 2(\underline{y}^T - \underline{x}^T) Q \underline{x} + \underline{b}^T (\underline{y} - \underline{x}) + (\underline{y} - \underline{x})^T Q (\underline{y} - \underline{x}) =
$$

$$
= f(\underline{x}) + 2(Q \underline{x})^T (\underline{y} - \underline{x}) + \underline{b}^T (\underline{y} - \underline{x}) + (\underline{y} - \underline{x})^T Q (\underline{y} - \underline{x}) =
$$

$$
= f(\underline{x}) + \nabla f^T(\underline{x}) (\underline{y} - \underline{x}) + (\underline{y} - \underline{x})^T Q (\underline{y} - \underline{x}) \leq
$$

$$
\leq f(\underline{x}) + \nabla f^T(\underline{x}) (\underline{y} - \underline{x}) + ||\underline{y} - \underline{x}|| ||Q(\underline{y} - \underline{x})|| \text{ (by Cauchy-Schwatz) } \leq
$$

$$
\leq f(\underline{x}) + \nabla f^T(\underline{x})(\underline{y} - \underline{x}) + ||\underline{y} - \underline{x}|| ||Q||_2 ||\underline{y} - \underline{x}|| =
$$

$$
f(\underline{x}) + \nabla f^T(\underline{x})(\underline{y} - \underline{x}) + ||Q||_2 ||\underline{y} - \underline{x}||^2 \text{.}
$$

>> Hence, $f$ is smooth with $L = 2 ||Q||_2$.

>> iv. Let $f(x) = x^4$ (which is convex).
Then $f'(x) = 4 x^3$, hence:

---

$$
f(y) - f(x) - f'(x)(y-x) + \frac{L}{2}(y - x)^2 =
$$

$$
= y^4 - x^4 - 4x^3(y-x) + \frac{L}{2} y^2 + \frac{L}{2} x^2 - L xy =
$$

$$
= y^4 - x^4 - 4 x^3 y + 4 x^4 + \frac{L}{2} y^2 + \frac{L}{2} x^2 - L xy =
$$

$$
= y^4 + \frac{L}{2} y^2 + (-4x^3 - Lx)y + (3x^4 + \frac{L}{2} \underline{x}^2) \text{.}
$$

>> Then, for every $x \in \mathbb{R}, L > 0$, we can find $y$ big enough such that the expression above is greater than 0. Hence $f$ is not smooth.
In general if $f$ is asymptotically more than quadratic, then $f$ is not smooth.

>> v. Even if $f$ is less than quadratic, we can't say anything about its smoothness.
For example let $f(x) = |x|^{\frac{3}{2}}$.
Then
$$
f'(x) = \begin{cases}
\frac{3}{2}\sqrt{x} \text{ if } x > 0 \\
- \frac{3}{2} \sqrt{ -x } \text{ if } x < 0
\end{cases} \text{.}
$$
>> Let $x >0, y \geq 0$.
Then
$$
f(y) - f(x) - f'(x)(y-x) - \frac{L}{2}(y - x)^2 =
$$

$$
= y^{\frac{3}{2}} - x^{\frac{3}{2}} - \frac{3}{2}x^{\frac{1}{2}}(y - x) - \frac{L}{2} y^2 - \frac{L}{2} x^2 + L x y =
$$

$$
= y^{\frac{3}{2}} + \frac{1}{2}x^{\frac{3}{2}} - \frac{3}{2} x^{\frac{1}{2}} y - \frac{L}{2} y^2 - \frac{L}{2} x^2 + L xy \text{.}
$$

>> Hence
$$
f(0) - f(x) - f'(x)(0-x) - \frac{L}{2}(0-x)^2 =
$$

$$
= \frac{1}{2}x^{\frac{3}{2}} - \frac{L}{2}x^2 = \frac{1}{2} x (x^{\frac{1}{2}} - L \underline{x}) \text{.}
$$

>> It is easy to prove that if $y < \frac{1}{b^n}$ with $b \in \mathbb{R}^+$, then $\sqrt{y} > b^{\frac{n}{2}}y$.
For observe that $y < \frac{1}{b^n}$ implies $\sqrt{y} < b^{-\frac{n}{2}}$. Now suppose $\sqrt{y} \leq b^{\frac{n}{2}}y$.
Then
$$
\sqrt{y} \sqrt{y} \leq b^{\frac{n}{2}} y \sqrt{y} < b^{\frac{n}{2}} y b^{-\frac{n}{2}} = y \text{,}
$$

---

>> which is absurd.
From this observation it follows that, if we take $0 < x < \frac{1}{b^n}$, with $b > 1$, then
$$
\frac{1}{2}x(x^{\frac{1}{2}} - Lx) > \frac{1}{2}x(b^{\frac{n}{2}}x - Lx) = \frac{1}{2}x^2(b^{\frac{n}{2}} - L)
$$
>> which is greater than 0 for any value of $L$ if we take $n$ big enough.
Hence $f$ isn't smooth.

> **Lemma (3)**: let $f : A \subseteq \mathbb{R}^d \rightarrow \mathbb{R}$ differentiable, with $A$ convex and open. Then the following statements are equivalent:
>> i. $f$ is smooth with parameter $L$.
>> ii. $(\nabla f (\underline{x}) - \nabla f (\underline{y}))^T (\underline{x} - \underline{y}) \leq L ||\underline{x} - \underline{y}||^2$ for all $\underline{x}, \underline{y} \in A$.

> **Proof**: Let's prove that (i) implies (ii).
By the smoothness:
$$
f(\underline{y}) \leq f(\underline{x}) + \nabla f^T(\underline{x}) (\underline{y} - \underline{x}) + \frac{L}{2} ||\underline{y} - \underline{x}||^2 \text{, and}
$$

$$
f(\underline{x}) \leq f(\underline{y}) + \nabla f^T(\underline{y}) (\underline{x} - \underline{y}) + \frac{L}{2} ||\underline{x} - \underline{y}||^2 \text{.}
$$
> If we sum the two inequalities we get:
$$
f(\underline{y}) + f(\underline{x}) \leq f(\underline{x}) + f(\underline{y}) + (\nabla f(\underline{x}) - \nabla f(\underline{y}))^T(\underline{y} - \underline{x}) + L ||\underline{x} - \underline{y}||^2 \text{ iff }
$$

$$
(\nabla f(\underline{x}) - \nabla f(\underline{y}))^T (\underline{x} - \underline{y}) \leq L ||\underline{x} - \underline{y}||^2 \text{,}
$$
> as we wanted to prove.

> Conversely, let's prove that (ii) implies (i). Let $\underline{x}, \underline{y} \in A$. By the same arguments used in the proof of lemma(1):
$$
g : (a, b) \rightarrow \mathbb{R}
$$

$$
t \mapsto f(\underline{x} + t (\underline{y} - \underline{x}))
$$
> with $a < 0$ and $b > 1$, is well-defined, and, so, as we showed before.
$$
g'(t) = \nabla f^T(\underline{x} + t(\underline{y} - \underline{x}))(\underline{y} - \underline{x}) \text{.}
$$

By the fundamental theorem of calculus:
$$
g(1) - g(0) = \int_0^1 g'(t) dt = \int_0^1 \nabla f^T(\underline{x} + t(\underline{y} - \underline{x}))(\underline{y} - \underline{x}) dt =
$$

---

$$
= \int_0^1 ( \nabla f^T(\underline{x})(\underline{y} - \underline{x}) + \nabla f^T(\underline{x} + t(\underline{y} - \underline{x}))(\underline{y} - \underline{x}) - \nabla f^T(\underline{x})(\underline{y} - \underline{x}) ) dt =
$$

$$
\begin{matrix}
= \lim_{\epsilon \rightarrow 0^+} \int_\epsilon^1 ( \nabla f^T(\underline{x})(\underline{y} - \underline{x}) + \nabla f^T(\underline{x} + t(\underline{y} - \underline{x}))(\underline{y} - \underline{x}) - \nabla f^T(\underline{x})(\underline{y} - \underline{x}) ) dt \\

\text{(by Theorem 6.20 of Baby Rudin)}
\end{matrix} =
$$

$$
= \lim_{\epsilon \rightarrow 0^+} \int_\epsilon^1 ( g'(0) + \frac{1}{t}(\nabla f^T(\underline{x} + t(\underline{y} - \underline{x})) - \nabla f^T(\underline{x})) t (\underline{y} - \underline{x}) ) dt \leq
$$

$$
= \lim_{\epsilon \rightarrow 0^+} \int_\epsilon^1 (g'(0) + \frac{L}{t}||t(\underline{y} - \underline{x})||^2)dt =
$$

$$
= \lim_{\epsilon \rightarrow 0^+}(g'(0)(1- \epsilon) + L||\underline{y} - \underline{x}||^2 \int_\epsilon^1 t dt) =
$$

$$
= \lim_{\epsilon \rightarrow 0^+}(g'(0)(1 - \epsilon) + L||\underline{y} - \underline{x}||^2 (\frac{1}{2} - \frac{\epsilon^2}{2})) = g'(0) + \frac{L}{2}||\underline{y} - \underline{x}||^2 \text{.}
$$
> Then
$$
f(\underline{y}) = g(1) = g(0) + g(1) - g(0) \leq g(0) +g'(0) + \frac{L}{2}||\underline{y} - \underline{x}||^2 =
$$

$$
= f(\underline{x}) + \nabla f^T(\underline{x}) (\underline{y} - \underline{x}) + \frac{L}{2}||\underline{y} - \underline{x}||^2 \text{,}
$$
> as we wanted to prove.

> **Lemma (4)**: let $f : \mathbb{R}^d \rightarrow \mathbb{R}$ be smooth over $\mathbb{R}^d$ with parameter $L$. Let $\underline{x}^*$ be a minimizer of $f$. Then
$$
\frac{1}{2L}||\nabla f(\underline{z})||^2 \leq f(\underline{z}) - f(\underline{x}^*) \leq \frac{L}{2}||\underline{z} - \underline{x}^*||^2 
$$
> for all $\underline{z} \in \mathbb{R}^d$.

> **Proof**: Let $\underline{z} \in \mathbb{R}^d$. By the smoothness of $f$:
$$
f(\underline{z}) \leq f(\underline{x}^*) + \nabla f^T(\underline{x}^*)(\underline{z} - \underline{x}) + \frac{L}{2}||\underline{z} - \underline{x}^*|| =
$$

$$
= \begin{matrix}
f(\underline{x}^*) + \underline{0}_d^T (\underline{z} - \underline{x}) + \frac{L}{2}||\underline{z} - \underline{x}^*||^2 \\
\text{(by Fermat's theorem)}
\end{matrix} \text{ iff }
$$

$$
f(\underline{z}) - f(\underline{x}^*) \leq \frac{L}{2} ||\underline{z} - \underline{x}^*||^2 \text{.}
$$

> We just proved inequality on the right.

---

> For the inequality on the left, we need to prove an intermediate result:
$$
\inf_{\underline{y} \in \mathbb{R}^d} \{ f(\underline{z}) + \nabla f^T (\underline{z}) (\underline{y} - \underline{z}) + \frac{L}{2}||\underline{y} - \underline{z}||^2 \} =
$$

$$
= \inf_{||\underline{v}|| = 1} \inf_{t \in \mathbb{R}} \{ f(\underline{z}) + t \nabla f^T (\underline{z}) \underline{v} + \frac{L}{2} t^2 \} \text{.}
$$

> First of all observe that
$$
P_{\underline{v}}(t) = f(\underline{z}) + t \nabla f^T (\underline{z}) \underline{v} + \frac{L}{2} t^2
$$
> is a parabola in $t$ with the coefficient of $t^2$ greater than 0. Then it admits minimum at $p_{\underline{v}}'(\hat{t}_\underline{v}) = 0$, iff
$$
\nabla f^T (\underline{z}) \underline{v} + L \hat{t}_\underline{v} = 0 \text{ iff }
$$

$$
\hat{t}_\underline{v} = - \frac{\nabla f^T (\underline{z}) \underline{v}}{L} \text{.}
$$

> Hence, $\inf_{t \in \mathbb{R}}\{ f(\underline{z}) + t \nabla f^T (\underline{z}) \underline{v} + \frac{L}{2} t^2 \} = p_{\underline{v}}(\hat{t}_\underline{v}) =$

$$
= f(\underline{z}) - \frac{\nabla f^T(\underline{z}) \underline{v}}{L} \nabla f^T(\underline{z}) \underline{v} + \frac{L}{2} \frac{(\nabla f^T(\underline{z}) \underline{v})^2}{L^2} =
$$

$$
= f(\underline{z}) - \frac{(\nabla f^T(\underline{z}) \underline{v})^2}{2L} \text{.}
$$

> Then we have to prove that
$$
\inf_{\underline{y} \in \mathbb{R}^d} \{ f(\underline{z}) + \nabla f^T(\underline{z})(\underline{y} -\underline{z}) + \frac{L}{2}||\underline{y} - \underline{z}||^2 \} = \inf_{||\underline{v} = 1||} \{ p_{\underline{v}}(\hat{t}_\underline{v}) \} \text{.}
$$

> Let $a = f(\underline{z}) + \nabla f^T(\underline{z}) (\underline{y} - \underline{z}) + \frac{L}{2}||\underline{y} - \underline{z}||^2$ for some $\underline{y} \in \mathbb{R}^d$.
If $\underline{y} = \underline{z}$, $a = f(\underline{z}) = p_\underline{v}(0) \geq p_\underline{v}(\hat{t}_\underline{v})$ for every $\underline{v} \in \mathbb{R}^d$, $||\underline{v}|| = 1$.
If $\underline{y} \neq \underline{z}$, then
$$
a  = f(\underline{z}) + ||\underline{y} - \underline{z}|| \nabla f^T(\underline{z}) \frac{\underline{y} - \underline{z}}{||\underline{y} - \underline{z}||} + \frac{L}{2} ||\underline{y} - \underline{z}||^2 = 
$$

$$
= p_{\frac{\underline{y} - \underline{z}}{||\underline{y} - \underline{z}||}}(||\underline{y} - \underline{z}||) \geq p_{\frac{\underline{y} - \underline{z}}{||\underline{y} - \underline{z}||}}(\hat{t}_{\frac{\underline{y} - \underline{z}}{||\underline{y} - \underline{z}||}}) \text{.}
$$

> In every case $a \geq p_\underline{v}(\hat{t}_\underline{v})$ for some $\underline{v} \in \mathbb{R}^d$, with $||\underline{v}|| = 1$. Then

$$
\inf_{\underline{y} \in \mathbb{R}^d} \{ f(\underline{z}) + \nabla f^T(\underline{z})(\underline{y} -\underline{z}) + \frac{L}{2}||\underline{y} - \underline{z}||^2 \} \geq \inf_{||\underline{v}|| = 1} \{ p_{\underline{v}}(\hat{t}_\underline{v}) \} \text{.}
$$

---

> Now, let $a = p_\underline{v}(\hat{t}_\underline{v})$ for some $\underline{v} \in \mathbb{R}^d$, with $||\underline{v}|| = 1$.
Let $\underline{y} = \hat{t}_\underline{v} \underline{v} + \underline{z} \in \mathbb{R}^d$. Then
$$
a = f(\underline{z}) + \nabla f^T(\underline{z})(\hat{t}_\underline{v} \underline{v}) + \frac{L}{2}\hat{t}_\underline{v}^2 ||\underline{v}||^2 =  f(\underline{z}) + \nabla f^T(\underline{z})(\underline{y} - \underline{z}) + \frac{L}{2}||\underline{y} - \underline{z}||^2 \text{.}
$$

> That is
$$
\{ p_{\underline{v}}(\hat{t}_\underline{v}) | ||\underline{v}|| = 1\}  \subseteq \{ f(\underline{z}) + \nabla f^T(\underline{z})(\underline{y} - \underline{z}) + \frac{L}{2}||\underline{y} - \underline{z}||^2 | \underline{y} \in \mathbb{R}^d \} \text{.}
$$
> Hence:
$$
\inf_{||\underline{v}|| = 1} \{ p_{\underline{v}}(\hat{t}_\underline{v}) \} \geq \inf_{\underline{y} \in \mathbb{R}^d} \{ f(\underline{z}) + \nabla f^T(\underline{z})(\underline{y} -\underline{z}) + \frac{L}{2}||\underline{y} - \underline{z}||^2 \} \text{.}
$$

> The equality follows by considering both inequalities.

> Finally:
$$
f(\underline{x}^*) = \inf_{\underline{y} \in \mathbb{R}^d}\{ f(\underline{y}) \} \leq \inf_{\underline{y} \in \mathbb{R}^d}\{ f(\underline{z}) + \nabla f^T(\underline{z})(\underline{y} - \underline{x}) + \frac{L}{2}||\underline{y} - \underline{x}||^2 \} =
$$

$$
= \inf_{||\underline{v}|| = 1} \inf_{t \in \mathbb{R}} \{ f(\underline{z}) + t \nabla f^T (\underline{z}) \underline{v} + \frac{L}{2} t^2 \} =
$$

$$
= \begin{matrix}
\inf_{||\underline{v}|| = 1} \{ f(\underline{z}) - \frac{(\nabla f^T(\underline{z}) \underline{v})^2}{2L} \} \\
\text{ (computed before) }
\end{matrix} = f(\underline{z}) - \frac{1}{2L} \sup_{||\underline{v}|| = 1} \{ (\nabla f^T(\underline{z}) \underline{v})^2 \} =
$$

$$
= \begin{matrix}
f(\underline{z}) - \frac{1}{2L} ||\nabla f^T(\underline{z})||^2 \\
\text{(straightforward consequence of Cauchy-Schwarz)}
\end{matrix} \text{.}
$$

> Iff
$$
\frac{1}{2L}||\nabla f^T(\underline{z})||^2 \leq f(\underline{z}) - f(\underline{x}^*)
$$
> as we wanted to prove.

**Lemma (5)**: