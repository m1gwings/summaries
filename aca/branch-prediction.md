---
marp: true
theme: summary
math: mathjax
---
# Branch prediction

<div class="author">

Cristiano Migali

</div>

## Reducing branch penalties of the MIPS naive implementation

In the naive version of the MIPS pipelined architecture, branch instructions cause a significant loss in throughput.
Indeed, in such architecture, the execution of a branch works as follows:
1. in the IF stage the branch instruction is fetched;
2. in the ID stage we decode the branch instruction and stall the IF stage: we don't know the address of the next instruction to fetch until we resolve the branch;
3. in the EX stage we compute the **Branch Target Address** (**BTA**) by adding the sign extended immediate of the branch instruction to $\text{PC}+4$ and perform the comparison required to assess the outcome of the branch condition;
4. in the MEM stage, depending on the result of the comparison carried out during the previous stage, we store either the $\text{BTA}$ or $\text{PC}+4$ into the PC;
5. finally, during the WB stage we resume the IF stage and start fetching the next instruction.

Hence, in this implementation, every branch instruction causes **3 stalls**.
We can also measure the impact on the pipeline speedup. (_We will assume that the un-pipelined architecture has the same clock cycle of the pipelined one, but with an higher CPI, in particular: $\text{CPI}_{\text{un-pipelined}} = \text{pipelined depth}$, $\text{CPI}_{\text{pipelined}} = 1$ when there are no branches. This is equivalent to assuming that the un-pipelined version has an higher clock period, but the former is the usual implementation_).

$$
\text{pipeline speedup} = \frac{\text{instruction time}_{\text{un-pipelined}}}{\text{instruction time}_{\text{pipelined}}} = \frac{\text{CPI}_{\text{un-pipelined}} \cdot \text{clock period}}{\text{CPI}_{\text{pipelined}} \cdot \text{clock period}} =
$$
$$
= \frac{\text{pipeline depth} \cdot \text{clock period}}{(1 + \text{branch frequency} \cdot \text{branch penalty}) \cdot \text{clock period}} = \frac{\text{pipeline depth}}{1+\text{branch frequency} \cdot \text{branch penalty}}.
$$

### Naive optimization: assuming branch always untaken

**Remember**: we call **taken branch** a branch which changes the PC to its target address; otherwise we say that the **branch** is **untaken**.
The first naive optimization that we can make is to assume always that the branch in untaken until we know the actual result. Hence, instead of stalling the IF for the next instruction, we can fetch that at $\text{PC}+4$ and continuing the execution. If at the MEM stage we notice that we made the wrong choice, we can flush all the pipeline stages before MEM. At the next cycle we will fetch the right instruction at the BTA.

---

### Forwarding

To reduce by 1 the branch penalty of taken branches we can exploit forwarding: we can forward the address of the next instruction from the EX stage of the branch. In this way, even when the branch is taken, we will fetch the right instruction **while** the branch is in the MEM stage, that is, after only **2 stalls**.

### Early evaluation of the PC

The operations required to compute the BTA and evaluate the condition of a branch are very light: we can execute them in half a cycle. Hence we can modify our architecture to carry them out **during the ID stage**. (_Remember that the register file is written on a different clock edge w.r.t. to the one which makes the inter-stage registers to commute; hence the data required by the branch could be written in the middle of the ID stage and we must be able to compute the BTA and evaluate the branch condition in just half a cycle_). Then we can forward the results from the ID stage. In this way a branch instruction causes only **1 stall**.

Anyways, this comes with **a cost**: if one of the operands of the branch is produced by the previous instruction during the EX stage, we can't exploit EX/EX forwarding anymore (since we've anticipated the computation at the ID stage) and we need also to stall 1 cycle to wait for the data to be computed.

## Branch prediction

**Branch prediction** techniques try to reduce the branch penalty by predicting the outcome of a branch condition before the actual result is computed.
We can distinguish between two main families of branch prediction techniques:
- **Static branch prediction techniques**: the actions for a branch are fixed for each branch during the entire execution. They are determined at compile time.
- **Dynamic branch prediction techniques**: the decision causing the branch prediction can change during the program execution.

In both cases, care must be taken not to change the processor state until the branch is definitely known.

### Static branch prediction

**Static branch prediction** is used in processors where the expectation is that the branch behavior is highly predictable at compile time. They can also be used to assist dynamic predictors.

We will discuss 5 static branch prediction techniques:
- **Branch Always Not Taken**;
- **Branch Always Taken**;
- **Backward Taken Forward Not Taken** (**BTFNT**);

---

- **Profile-Driven prediction**;
- **Delayed branch**.

#### Branch Always Not Taken (Predicted-Not-Taken)

The **Branch Always Not Taken** technique coincides with the first naive optimization that we introduced for the MIPS pipeline: we assume the **branch will not be taken**. thus the sequential instruction flow we have fetched can continue as if the branch condition was not satisfied.

If the condition in the ID stage will result not satisfied (**the prediction is correct**), we can preserve performance.
Otherwise (**the prediction is incorrect**) we need to flush the next instruction already fetched and we restart the execution by fetching the instruction at the BTA (**1 cycle of penalty**).

#### Branch Always Taken

An alternative scheme is to consider every branch as taken: as soon as the branch is decoded and the BTA is computed, we assume the branch to be taken and we begin fetching and executing the target.

**Important remark**: the predicted-taken scheme makes sense for pipelines where the branch target is known before the branch outcome. In MIPS pipeline, we don't know the BTA earlier than the branch outcome, so there is no advantage in this approach for this pipeline.

#### Backward Taken Forward Not Taken (BTFNT)

In this technique, the prediction is based on the branch direction:
- _backward-going_ branches ($\text{BTA} < \text{PC}$) are predicted as taken;
- _forward-going_ branches are predicted as not taken.

This technique makes sense when we think about loops: the jump at the end of a loop to go back and start the next iteration is a _backward-going_ branch which is taken most of the time.

#### Profile-Driven Prediction

In this technique, the branch prediction is based on profiling information collected from earlier runs.

#### Delayed Branch

We call **branch delay slots** the cycles, after the fetch of a branch instruction, during which we still don't know the actual address of the next instruction to fetch. In the optimized MIPS pipeline, we have one delay slot.

---

The **delayed branch** technique consists in scheduling in the branch delay slot an instruction which has to be executed, no matter the outcome of the branch condition.
The _job of the compiler_ is to make the instruction placed in the branch delay slot **valid** (we must preserve program correctness) and useful.

There are three ways in which the branch delay slot can be scheduled:
- **from before**;
- **from target**;
- **from fall-through**.

##### Delayed Branch From Before

In this case, the branch delay slot is scheduled with an independent instruction from before the branch. The instruction in the branch delay slot **has always to be executed**.
Observe that the branch condition must not depend on the outcome of such instruction for this scheduling to be valid.

##### Delayed Branch From Target

In this case, the branch delay slot is scheduled with an instruction from the target of the branch. This strategy is preferred when the branch is taken with high probability, for example in loops.
Observe that the optimization has to be legal: it must be OK to executed the moved instruction when the branch goes in the unexpected direction. This can happen for example when the destination register of such instruction is an unused temporary register if the branch goes in the unexpected direction.

##### Delayed Branch From Fall-through

In this case, the branch delay slot is scheduled from the not-taken fall-through path. This strategy is preferred when the branch is not taken with high probability.
Also in this case we have to make sure that the optimization is legal.

### Dynamic branch prediction

In **dynamic branch prediction** we use the hardware to dynamically predict the outcome of a branch: the prediction will depend on the behavior of the branch at run time and will change if the branch changes its behavior during execution.
Dynamic branch prediction is based on **two interacting** mechanisms:
- **Branch Outcome Predictor**: to predict the direction of a branch (i.e. _taken_ or _not taken_);
- **Branch Target Predictor** (**BTP**): to predict the BTA in case of taken branch.

These modules are used by the Instruction Fetch Unit to predict the next instruction to read in the Instruction cache: if the branch is predicted as not taken, then the PC is incremented, otherwise we fetch the instruction at the address provided by the BTP.

---

#### Branch Target Buffer

The **Branch Target Buffer** (**BTB**) is a way of implementing a **Branch Target Predictor**. It consists in a cache storing the predicted BTA. We access the BTB in the IF stage using the lower bits (_for cache sizing reasons_) of the instruction address of the fetched instruction (_a possible branch_) to index the cache. A typical entry of the BTB has two fields: the **exact address of the branch** (_remember, since we're indexing through the lower bits, there could be conflicts between different branches and we must be able to identify them_), and the **predicted BTA**. The predicted BTA is expressed as an offset from the PC. As usual in caches, there are also some validity bits to distinguish valid entries from invalid ones.

#### Branch history Table

The **Branch History Table** (**BHT**) (or Branch Prediction Buffer) is a way of implementing a **Branch Outcome Predictor**. The simplest version consists in a table containing 1 bit for each entry that says whether the branch was recently taken or not. As for the BTB, the table is indexed by the lower portion of the address of the branch instruction.
As opposed to what happens for BTB, this table doesn't store the exact address of the branch instruction (every access is a hit)m hence the prediction bit could have been put there by another branch with the same low-order address-bits. At the end it is not a big deal, the prediction is just an hint.

If we use $k$ bits to index the BHT, then we will have $2^k$ entries.

The behavior of this simple 1 bit BHT is determined by the following state machine.

<p align="center">
    <img src="static/1bit-bht-state-machine.svg"
    width="300mm" />
</p>

A more accurate version of the BHT uses 2 bits for entry instead of one: _the prediction must miss twice before it is changed_.
The behavior can be again described by a state machine:
<p align="center">
    <img src="static/2bit-bht-state-machine.svg"
    width="300mm" />
</p>

---

Observe that this implementation uses twice the memory w.r.t. the 1 bit BHT.

Finally, we can generalize this architecture to an $n$-bit history table implemented through an $n$-bit _saturating counter_ for each entry in the table. The counter can take on values between 0 and $2^n - 1$. When the counter is greater than or equal to one-half of its maximum value $2^n-1$, the branch is predicted as taken. Otherwise, it is predicted as untaken.

#### Correlating Branch Predictors

BHT predictors use only the (recent) behavior of a **single** branch to predict the future behavior of that branch. The basic idea behind **Correlating Branch Predictors** is that the behavior of recent branches is correlated. That is, the recent behavior of other branches other than the current branch can influence the prediction of the outcome of the current branch condition.
In particular, an $(m, n)$ Correlating Branch Predictor records the outcome of the last $m$ branches and uses them to choose from $2^m$ $n$-bits BHTs.
An analogous way of achieving the same behavior is by indexing the BHT by a concatenation of low-order bits from the branch address plus $m$ bits of _global history_ (i.e. the outcome of the $m$ most recent branches).
This BHT has $2^{k+m}$ (where $k$ is the number of lower bits of the branch address used for indexing) entries, each of which occupies $n$ bits.

Usually $(2, 2)$ Correlating Branch Predictors are significantly more efficient than 2-bit BHTs.
