---
marp: true
theme: summary
math: mathjax
---
# Parallel architectures

<div class="author">

Cristiano Migali

</div>

- A **parallel computer** is a collection of processing elements that cooperate and communicate to solve large problems fast.

The aim of parallel architectures is to replicate processors to add performance instead of designing faster processors (_horizontal scalability_ vs _vertical scalability_). They extend the traditional computer architecture with a **communication architecture** (_to allow the interaction among the different computational units_).

## SIMD parallel architectures

In SIMD parallel architectures, multiple processing units execute the same instruction, but they operate on different data elements. Usually, each processing unit has its own data memory and they are typically special-purpose.
There is a central controller which broadcasts instructions to multiple processing elements. The units are synchronized: there is a single Program Counter.
SIMD architectures are motivated by the fact that the cost of the control unit is shared by all execution units.

### Vector processing

**Vector processors** execute high-level operations that work on linear arrays of numbers known as **vectors** (this is analogous to the definition of vector in linear algebra).
A vector processor consists of a pipelined _scalar unit_ (for usual operations on scalars, i.e. single numbers as in linear algebra) and a _vector unit_.
We distinguish between:
- **memory-memory vector processors**: all vector operations are memory to memory (_the data is read from the memory, processed, and written back to the memory_);
- **vector-register processors**: all vector operations are between _vector registers_ (except loads and stores).

Each FU which implements vector operations has multiple, usually deep, pipelines, known as **lanes** on which the computations among the elements of the vectors are distributed. The control is simplified by the fact that the computations on the elements of the vectors are independent. For example a single lane can carry out the addition between two elements of different vectors (in the same position, as usual vector addition).
The vector register storage is distributed over the lanes. For example, if we have 4 lanes, we also have 4 different vector registers; the elements of a vector are stored in these registers in a round-robin fashion. Usually, more than one pipeline is connected to each of these vector registers: different pipelines implement different operations.

---

### Graphics Processing Units (GPUs)

A GPU is a computing device tailored for highly parallel operations. It has many parallel execution units and higher transistor count w.r.t. CPUs.
It is for the most part deterministic in its operations and have very deep pipelines (several thousands of stages).
Finally, the memory interfaces of GPUs are significantly faster and more advanced w.r.t. those of CPUs since they need to shift around a lot more data.

In the usual GPU workload for graphics processing, the GPU receives geometry information from the CPU and computes the corresponding picture as an output.
This happens going through 5 stages:
- **host interface**;
- **vertex processing**;
- **triangle setup**;
- **pixel processing**;
- **memory interface**.

#### Host interface

The **host interface** is the communication bridge between the CPU and the GPU. Through this interface, the GPU receives commands from the CPU and also pulls geometry information from system memory. The geometry information consists in a stream of vertices in object space with all their associated features (normals, texture coordinates, per vertex color, ...).

#### Vertex processing

The **vertex processing** stage receives vertices from the host interface in object space and output them in screen space.
This may require a simple linear transformation, or a complex operation involving morphing effects.
Normals, texture coordinates, ... are also transformed. Now new vertices are created in this stage and no vertices are discarded.

#### Triangle setup

In this stage geometry information becomes raster information: the output in in pixel space.
Prior to rasterization, triangles that are back-facing or are located outside the viewing frustum are rejected. Some GPUs also do some hidden surface removal at this stage.

---

#### Fragment processing

Each fragment provided by triangle setup is fed into fragment processing as a set of attributes (position, normal, texture coordinates, etc...) which are used to compute the final color for the pixel.
The computations taking place here include texture mapping operations.
Typically this stage is the bottleneck of the graphics workload.

#### Memory interface

Fragment colors provided by the previous stage are written to the frame-buffer.
On modern GPUs, color and $z$ level information is compressed to reduce the required frame-buffer bandwidth.

#### Programmability of the GPU

Vertex and fragment processing, and now triangle set-up, are programmable.
The programmer can write programs that are executed for every vertex as well as for every fragment.
This allows fully customizable geometry and shading effects.

#### CPU/GPU interaction

The CPU and GPU inside the system work in parallel with each other. There are two "threads" going on, one for the CPU and one for the GPU, which communicate through a **command buffer**. If this command buffer is drained empty, we are CPU limited and the GPU will spin around waiting for new input. If the command buffer fills up, the CPU will spin around waiting for the GPU to consume it, and we are effectively GPU limited.

Another important point to consider is that programs that use the GPU do not follow the traditional sequential execution model. Indeed, the requests of the CPU to execute a command on the GPU are asynchronous. This of course introduces several synchronization issues.

Suppose that the CPU has sent a command to the GPU requesting to operate on a block of data. The CPU can't modify such block until the GPU has carried out the computation, otherwise we could affect program correctness.
There are different ways to handle this situations.
- Some APIs implement **semaphore style** operations to keep this from causing problems. If the CPU attempts to modify a piece of data that is being referenced by a pending GPU command, it will have to spin around waiting, until the GPU is finished with that command. While this ensures correct operations, it is not good for performance since we're wasting CPU time.
- Another solution is to inline the data block in the command buffer. This is also bad for performance, since we may need to copy several MiB of data instead of merely passing around a pointer.

---

- A better solution is to allocate a new data block and initialize that one instead, the old block will be deleted once the GPU is done with it. Modern APIs do this automatically.

#### GPU readbacks

The output of a GPU is a rendered image on the screen, what will happen if the CPU tries to read it? This forces to synchronize the CPU and the GPU: the GPU musts drain its entire command buffer, and the CPU must wait while this happens. We lose parallelism, since first the CPU waits for the GPU, then the GPU waits for the CPU (because the command buffer has been drained).
This tells us that is better to treat the communication from CPU to GPU as unidirectional.

#### Some more GPU tips

Since GPUs are highly parallel and deeply pipelined, it is better to try to dispatch large batches with each drawing call. Sending just one triangle at a time will not occupy all of the GPU's several vertex/pixel processors, nor it will fill its deep pipelines.
Since all GPUs today use the z-buffer algorithm to do hidden surface removal, rendering objects front-to-back is faster than back-to-front, or random ordering.


---

## MIMD parallel architectures

Nowadays, the most common types of parallel computer fall in the MIMD class.
In a MIMD architecture there are several processing units. Each processor may be executing a different instruction stream, operating on different data elements.
The execution can be synchronous or asynchronous, deterministic or non-deterministic.

MIMDs are flexible: they can function as single-user machines for high performances on one application, as multi-programmed multiprocessors running many tasks simultaneously, or as some combination of such functions.
Finally, MIMD architectures can be realized starting from standard CPUs.
Indeed, each processors in a MIMD architecture is usually an off-the-shelf microprocessor which fetches its own instructions and operates on its own data.
We can make this architectures scale by increasing the number of processor nodes.
To exploit a MIMD architecture with $n$ processors we need at least $n$ threads or processes to execute in parallel.

Existing MIMD machines fall into 2 classes, depending on the number of processors involved, which in turn dictates a memory organization and interconnection strategy. We refer to the multiprocessors by their memory organization because what constitutes a small or large number of processors is likely to change over time.
- **Centralized shared-memory architectures** (also knows as _Symmetric MultiProcessors_ (_SMP_)): they feature a small number of cores, typically eight or fewer. For multiprocessors with such small processor counts, it is possible for the processors to share a single centralized memory that all processors have equal access to. In multi-core chips, the memory is effectively shared in a centralized fashion among the cores, and all existing multi-cores are SMPs. SMP architectures are also sometimes called _Uniform Memory Access_ (_UMA_) multiprocessors, arising from the fact that all processors have a uniform latency from memory, even if the memory is organized into multiple banks.
- **Distributed memory architectures**: to support larger processor counts, memory must be distributed among the processors rather than centralized, otherwise, the memory system would not be able to support the bandwidth demands of a larger number of processors without incurring excessively long access latency. The key disadvantages for a DSM are that communicating data among processors becomes somewhat more complex, and a DSM requires more effort in the software to take advantage of the increased memory bandwidth afforded by distributed memories.

Currently, the approach that dominates the server market is _Bus-Bases Symmetric Shared Memory_.

Observe that there are also two types of address spaces on which processors can rely <u>which are orthogonal w.r.t. the underlying physical memory architecture that we just discussed</u>.
- **Single logically shared address space**: a memory reference can be made by any processor to any memory location.

---

>  The address space is shared among processors: the same physical address on 2 processors refers to the same location in memory;

- **Multiple and private address spaces**: the processors communicate among them through send/receive primitives. This is know as a **Message Passing Architecture**. The address space is logically disjoint and cannot be addressed by different processors: the same physical address on 2 processors refers to 2 different locations in 2 different memories.

For example, multiprocessor systems can have a single addressing space on a distributed physical memory.

The kind of address space determines also the programming model used to distribute the workload.
- [Programming model 1] **Shared Memory**: in this programming model, a program is a collection of threads. It is also possible to create them dynamically during the execution. Each thread has a set of **private variable**, e.g. local stack variables and a set of **shared variables**, e.g. static variables, shared common blocks, or global heap. Threads communicate **implicitly** by writing and reading shared variables. Threads coordinate by **synchronizing** on shared variables.
**Advantages**:
> - implicit communication;
> - low overhead when cached;

> **Disadvantages**:
> - complex to build in a way that scales well;
> - requires synchronization operations;
> - hard to control data placement within caching systems.

- [Programming model 2] **Message Passing**: in this programming model, a program consists of a collection of **named** processes, usually fixed at program startup time. They DO NOT share data. Instead they communicate explicitly through send/receive primitives.
**Advantages**:
> - explicit communication;
> - easier to control data placement;

> **Disadvantages**:
> - message passing overhead can be quite high;
> - more complex to program;
> - high software overhead to execute the send/receive primitives. In particular receiving messages can be expensive due to the need to poll or interrupt.

---

### Shared Memory Machines
#### Cache coherency

We can classify further Shared Memory Machines in two main categories:
- **Non cache coherent**;
- **Hardware cache coherent**.

To understand the difference we need to talk about the problem of cache coherence.
Shared Memory Architectures cache both private data (used by a single processor) and shared data (used by multiple processors to provide communication).
When shared data are cached, the shared value may be replicated in multiple caches. In addition to the reduction in access latency and required memory bandwidth, this replication provides a reduction of shared data contention read by multiple processors simultaneously. But **private processor caches create a problem**: copies of a variable can be present in multiple caches, hence a write by one processor may not become visible to others. This problem is known as **cache coherence**.

An informal definition of cache coherency could be "Any read must return the most recent write". Unfortunately this requirement is too strict and too difficult to implement. A better requirement is the following: "Any write must eventually be seen by a read. All writes are seen in proper order (**serialization**)".
There are two rules which are sufficient to guarantee the second requirement.
1. If P1 writes $x$ and P2 reads it, P1's write will be seen by P2 if the read and write are sufficiently far apart and no other writes to $x$ occur between the two accesses.
2. Writes to a single location are serialized: two writes to the same location by any two processors are seen in the same order by all processors.
The HW-based solutions to maintain coherency rely on the so-called **Cache Coherence Protocols**. The key issue to solve in order to implement a Cache Coherence Protocol in a multi-processors system is being able to track the status of any sharing of a cache data block.
In particular, we distinguish two classes of protocols:
- **Snooping protocols**;
- **Directory-based protocols**.

##### Snooping protocols

In **Snooping Protocols** all cache controllers monitor (_snoop_) on a shared bus to determine whether or not they have a copy of the block requested on the bus and respond accordingly. Every cache that has a copy of the shared block, also has a copy of the sharing status of the block, and no centralized state is kept.
Requests for shared data are sent to all the processors. Hence these protocols require broadcasting.

---

Snooping Protocols are of two types depending on what happens on a write operation:
- **Write-Invalidate Protocol**;
- **Write-Update** or **Write-Broadcast Protocol**.

In a **Write-Invalidate Protocol** the writing processor issues an invalidation signal over the bus to cause all copies in other caches to be invalidated before changing its local copy.
The writing processor is then free to update the local data until another processor asks for it. All caches on the bus check to see if they have a copy of the data and, if so, they must invalidate the block containing them. This scheme allows multiple readers but only a single writer.
The bus is used only on the first write by a processor to invalidate the other copies. Subsequent writes do not result in bus activity. This protocol provides similar benefits to write-back protocols in terms of reducing demands on bus bandwidth.

In a **Write-Update Protocol** the writing processor broadcasts the new data over the bus; all caches check if they have a copy of the data and, if so, all copies are updated with the new value. This scheme requires the continuous broadcast of writes to shared data (while Write-Invalidate Protocols delete all other copies on the first write). This protocol provides similar benefits to write-through protocols because all writes go over the bus to update the copies of the shared data. Furthermore, the memory stays always up to date.

Most part of commercial cache-based multi-processors uses **Write-Back caches** with a **Write-Invalidate protocol** to reduce bus traffic.

Observe that we can use the same snooping scheme both for cache misses and writes. Each processor snoops every address placed on the bus; if a processor finds that it has a dirty copy of the requested cache block, it provides the cache block in response to the read request.

###### Write-Invalidate protocols

In a Write-Back cache system with Write-Invalidate protocol each **memory block** can be in one of three states:
- **Clean**: it is in more than one cache and up-to-date in memory;
- **Dirty**: it is exactly in one cache;
- NOT in any cache.

In the **MSI Invalidate** protocol also **cache blocks** have three states:
- **M**: **Modified**;
- **S**: **Shared**;
- **I**: **Invalid**.

When a processor reads, it obtains a block in the shared state. Writing requires to obtain exclusive ownership: we send an invalidate message to all other caches.
There are some complications for the basic MSI protocol: the operations are not atomic, e.g. detecting misses, acquiring the bus, receiving a response.

---

It creates the possibility of deadlocks and races. One possible solution is that the processor which sends the invalidate can hold the bus until other processors receive the invalidate.

The **MESI Invalidate** is an improvement w.r.t. **MSI invalidate**. We add another state: **E**, **Exclusive**.
In particular, the meaning of the states is:
- **Modified**: the block is dirty and cannot be shared, cache has the only copy, it is writable;
- **Exclusive**: the block is clean and the cache has the only copy;
- **Shared**: the block is clean and other copies of the block are in cache;
- **Invalid**: the block contains no valid data.

The addition of the exclusive block prevents the need of sending useless invalidate on write when we are the only owners of the block.

#### Memory consistency

**Memory consistency** answers the question "When must a processor see the new value of a data updated by another processor?". There are several possible definitions (requirements) for consistency.

- A system is **sequentially consistent** if the result of any execution is the same as if the operations of all the processors were executed in some sequential order, and the operations of each individual processor appear in the order specified by the program.

Sequential consistency is usually a too strict requirement, and often it is also unnecessary if  programs are **synchronized**: i.e.e, the accesses to shared variables are ordered by synchronization operations (_lock_, _unlock_).
The need for synchronization arises whenever there are concurrent processes in a system (_even in a uni-processor system_).
The are two **classes of synchronization**:
- **Producer-Consumer**: a consumer process must wait until the producer process has produced the data;
- **Mutual exclusion**: ensures that only one process uses a resource at a given time.

Atomic _Read-Modify-Write_ (_RMW_) instructions have been added to ISAs to support mutual exclusion.
