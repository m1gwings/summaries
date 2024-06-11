---
marp: true
theme: summary
math: mathjax
---
# ILP

<div class="author">

Cristiano Migali

</div>

- **Instruction Level Parallelism** (**ILP**) refers to the overlap of execution (_on a processor_) among unrelated instructions.

- We call a **basic block** a straight-line code with no _branches in_ except at the entry and no _branches out_ except at the exit.

The instructions inside a _basic block_ are likely to depend one upon the other: the amount of overlap that we can exploit within a basic block is likely to be less than the average basic block size.
To obtain substantial performance enhancements, we must exploit ILP across multiple basic blocks.

## Dependencies (or conflicts) and hazards

Determining how one instruction depends on another is critical to determining how much parallelism exists in a program and how that parallelism can be exploited. If two instructions are _parallel_, they can execute simultaneously in a pipeline of arbitrary depth without causing any stalls, assuming the pipeline has sufficient resources.

There are 3 different types of dependencies: **data dependencies**, **name dependencies**, and **control dependencies**.

- We say that instruction $j$ is **data dependent** on instruction $i$ if instruction $i$ produces a result that may be used by instruction $j$. [In the course, we call this dependence a **RAW** (**Read After Write**), _even though, on the book, this tem is used to indicate the corresponding hazard (see later)_].

- We say that two instructions are **name dependent** when they use the same register or memory location, called a _name_, but there is no data flow between the two. In particular we can distinguish two types of name dependencies:
> - There is an **antidependence** between instruction $i$ and instruction $j$ (where $j$ comes after instruction $i$ in program order) when instruction $j$ writes a register or memory location that instruction $i$ reads. [In the course, we call this dependence a **WAR** (**Write After Read**)].
> - There is an **output dependence** between instruction $i$ and instruction $j$ if they write the same register or memory location. [In the course, we call this dependence a **WAW** (**Write After Write**)].

- We say that an instruction $i$ is **control dependent** on a _branch instruction_ if the behavior of the branch instruction determines when and if instruction $i$ has to be executed.

---

> **Important**: preserving control dependencies means that instructions which come before a branch in _program order_ will be executed before that branch, and instructions after a branch won't be executed until the branch direction is known. Although preserving control dependencies is a simple way to preserve program order, it is not necessary for program correctness. Indeed program correctness depends on two properties that have to be preserved: the _exception behavior_ (preserving exceptions behavior means that any changes in the ordering of instructions execution must NOT change how exceptions are raised by the program), and _data flow_ (we must preserve the flow of data among instructions specified by the _program order_).

Dependencies are a property of **programs**. Whether a given dependence results in an actual **hazard** being detected and whether that hazard actually causes a stall are properties of the _pipeline organization_.

In particular an **hazard** exists whenever there is a name or data dependence between instructions, and they are close enough that the overlap during execution would change the order of access of the operands involved in the dependence. Because of the dependence we must preserve the _program order_, which is the order in which the instruction would be executed if they were executed sequentially, one at a time, as determined by the original source program.

We can distinguish between 3 kinds of hazards: **data hazards**, **structural hazards**, and **control hazards**.

- **Structural hazards** arise from resource conflicts when the hardware cannot support all possible combinations of instructions simultaneously in overlapped execution.

- **Data hazards** arise when an instruction depends on the results of a previous instruction in a way that is exposed by the overlapping of instructions in the pipeline.

- **Control hazards** arise from the pipelining of branches and other instructions that change the PC.

Hazards in pipelines _can make it necessary to stall the pipeline_. For this reason, hazards have an important effect on the pipeline speedup. Indeed:
$$
\text{pipeline CPI} = \frac{n_{\text{instr.}} \cdot 1 \text{ cycle } + n_{\text{branches}} \cdot \text{ branch penalty } + n_{\text{struct. haz.}} \cdot \text{ struct. haz. penalty }}{n_{\text{instr.}}} +
$$

$$
+ \frac{n_{\text{data haz.}} \cdot \text{data haz. stalls}}{n_{\text{instr.}}} = 1 + f_{\text{branches}} \cdot \text{ branch penalty } + f_{\text{struct. haz.}} \cdot \text{ struct. haz. penalty } + f_{\text{data haz.}} \cdot \text{ data haz. stalls }.
$$

---

## Complex pipeline

ILP arises also if we try to overlap the execution of floating point operations and integer operations: we now want to explore how our MIPS pipeline can be extended to handle floating-point operations.

It is impractical to require that all MIPS FP operations complete in 1 clock cycle, or even in 2. Doing so would mean accepting a slow clock or using enormous amounts of logic in the FP units, or both. Instead, the FP pipeline will allow for a longer latency for operations. This is easier to grasp if we imagine the FP instructions as having the same pipeline as the integer instructions, with two important changes. First, the EX cycle may be repeated as many times as needed to complete the operation (_the number of repetitions can vary for different operations_). Second, there may be multiple FP functional units. A stall will occur if the instruction to be issued will cause either a structural hazard for the functional unit it uses or a data hazard.
Observe that the Functional Units (FUs) for FP operations could be either pipelined (we can overlap the execution of multiple instructions), or simply multi-cycle (they can execute only an instruction at a time and it takes more than one cycle).
We can provide an high level scheme of such architecture:
<p align="center">
    <img src="static/complex-pipeline-no-issue.svg"
    width="500mm" />
</p>

Let's discuss the consequences of having multiple FUs which execute different instructions in parallel.
- Because the instructions have varying running times, the number of registers writes required in a cycle can be larger than 1.

---

- Assuming that the instructions read the operands in the ID stage, and that all instructions go through the ID stage in order, WAR hazards are NOT possible. **Important remark**: this is NOT the architecture used in the complex pipeline exercises of the course, it is just a simpler version, we will see that used in the exercises in a moment and there we can also have WAR hazards.
Conversely, WAW hazards can happen since instructions have different execution times, hence, an instruction which starts after could still finish before w.r.t. another instruction.
- During the ID stage we need to:
> - check for _structural hazards_: we can _issue_ (this is the technical term to be used) an instruction to a FU only if it is NOT busy (observe that the busyness depends if the FU is pipelined or not);
> - check for _RAW hazards_: if there are some, we stall the pipeline until the required data is available;
> - check for _WAW hazards_: if the instruction that we're going to issue could cause a WAW, we will stall the pipeline instead and wait for the other instruction to write.

This architecture has (among the others) one major flaw: at every RAW hazard we stall the entire pipeline even if the following instruction are ready (have all the data) to execute.
We can fix this by splitting the current ID stage in two. **Important remark**: this is the architecture used in the complex pipeline exercises.

The two new stages will be ID (as before) and **Issue** (**IS**). Now the ID stage decodes the instruction and checks for hazards. The Issue stage instead can be seen as a queue of instructions waiting to start their execution (_usually, in the exercises we assume that the queue has unlimited capacity, in reality it could be the case that we must stall the ID stage when we saturate the IS_). In particular the instructions in IS wait for the RAW hazards to be solved, or, in other words, wait for the data of their operands to be written in the register file by other instructions in the pipeline. Observe that this new stage introduces a significative change: now instructions can start their execution NOT in program order, hence WAR hazards are possible.

<p align="center">
    <img src="static/complex-pipeline.svg"
    width="450mm" />
</p>

---

Now:
- instructions are stalled at the ID stage if they cause WARs or WAWs until the conflict is solved;
- instructions in the IS stage wait until any RAW hazard is solved and the required FU is not busy, <u>at every clock only one instruction starts its execution</u>, and, in case multiple instructions are ready, the oldest one will go first;
- as before, it could happen that more than one instruction wants to write and there is only one write port; in this case we stall the execution of all such instructions except one (usually the oldest one), which is let writing.

**Important remark**: in the complex pipeline the register file is split in two: we distinguish between General Purpose Registers (GPR) for integer data, and Floating Point Registers (FPR) for floating point data.

## More advanced techniques to increase ILP

To increase the ILP w.r.t. what we already discuss we can exploit two main families of techniques:
- **static scheduling**, in which we rely on the software to identify the potential parallelism among instructions, and
- **dynamic scheduling**, in which it is the hardware at runtime that identifies parallelism and overlaps instructions execution.

### Static scheduling

#### Very Long Instruction Word (VLIW)

**Very Long Instruction Word** (**VLIW**) processors issue a fixed number of instructions every cycle, formatted as one large instruction word. VLIW processors are inherently statically scheduled by the compiler. The compiler must schedule instructions in order to prevent any data hazard.

In VLIW processors we distinguish between **operations** (an operation is unit of computation, like an addition or load from memory) and **instructions** (an instruction is a set of operations that are intended to be issued simultaneously).

VLIWs use multiple, independent, functional units to run the bundle of operations in parallel. To keep the functional units busy, there must be enough parallelism in a code sequence to fill the available operation slots. Some NOPs are inserted in the instruction otherwise.

**Pros**:
- the HW is simple;
- it is easy to extend the number of FUs;
- good compilers can effectively detect parallelism.

---

**Cons**:
- needs a huge number of registers to store the operands and results of all the different operations;
- requires large data transport capacity between the FUs and the register files and the between the register files and the memory;
- requires high communication bandwidth between the instructions cache and the fetch unit;
- usually increases code size.

#### Static scheduling methods

As we've just seen, the efficiency of architectures like VLIW, which rely on static scheduling, heavily depends on the ability of the compiler to find parallelism among instructions. In this section we will discuss some techniques which allow to rearrange the code in a program, increasing the parallelism and without affecting the correctness.

##### Loop unrolling

**Loop unrolling** is a technique which allows to increase the size of the body of a loop, thus increasing the number of instructions per branch (_the jump at the end of the loop_) and the parallelism. It allows instructions from different iterations to be scheduled together.

It simply consists in replicating the loop body multiple times, adjusting the termination code. That is, the new loop body corresponds to $k$ copies of the original body. Usually some optimizations are applied to the new body, for example, instead of incrementing the loop variable $k$ times, we increment it once by $k$; and, <u>more important</u> we move instructions as to distantiate as possible those who share a dependency.
Observe that we don't know a priori that the number of times a loop has to be executed, let's call it $n$, is a multiple of $k$. For this reason, to preserve program correctness, a loop is usually transformed in two loops: the first with the large body consisting in $k$ copies of the original one, which is executed $\lfloor \frac{n}{k} \rfloor$ times, the second has as body the body of the original loop and is executed $n \mod k$ times.

##### Software pipelining

**Software pipelining** is a technique for reorganizing loops such that each iteration in the software-pipelined code is made from instructions chosen from different iterations of the original loop. By choosing instructions from different iterations, dependent computations are separated from one another by an entire loop body, increasing the possibility that the unrolled loop can be scheduled without stalls. A software-pipelined loop interleaves instructions from different iterations without unrolling the loop, but often the two techniques are used together.

Loop unrolling reduces the overhead of the loop: the branch and the counter update code. Software pipelining reduces the time when the loop is not running at peak speed (when we have the maximum amount of parallelism among the instructions of each iteration) tto once per loop at the beginning and at the end.

---

Indeed software pipelining, in order to preserve program correctness, requires some start-up and wind-down code where usually the amount of parallelism among instructions is not maximum.
In simple loop unrolling instead we pay this time at suboptimal speed once per iteration.

##### Trace scheduling

**Trace scheduling** is a code motion technique which aims at simplifying scheduling and increasing parallelism on frequent "_paths_" in the program by increasing the cost of the infrequent ones. Because it can generate significant overhead on the designated infrequent path, it is best used when accurate profile information is available. It allows to increase the parallelism also in absence of loops (i.e. when we can't apply loop unrolling or software pipelining).

Trace scheduling consists of two steps: **trace selection** and **trace compaction**.

- A **trace** is a loop-free sequence of basic blocks embedded in the control flow graph.

In _trace selection_ we identify the most frequent executed traces in out program. We will try to schedule this sequence of basic blocks together as if they were one basic block (no special consideration for branches); of course, as anticipated, this will require to add additional code on infrequent paths to preserve program correctness.
Once a trace is selected, _trace compaction_ tries to squeeze the trace into a small number of wide instructions.

In trace scheduling, branches are seen as jumps into or out the selected trace. When code is moved across such trace entry and exit points, additional book-keeping code will often be needed on the entry or exit point.
Let's see two examples.

- **Moving an instruction below a side exit**

<p align="center">
    <img src="static/trace-scheduling-side-exit.svg"
    width="500mm" />
</p>

- **Moving an instruction below a side entry**

<p align="center">
    <img src="static/trace-scheduling-side-entry.svg"
    width="500mm" />
</p>

---

Some variants of trace scheduling allows to simplify this compensation code generation. An example is **superblock scheduling**: a _superblock_ is a special trace with a single entry point and, potentially, many exit points.

##### Predicated execution

**Conditional** or **predicated instructions** are an extension to the ISA which allows to expose more parallelism. These instructions can be used to eliminate branches, converting a control dependence into a data dependence and potentially improving performance.

The concept behind conditional instructions is quite simple: an instruction refers to a condition, which is evaluated as part of the instruction execution. If the condition is true, the instruction is executed normally; if the condition is false, the execution continues as if the instruction were a no-op-
The most common example of such an instruction is the conditional move.

##### Rotating register file

Resume...

### Dynamic scheduling

In **dynamic scheduling**, the hardware reorders the instructions execution to reduce pipeline stalls while maintaining data flow and exception behavior.
The main advantages of this approach are that:
- it enables handling some cases where dependencies are unknown at compile time;
- it reduces the compiler complexity;
- it allows compiled code to run efficiently on a different pipeline.

These advantages are gained at a cost:
- a significant increase in hardware complexity;
- increased power consumption;
- possible generation of imprecise exception.