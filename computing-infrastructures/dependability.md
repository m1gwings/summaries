---
marp: true
theme: summary
math: mathjax
---
# Dependability

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Roberto Sala_)

</div>

<style>
section {
    font-size: x-large;
}

.definition {
    padding-left: 0.5cm;
    padding-right: 0.5cm;
    background: var(--algorithms);
    border-radius: 0.5cm;
    border-style: solid;
    border-color: var(--text);
    border-width: 3pt;
    text-align: justify;
}
</style>

<div class="definition">

**Dependability** is a _measure_ of how much we trust a system.
In particular, it is the _ability_ of a system to perform its functionality while exposing:
- reliability: the continuity of correct service;
- availability: the readiness for correct service;
- maintainability: the ability for easy maintenance;
- safety: the absence of catastrophic consequences;
- security: the confidentiality and integrity of the data.

</div>

A lot of effort is devoted to make sure the implementation:
- matches specifications;
- fulfills requirements;
- meets constraints;
- optimizes selected parameters (performance, energy).

Nevertheless, even if all above aspects are satisfied, things _may go wrong_: the system can fail because something broke.

A single system failure may affect a large number of people and it may have high costs. Furthermore, systems that are not dependable are likely not be used or adopted.

---

This is the reason why we need to think about dependability both at design-time and at runtime.
In particular, during the design phase we can analyze the system under design, measure its dependability property, and modify the design if required.
At runtime we can detect malfunctions, understand causes, and react.

Failures occur in development and operation:
- failures in development _should_ be avoided;
- failures in operation _cannot_ be avoided (things break), they must be dealt with.

The design should take failures into account and guarantee that control and safety are achieved when failures occur.

Dependability used to be a relevant aspect only for safety-critical and mission-critical application environments. But a failure of a non-critical system can still have economic and reputation effects.

## How to provide dependability?

To provide dependability we can adopt the failure avoidance paradigm:
- make a _conservative design_;
- perform _design validation_;
- run detailed tests;
- screen infant mortality.

---

## "Formal" treatment of reliability and availability

### Reliability

**Reliability** is the ability of a system or component to perform its required functions under stated conditions for a specified period of time.

<div class="definition">

Formally, we define **reliability** $R(t)$ the probability that the system will operate correctly in a specified operating environment until time $t$ assuming that the system was operating at $t = 0$:
$$
R(t) = \mathbb{P}(\text{system has not failed in } [0, t] \ |
$$
$$
|\text{ system was operating at } t = 0).
$$

</div>

We denote with $Q(t) = 1 - R(t)$ the **unreliability**.

Observe that $R(t)$ is a _non-increasing_ function varying from 1 to 0 over $[0, +\infty)$:
$$
\lim_{t \rightarrow + \infty} R(t) = 0.
$$

Reliability is often used to characterize systems in which even small periods of incorrect behavior are unacceptable.

---

### Availability

**Availability** is the degree to which a system or component is operational and accessible when required for use:
$$
\text{availability } = \frac{\text{up-time}}{\text{down-time}}.
$$

<div class="definition">

Formally, we define **availability** $A(t)$ the probability that the system will be operational at time $t$:
$$
A(t) = \mathbb{P}(\text{system is operating at time } t).
$$

</div>

Observe that the definition of availability admits the possibility of brief outages, and this makes it fundamentally different from reliability.

It follows that the **unavailability** is $1-A(t)$.

If the system is **NOT repairable**: $A(t) = R(t)$ (since the system is operating at time $t$ iff the system has not failed in $[0, t]$).
In general (for **repairable** systems) $A(t) \geq R(t)$ (since if the system has not failed in $[0, t]$ then it is operating at time $t$).

### Indices related to $R(t)$ and $A(t)$

We define **Mean Time To Failure** (**MTTF**) the mean time before <u>any</u> failure will occur.

---

We define **Mean Time Between Failures** (**MTBF**) the mean time between two failures.
Under the following regularity assumption for the reliability function:
$$
\lim_{t \rightarrow + \infty} t R(t) = 0
$$
it is possible to compute the MTTF from the reliability of a system.

In particular let $T$ be a random variable representing the failure time of a system.
Then: $R(t) = \mathbb{P}(T > t) = 1 - F_T(t)$.
Hence, thanks to integration by parts:
$$
\int_0^{+ \infty} R(t) dt = \int_0^{+ \infty}(1-F_T(t)) dt = \int_0^{+\infty} (1-F_T(t)) \cdot 1 dt =
$$

$$
= \left[ (1-F_T(t)) t \right]^{+\infty}_0 - \int_0^{+\infty} (-f_T(t)) t dt =
$$

$$
= \lim_{t \rightarrow + \infty} t R(t) - 0 + \int_0^{+\infty} t f_T(t) dt = \mathbb{E}[T] = \text{MTTF}.
$$

The MTBF can be estimated through a simple ratio:
$$
\text{MTBF} = \frac{\text{total operating time}}{\text{number of failures}}.
$$

**Remark**: usually we model $T$ with an exponential density: $T \sim \varepsilon(\lambda)$: $f_T(t; \lambda) = \lambda e^{-\lambda t} \mathbb{1}\{t \geq 0\}$ where $\lambda \geq 0$.

---

It follows that $F_T(t; \lambda) = 1 - e^{-\lambda t}$, and so, $R(t) = e^{-\lambda t}$.
Furthermore:
$$
\mathbb{E}[T] = \frac{1}{\lambda}, \mathbb{V}\text{ar}[T] = \frac{1}{\lambda^2}.
$$

Another important index is the **Failures In Time** (**FIT**) which is the number of expected failures per $10^9 h$ (_1 billion hours_) of operation for a device.

Furthermore, we define the **failure rate**
$$
\lambda = \frac{\text{number of failures}}{\text{total operating time}}.
$$
Observe that:
$$
\text{MTBF} = \frac{1}{\lambda}.
$$

Usually, the failure rate of a system is NOT constant during the operation time. Indeed the curve $\lambda(t)$ over $t$, known as **Product Reliability Curve**, takes a bathtub shape.
We can distinguish 3 phases of the operating life of a system.
1. **Infant mortality**: at the beginning the failure rate is high, and it decreases fast. This is due to the failures showing up in new systems. Usually these failures happen in testing and not in production.

2. **Random failures**: the central phase presents an almost constant failure rate. Failures can show up "_uniformly_".

---

3. **Wear out**: at the end of its life, some components can cause the failure of a system. Pre-emptive maintenance can reduce the number of this type of failures.

### Fault vs Error vs Failure

A **fault** is a _defect_ of the system that _may_ cause errors or even failures.

An example of fault is a bug in a computer program: we could be lucky and never trigger its behavior, anyways the defect exists and it may cause problems in response to the "right" input sequence.

An **error** is a wrong result/value on an _internal_ signal of the system, that is, a signal which is not observable from the exterior of the system (here we're using the term signal with a very broad meaning).

For example, due to a bug, an autonomous vehicle could compute the wrong trajectory: observe that the trajectory to follow is not observable from the outside of the system.

A **failure** is a wrong result/value on an _external_ signal of the system, that is, a signal on an interface with the exterior.

When the autonomous vehicle of the previous example follows the wrong trajectory, it could crash, exhibiting a wrong behavior to the exterior.

---

Observe that NOT always the **fault-error-failure chain** closes: fault could never be triggered and errors can be absorbed.

### Reliability Block Diagrams (RBD)

A **Reliability Block Diagram** (**RBD**) allows to represent a system as a composition of several subsystems, represented as blocks. The objective is calculating the reliability of the whole system from the reliability of the single blocks.
Blocks are then combined together to model all the possible success paths. In particular a RBD is a DAG with a source and sink: the system is operating iff there is a path of operating nodes from the source to the sink.

We can connect blocks:
- **in series**: all blocks must work for the system to work;
- **in parallel**: at least one block must work for the system to work.

Let $R_S$ denote the reliability of the system and $R_{C_1}$ and $R_{C_2}$ the reliability of its components. Analogously, let $A_S$, $A_{C_1}$, and $A_{C_2}$ denote the availabilities. <u>We assume that the failures of the components are independent</u>.

- If **$C_1$ and $C_2$ are connected in series**:

$$
R_S(t) = \mathbb{P}(T_S > t) = \mathbb{P}(T_{C_1} > t, T_{C_2} > t) = \mathbb{P}(T_{C_1} > t) \cdot
$$

$$
\cdot \mathbb{P}(T_{C_2} > t) = R_{C_1}(t) R_{C_2}(t).
$$

---

> If we assume that the failure times follow an exponential distribution, that is: $R_{C_1}(t) = e^{-\lambda_{C_1} t}$, and $R_{C_2}(t) = e^{-\lambda_{C_2} t}$, then:

$$
R_S(t) = R_{C_1}(t)R_{C_2}(t) = e^{-\lambda_{C_1} t} e^{-\lambda_{C_2} t} =
$$
$$
= e^{-(\lambda_{C_1} + \lambda_{C_2}) t} = e^{-\lambda_S t} \text{ with } \lambda_S = \lambda_{C_1} + \lambda_{C_2}.
$$
> Hence:
$$
\text{MTTF}_S = \frac{1}{\lambda_S} = \frac{1}{\lambda_{C_1} + \lambda_{C_2}} = \frac{1}{\frac{1}{\text{MTTF}_{C_1}} + \frac{1}{\text{MTTF}_{C_2}}}.
$$

> A special case is when we have a series of $n$ components:
$$
\text{MTTF}_S = \frac{1}{\frac{n}{\text{MTTF}_C}} = \frac{\text{MTTF}_C}{n}.
$$

> We can make analogous considerations for the availability:
$$
A_S(t) = A_{C_1}(t) A_{C_2}(t);
$$
> and, in general:
$$
A_S(t) = \prod_{i = 1}^n A_{C_i}(t) = \prod_{i = 1}^n \frac{\text{MTTF}_{C_i}}{\text{MTTF}_{C_i} + \text{MTTR}_{C_i}}.
$$

---

- If **$C_1$ and $C_2$ are connected in parallel**:
$$
R_S(t) = \mathbb{P}(T_S > t) = 1 - \mathbb{P}(T_S \leq t) = 1 - \mathbb{P}(T_{C_1} \leq t) \cdot
$$

$$
\cdot \mathbb{P}(T_{C_2} \leq t) = 1 - (1 - \mathbb{P}(T_{C_1} > t))(1 - \mathbb{P}(T_{C_2} > t)) =
$$

$$
= 1 - (1-R_{C_1}(t))(1-R_{C_2}(t)).
$$

In general:
$$
R_S(t) = 1 - \prod_{i=1}^n(1 - R_{C_i}(t))
$$

Analogously, for the availability we have:
$$
A_S(t) = 1 - \prod_{i=1}^n(1 - A_{C_i}(t)) = 1 - \prod_{i=1}^n \frac{\text{MTTR}_{C_i}}{\text{MTTF}_{C_i} + \text{MTTR}_{C_i}}.
$$

#### Standby redundancy

**Standby redundancy** is a design framework in which we compose a system of two parallel replicas:
- the primary replica, working all the time, and
- the redundant replica, generally disabled, that is activated when the primary replica fails.

Obviously, for such system to work, we need:
- a mechanism to determine whether the primary replica is working properly or not;
- a dynamical switching mechanism to disable the primary replica and activate the redundant one.

---

In general the switching component also could fail and we need to model it. The RBD of the resulting system is a series between the parallel of the two system replicas and the switch.
The system keeps operating in two disjoint cases: either the primary replica doesn't fail, or it does, but the switch works, and the secondary replica doesn't fail in the remaining time. That is:
$$
R_S(t) = \mathbb{P}(T_{\text{primary}} > t) + \int_0^t \mathbb{P}(T_\text{primary} \in [\tau, \tau + d\tau]) \cdot
$$

$$
\cdot \mathbb{P}(\text{the switch works}) \mathbb{P}(T_{\text{replica}} > t - \tau) d\tau .
$$

We can summarize the result in different relevant cases:

<style>

td {
    padding: 2mm;
    text-align: center;
}

</style>

| **Standby Parallel Model**                    | **System Reliability**                                                                                                                                                                                                     |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Equal failure rates,<br>perfect switching     | $R_S = e^{- \lambda_{\text{primary}} t} (1 + \lambda_{\text{primary}} t)$                                                                                                                                                  |
| Unequal failure rates,<br>perfect switching   | $R_S = e^{-\lambda_{\text{primary}} t} +$<br>$+ \lambda_{\text{primary}} \frac{(e^{- \lambda_{\text{primary}} t} - e^{- \lambda_{\text{secondary}} t})}{\lambda_{\text{secondary}} - \lambda_{\text{primary}}}$                  |
| Equal failure rates,<br>imperfect switching   | $R_S = e^{- \lambda_{\text{primary}} t} (1 + R_{\text{switch}} \lambda_{\text{primary}} t)$                                                                                                                                |


---


| **Standby Parallel Model**                    | **System Reliability**                                                                                                                                                                                                     |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unequal failure rates,<br>imperfect switching | $R_S = e^{-\lambda_{\text{primary}} t} +$<br>$+ R_{\text{switch}}\lambda_{\text{primary}} \frac{(e^{- \lambda_{\text{primary}} t} - e^{- \lambda_{\text{secondary}} t})}{\lambda_{\text{secondary}} - \lambda_{\text{primary}}}$ |

More in general, a system may have one primary replica and $n$ redundant replicas.
It holds that, with identical replicas and perfect switching:
$$
R_S(t) = e^{-\lambda t} \sum_{i=0}^{n-1} \frac{(\lambda t)^i}{i!}.
$$

We can have also **$r$ out of $n$** (**RooN**) redundancy, in which a system is composed of $n$ identical replicas where at least $r$ replicas have to work fine for the entire system to work fine. Furthermore, we have a voter component.
For these systems:
$$
R_S(t) = R_{\text{voter}} \sum_{i=1}^r R_C^i(t) (1-R_C(t))^{n-i} \frac{n!}{i!(n-i)!}.
$$

An important special case is **Triple Modular Redundancy** (**TMR**) where $r=2$ and $n = 3$.
For such systems, we can compute through the previous formula that:
$$
R_{\text{TMR}}(t) = R_{\text{voter}}(3 R_C^2(t) - 2 R_C^3(t)).
$$

---

And, by integrating the reliability:
$$
\text{MTTF}_{\text{TMR}} \approx \frac{5}{6} \text{MTTF}_{C}.
$$
Observe that $\text{MTTF}_{\text{TMR}} < \text{MTTF}_{C}$.
