---
marp: true
theme: summary
math: mathjax
---
# Parallel architectures

<div class="author">

Cristiano Migali

</div>

- A **parallel computer** is a collection of processing elements that cooperates and communicate to solve large problems fast.

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
In a MIMD architecture there are several processing units. Each processor may be executing a different instruction streams, operating on different data elements.
The execution can be synchronous or asynchronous, deterministic or non-deterministic.

MIMDs are flexible: they can function as single-user machines for high performances on one application, as multi-programmed multiprocessors running many tasks simultaneously, or as some combination of such functions.
Finally, MIMD architectures can be realized starting from standard CPUs.
Indeed, each processors in a MIMD architecture is usually an off-the-shelf microprocessor which fetches its own instructions and operates on its own data.
We can make this architectures scale by increasing the number of processor nodes.
To exploit a MIMD architecture with $n$ processors we need at least $n$ threads or processes to execute in parallel.

Existing MIMD machines fall into 2 classes, depending on the number of processors involved, which in turn dictates a memory organization and interconnection strategy:
- **Centralized shared-memory architectures**: resume...
- **Distributed memory architectures**: resume...