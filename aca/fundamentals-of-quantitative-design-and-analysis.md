---
marp: true
theme: summary
math: mathjax
---
# Fundamentals of quantitative design and analysis

<div class="author">

Cristiano Migali

</div>

## Classes of computers

We can distinguish 5 main _classes_ of computing environments:
- **Personal mobile devices** (**PMDs**);
- **Desktop computers**;
- **Servers**;
- **Clusters**/**Warehouse Scale Computers** (**WSCs**);
- **Embedded computers**.

### Personal mobile devices

_Personal mobile device_ (PMD) is the term we apply to a collection of wireless devices with multimedia user interfaces such as cell-phones, tablets, and so on.
Cost is the main concern for this class of computing systems, but there is also emphasis on energy efficiency since these devices are battery powered. The applications running on PMDs are often Web-based and media-oriented.

### Desktop computers

Desktop computers constitute the largest market share in dollar terms. They span from low-end notebooks, to high-end, heavily configured workstations. The desktop market tends to be driven to optimize _price-performance_.

### Servers

Servers have become the backbone of large-scale enterprise computing, replacing the traditional mainframe. The role of servers is to provide larger-scale, more reliable, file and computing services.
The most important features that servers have to provide are _availability_, _scalability_, and _throughput_.

### Clusters/Warehouse Scale Computers

Clusters are a collection of desktop computers or servers connected by local are networks to act as a single larger computer. Each node runs its own operating system, and nodes communicate using a networking protocol. The largest of the clusters are called Warehouse Scale Computers.

---

### Embedded computers

Embedded computers are a very general class: they are computing devices with a dedicated function within a larger system. We use the ability to run third-party software as the dividing line between non-embedded and embedded computers.

## Classes of parallelism

Inside _applications_ we can identify two kinds of parallelism:
- **Data-Level Parallelism** (**DLP**): it arises because there are many data items that cen be operated at the same time.
- **Task-Level Parallelism** (**TLP**): it arises because tasks of work are created that can operate independently and largely in parallel.

_Computer hardware_ in turn can exploit these two kinds of application parallelism in four major ways:
- **Instruction-Level Parallelism** (**ILP**): it exploits DLP at modest levels using ides like pipelining and at medium levels using ideas like speculative execution.
- **Vector architectures**: exploit DLP by applying a single instruction to a collection of data in parallel.
- **Thread-Level Parallelism**: exploits either DLP or TLP in a tightly coupled hardware model that allows for interaction among parallel threads.
- **Request-Level Parallelism**: exploits parallelism among largely decoupled tasks specified by the programmer or the operating system.

## Classes of parallel architectures: the Flynn's taxonomy

We can classify computer architectures w.r.t. how they handle parallelism considering two axes: the instruction stream and the data stream. This results in 4 classes which constitute **Flynn's taxonomy**.
- **Single instruction stream, Single data stream** (**SISD**): this category is the uni-processor, i.e. the standard sequential computer;
- **Single instruction stream, Multiple data stream** (**SIMD**): the same instruction is executed by multiple processors using different data streams. SIMD computers exploit DLP by applying the same operations to multiple items of data in parallel. Each processor has its own data memory.
- **Multiple instruction stream, Single data stream** (**MISD**): no commercial multiprocessor of this type has been built up to data.
- **Multiple instruction streams, Multiple data streams** (**MIMD**): each processor fetches its own instructions and operates on its own data, exploiting TLP. In general, MIMD is more flexible than SIMD and thus more generally applicable, but it is also inherently more expensive.

---

## Measuring performance

- We define **response time** or **execution time** the time between the start and the completion of a task.

- We define **throughput** the number of tasks completed in a certain unit of time.

- Given a task $T$ and two computer architectures $X$ and $Y$, we say that $X$ is $n$ times faster than $Y$ (_on task $T$_) with the meaning:
$$
\frac{\text{execution time}_Y}{\text{execution time}_X} = n.
$$

- We define **performance** the reciprocal of the execution time:
$$
\text{performance}_X = \frac{1}{\text{execution time}_X}.
$$
> It follows that, if $X$ is $n$ times faster than $Y$, then:
$$
\frac{\text{performance}_X}{\text{performance}_Y} = n.
$$

### Amdahl's law

**Amdahl's law** provides a way to compute the overall gain in performance due to the enhancement of one component of a computing system.

- We define **speedup** the ratio between the performance of a system or component $X$ with an enhancement and the original performance:
$$
\text{speedup}_X = \frac{\text{performance}_{X \text{ enhanced}}}{\text{performance}_X}.
$$

Let $S$ be a system whose component $C$ has been enhanced. Assume that $C$ is used for $\text{fraction}_C$ of $\text{execution time}_S$.
Since we lessen only the time during which $C$ is used:
$$
\text{execution time}_{S \text{ enhanced}} = (1-\text{fraction}_C) \text{ execution time}_S + \text{fraction}_C \text{ execution time}_S \cdot
$$

$$
\cdot \frac{\text{execution time}_{C \text{enhanced}}}{\text{execution time}_C} = \text{execution time}_S \ (1 - \text{fraction}_C + \frac{\text{ fraction}_C}{\text{ speedup}_C}).
$$

Finally:
$$
\text{speedup}_S = \frac{\text{execution time}_S}{\text{execution time}_{S \text{ enhanced}}} = \frac{1}{1 - \text{fraction}_C + \frac{\text{ fraction}_C}{\text{ speedup}_C}}.
$$

---

### The Processor Performance Equation

Essentially all (_digital_) computers are constructed using a clock running at a constant rate. Computer designers refer to the time of a clock period by its duration $T_{\text{clock}}$ or by its rate $f_{\text{clock}}$.
Hence we have two ways to compute the CPU time $T_{\text{CPU}}$ of a program.
$$
T_{\text{CPU}} = N_\text{clock cycles} T_{\text{clock}}
$$
or:
$$
T_{\text{CPU}} = \frac{N_{\text{clock cycles}}}{f_{\text{clock}}}.
$$

In addition to the number of clock cycles needed to execute a program, we can also count the number of instructions executed: the _instruction path length_ or _**instruction count**_ $\text{IC}$.

If we know the number of clock cycles and the instruction count, we can calculate the average number of _clock cycles per instruction_ $\text{CPI}$. Designer sometimes also use _instructions per clock_ $\text{IPC} = \frac{1}{\text{CPI}}$.
Observe that the $\text{CPI}$ can be computed as:
$$
\text{CPI} = \frac{N_{\text{clock cycles}}}{\text{IC}}.
$$
Hence, by rearranging the above formula:
$$
N_{\text{clock cycles}} = \text{CPI} \cdot \text{IC}.
$$
Finally, if we plug this result in the formula of $T_{\text{CPU}}$, we get:
$$
T_{\text{CPU}} = \text{CPI} \cdot \text{IC} \cdot T_{\text{clock}}.
$$
AS this formula demonstrates, processor performance is equally dependent on 3 characteristics. Unfortunately, it is difficult to change one parameter in complete isolation from others.
