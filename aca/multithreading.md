---
marp: true
theme: summary
math: mathjax
---
# Multithreading

<div class="author">

Cristiano Migali

</div>

- **Multithreading** allows multiple threads to share the functional units of a single processor in an overlapping fashion, duplicating only the private state of each thread: the registers and the program counter.

Although increasing performance by using ILP has the great advantage that it is reasonably transparent to the programmer, as we have seen ILP can be quite limited or difficult to exploit in some applications. In particular, with reasonable instruction issue rates, cache misses are unlikely to be hidden by available ILP. Of course, when the processor is stalled waiting on a cache miss, the utilization of the functional units drops dramatically.
_Multithreading_ answers to this problem by exploiting explicitly the natural parallelism which characterizes many applications (online transactions, ...).
For multithreading to be efficient, the hardware must support the ability to change to a different thread relatively quickly: in particular, a thread switch should be much more efficient than a process switch.

## Hardware approaches to multithreading

There are 3 main **hardware approaches** to multithreading:
- **fine-grained multithreading**;
- **coarse-grained multithreading**;
- **simultaneous multithreading** (**SMT**).

### Fine-grained multithreading

**Fine-grained multithreading** switches between threads on each clock, causing the execution of instructions from multiple threads to be interleaved. This interleaving is often done in a round.robin fashion, skipping any threads that are stalled at that time.

**Advantages**:
- It can hide the throughput losses that arise from both short and long stalls, since instructions from other threads can be executed when one thread stalls, even if the tall is only for a few cycles.

**Disadvantages**:
- It slows down the execution of an individual thread, since a thread that is ready to execute without stalls will be delayed by instructions from other threads. It trades an increase in multithreaded throughput for a loss in performance of a single thread.

---

### Coarse-grained multithreading

**Coarse-grained multithreading** switches threads only on costly stalls, such as level two ot three cache misses.

**Advantages**:
- It relieves the need to have thread-switching be essentially free.
- It is much less likely to slow down the execution of any one thread, since instructions from other threads will only be issued when a thread encounters a costly stall.

**Disadvantages**:
- It has limited ability to overcome throughput losses, especially from shorter stalls: because a CPU with coarse-grained multithreading issues instructions from a single thread, when a stall occurs the pipeline will see a bubble before the new thread begins executing (_the fetched instructions of the thread that stalled must become nop and we need to start fetching instructions from the new thread_). Because of this start-up overhead, coarse-grained multithreading is much more useful for reducing the penalty of very high-cost stalls, where pipeline refill is negligible compared to the stall time.

### Simultaneous multithreading (SMT)

**Simultaneous multithreading** is a variation of fine-grained multithreading in which multiple instructions from independent threads are executed together in parallel on the functional units. The resolution of the dependencies can be handled through dynamic scheduling capabilities.

**Remark**: **super-scalar processors** need NOT to implement multithreading. They could just fetch and issue many instructions at the same time, but _from the same thread_.
