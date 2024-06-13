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

In order to reduce the name dependencies among the instructions of different iterations of a loop, we can adopt a **rotating register file**. In a rotating register file, registers are split into rotating and non-rotating.
Rotating registers are used for the instructions in loop bodies. In particular, the actual address of the physical rotating register is obtained by adding the address of the virtual register, specified in the code, to the value of the **Rotating Register Base** (**RRB**) which points at the base of the register set for the current iteration. Of course this value is incremented (or decremented) at each iteration to prevent WAR and WAW hazards, maximizing the parallelism among different iterations.

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

---

#### Scoreboard (CDC 6600)

The **Scoreboard** (**CDC 6600**) is an evolution of the complex pipeline architecture, which aims at increasing ILP by reducing the number of stalls due to conflicts arising from name dependencies. Indeed, in the complex pipeline (_with IS stage_) that we described, all the instructions causing WAR or WAW hazards are stalled in the ID stage, causing a stall also for all the instructions that follow.
We can't do otherwise since, without further checks, executing such instructions out of order could corrupt the data flow and hence the correctness of a program.
In Scoreboard we improve the parallelism by <u>allowing out of order execution of instructions causing WAR hazards</u>, while we still have to stall instructions causing WAW hazards (_later you can find a disappointing comment about this_). This is achieved by introducing a **centralized scheduler** which keeps track of all the relevant information of the instructions executing in the pipeline. Thanks to this information we can stall the write-back of instructions causing WAR hazards until the previous data that will be overwritten is read by all those who need it.

In the Scoreboard architecture there are 4 stages (excluding the IF and ID stages).
1. **Issue**: if a functional unit for the instruction is free and the instruction does not cause a WAW (i.e., there is no other active instruction that has the same destination register), then the Scoreboard issues the instruction to the functional unit and <u>updates its internal data structure</u>. As in the complex pipeline with IS stage, we can have multiple instructions in the issue stage in a queue. If a structural or WAW hazard exists, the instruction issue stalls, and no further instructions will issue until the hazards are clear (i.e. we have in order issue). If we DON'T assume that the queue has unlimited capacity, we have to stall also the fetch when we reach saturation.
2. **Read operands**: the scoreboard monitors the availability of the source operands. A source operand is available if no earlier issued active instruction is going to write it. When the source operands are available, the scoreboard tells the functional unit to proceed to read the operands from the registers and begin the execution. The scoreboard resolves RAW hazards dynamically in thi step, and instructions may be sent into execution out of order.
3. **Execution**: the functional unit begins execution upon receiving operands. When the result is ready, it notifies the scoreboard that it has completed execution.
4. **Write result**: once the Scoreboard is aware that the functional unit has completed execution, the Scoreboard checks for WAR hazards and stalls the completing instruction if necessary. If there is no WAR hazard the Scoreboard tells the functional unit to store its result to the destination register.

**Important remark**: since we have to go through the centralized scheduler, it is NOT possible to overlap _read operands_ and _write result_ to solve a RAW hazard as in the simple 5 stages MIPS pipeline. That is, the reading instruction will complete the _read operands_ in the cycle <u>after</u> the _write result_ of the writing instruction involved in the RAW.

---

Let's go into the details of the information used by Scoreboard.
1. **Instruction status**: indicates which of the four steps the instruction is in.
2. **Functional unit status**: indicates the state of the FU. There are nine fields for each functional unit:
> - _Busy_: indicates whether the unit is busy or not;
> - _Op_: it is the operation to perform in the unit (e.g. _ADD_, or _SUB_);
> - _Fi_: the destination register;
> - _Fj, Fk_: the source register numbers;
> - _Qj, Qk_: functional units producing source registers Fj, Fk;
> - _Rj, Rk_: flags indicating when Fj, Fk are ready and not yet read. Set to No after operands are read.
3. **Register result**: indicates which functional unit will write each register, if an active instruction has the register as its destination. This field is set to blank whenever there are no pending instructions that will write that register.

Observe that:
- We can check if there is a WAW hazard by looking if the _register result_ slot for the destination register of the instruction in the IS stage is empty or not.
- We can check if there is a RAW hazard by looking if the _register result_ slots for the source registers of the instruction in the IS stage are empty or not, we will set Qj, Qk, Rj, and Rk consequently.
- Let f be the FU of the current instruction in the _write result_ stage, we can check if there is a WAR hazard or not by checking if in the _functional unit status_ table we have a functional unit f' s.t. (Fj(f') = Fi(f) and Rj(f') = Yes) or (Fk(f') = Fi(f) and Rk(f') = Yes) (_if this condition is satisfied WE HAVE A WAR_).
Observe that here we assume that if for example Fk(f') != Fi(f), but Fj(f') = Fi(f) and Rj(f') = No we DO NOT HAVE A WAR and we can write. This is due to the fact that, if Fj(f') = Fi(f) and Rj(f') = No, either the instruction in f' has already read or it is waiting for the result produced by f, which, since we stall instructions causing WAW hazards, is the only functional unit which writes in Fi(f).
I think that it is also possible to make the WAR check a bit more complicated by considering also Qj(f'), Qk(f') and if the instruction in f' has already read (from the instruction status), removing the need of stalling WAWs. Indeed, _according to Wikipedia_, the only reason why Scoreboard doesn't handle WAW hazards, is because its architects had to deliver the product.

---

#### Tomasulo

**Tomasulo** architecture is an improvement w.r.t. Scoreboard since it is capable not only of handling RAW and WAR, but also WAW hazards.
RAW hazards are avoided by executing an instruction only when its operands are available, which is exactly what the simpler Scoreboard approach provides.
WAR and WAW hazards, which arise from name dependencies, are eliminated by **implicit register renaming**. _Register renaming_ eliminates these hazards by renaming all destination registers, including those with a pending read or write for an earlier instruction, so that the out-of-order write does not affect any instructions that depend on an earlier value of the operand. In Tomasulo's scheme, register renaming is provided by _reservation stations_, which buffer the operands of instructions waiting to issue. The basic idea is that a reservation station fetches and buffers an operand as soon as it is available, eliminating the need to get the operand from a register. In addition, pending instructions designate the reservation station that will provide their input. Finally, when successive writes to a register overlap in execution, only the last one is actually used to update the register (_thus reducing also power consumption by minimizing useless bit flips_). As instructions are issued, the register specifiers for pending operations are renamed to the names of the reservation station, which provides register renaming.
Since there can be more reservation stations that real registers, the technique can even eliminate hazards arising from name dependencies that could not be eliminated by a compiler.
The use of reservation stations, rather than a centralized register file, leads to two other important properties. First, hazard detection and execution control are distributed: the information held in the reservation stations at each functional unit determines when an instruction can begin execution at that unit. Second, results are passed directly to functional units from the reservation stations where they are buffered, rather than going through the registers. This bypassing is done with a common result bus that allows all units waiting for an operand to be loaded simultaneously; this is called **Common Data Bus** (**CDB**).

In Tomasulo (excluding IF and ID stages) there are only 3 stages.
1. **Issue**: get the next instruction from the head of the instruction queue, which is maintained in FIFO order (_i.e., we have in order issue_) to ensure the maintenance of correct data flow. If there is a matching reservation station that is empty, issue the instruction to the station with the operand values, if they are currently in the registers. If there is not an empty reservation station, then there is a structural hazard and the instruction stalls until a station or buffer is freed. If the operands are not in the registers, keep track of the functional units that will produce the operands. This step renames registers, eliminating WAR and WAW hazards.
2. **Execute**: if one or more of the operands is not yet available, monitor the common data bus while waiting for it to be computed. When an operand becomes available, it is placed into any reservation station awaiting it. When all the operands are available, the operation can be executed at the corresponding functional unit. By delaying instruction execution until the operands are available, RAW hazards are avoided.

---

> Notice that several instructions could become ready in the same clock cycle for the same functional unit. Although independent functional units could begin execution in the same clock cycle for different instructions, if more than one instruction is ready for a single functional unit, the unit will have to choose among them.

**Important remark**: to preserve exception behavior, no instruction is allowed to initiate execution until all branches that precede the instruction in program order have completed. This restriction guarantees that an instruction that causes an exception during execution really would have been executed. In a processor using branch prediction, this means that the processor must know that the branch prediction was correct before allowing an instruction after the branch to begin execution.
As we will see, speculation provides a more flexible and more complete method to handle exceptions, so we will delay making this enhancement and show how speculation handles this problem later.

3. **Write result**: when the result is available, write it on the CDB and from there into the registers and into any reservation stations waiting for this result.

Let's discuss the data structures used to implement implicit register renaming.
Each reservation station has seven fields:
- _Op_: the operation to perform on source operands S1 and S2;
- _Qj, Qk_: the reservation stations that will produce the corresponding source operand; a value of zero indicates that the source operand is already available in Vj or Vk, or is unnecessary;
- _Vj, Vk_: the value of the source operands. Note that only one of the V fields or the Q fields is valid for each operand;
- _A_: used to hold information for the memory address calculation for a load or store. Initially, the immediate field of the instruction is stored here, after the address calculation, the effective address is stored here;
- _Busy_: indicates that this reservation station and its accompanying functional unit are occupied.

The register file has a field:
- _Qi_: the number of the reservation station that contains the operation whose result should be stored into this register. If the value of Qi is blank, no currently active instruction is computing a result destined to this register, meaning that the value is simply the register contents.

**Remark on loads and stores**: loads and stores require a two-step execution process. The first step computes the effective address when the base register is available, and the effective address is the placed in the load or store buffer. Loads in the load buffer execute as soon as the memory unit is available. Stores in the store buffer wait for the value to be stored before being sent to the memory unit. Loads and stores are maintained in program order through the effective address calculation, which will help to prevent hazards through memory.

---

#### Hardware-based speculation

As we try to exploit more instruction-level parallelism, maintaining control dependencies becomes an increasing burden. Overcoming control dependence is done by speculating on the outcome of branches and executing the program as if our guesses were correct. This mechanism represents a subtle, but important, extension over branch prediction with dynamic scheduling. In particular, with speculation, we fetch, issue, and _execute_ instructions, as if our branch predictions were always correct; dynamic scheduling only fetches and issues such instructions. Of course, we need mechanisms to handle the situation where the speculation is incorrect.

Hardware-based speculation combines 3 key ideas: dynamic branch prediction to choose which instructions to execute; speculation to allow the execution of instructions before the control dependencies are resolved; dynamic scheduling to deal with the scheduling of different combinations of basic blocks.
To extend Tomasulo's algorithm to support speculation, we must separate the bypassing of results among instructions, which is needed to execute an instruction speculatively, from the actual completion of an instruction. By making this separation, we can allow an instruction to execute and to bypass its results to other instructions, without allowing the instruction to perform any updates that cannot be undone, until we know that the instruction is no longer speculative.
When an instruction is no longer speculative, we allow it to update the register file or memory; we call this additional step in the instruction execution sequence: _instruction commit_.
The key idea behind implementing speculation is to allow instructions to execute out of order but to force them to commit _in order_ and to prevent any irrevocable action until an instruction commits. Hence, when we add speculation, we need to separate the process of completing execution from instruction commit, since instructions may finish execution considerably before they are ready to commit. Adding this commit phase to the instruction execution sequence requires an additional set of hardware buffers that hold the results of instructions that have finished execution but have not committed. This hardware buffer, which we call the **ReOrder Buffer** (**ROB**), is also used to pass results among instructions that may be speculated.
The ROB holds the result of an instruction between the time the operation associated with the instruction completes and the time the instruction commits. Hence, the ROB is a source of operands for instructions, just as the reservation stations provide operands in Tomasulo's algorithm. The key difference is that in Tomasulo's algorithm, once an instruction writes its result, any subsequent instructions will find the result in the register file. With speculation, the register file is not updated until the instruction commits, thus, the ROB supplies operands in the interval between completion of instruction execution and instruction commit.
The ROB is similar to the store buffer in Tomasulo's algorithm, and we integrate the function of the store buffer into the ROB for simplicity.

---

Each entry of the ROB contains 4 fields:
- the instruction type: it indicates if the instruction is a branch;
- the destination field: either the register number or the memory address where the instruction result should be written;
- the value field: the value of the instruction result;
- the ready field: indicates that the instruction has completed execution, and the value is ready.

Here we list the 4 stages (excluding IF and ID) of Tomasulo + Hardware-based speculation.
1. **Issue**: get an instruction from the instruction queue. Issue the instruction if there is an empty reservation station and an empty slot in the ROB; send the operands to the reservation station if they are available in either the registers or the ROB. _In the course we treat the ROB as a **circular queue** when we assign new slots or empty them during commits_. Update the control entries to indicate the buffers are in use. The number of the ROB entry allocated for the result is also sent to the reservation station, so that the number can be used to tag the result when it is placed on the CDB. If either all reservations are full or the ROB is full, then instruction issue is stalled until both have available entries.
2. **Execute**: if one or more of the operands is not yet available, monitor the CDB while waiting for the register to be computed. This step checks for RAW hazards. When both operands are available at a reservation station, execute the operation.
3. **Write result**: when the result is available write it on the CDB (with the ROB tag sent when the instruction issued) and from the CDB into the ROB, as well as to any reservation stations waiting for this result. Mark the reservation station as available. 
4. **Commit**: this is the final stage of completing an instruction, after which only its result remains. There are three possible behaviors:
> - **Normal commit**: the instruction at the head of the ROB (_remember that we treat it as a circular queue_) is not a store. The corresponding result slot has been filled. Then we can store the result in the register file and remove the entry from ROB (_we increase the head address_);
> - **Store commit**: the instruction at the head of the ROB is a store. We behave like in normal commit, but writing to memory instead of to the register file.
> - **Instruction is a branch with incorrect prediction**: it indicates that the speculation is wrong. The ROB is flushed (all the results of speculative instructions after the miss-predicted branch are removed) and execution restarts at the correct successor of the branch.