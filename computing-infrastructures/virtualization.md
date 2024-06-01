---
marp: true
theme: summary
math: mathjax
---
# Virtualization

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Manuel Roveri_)

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

## Basic definitions

In order to define what a **Virtual Machine** (**VM**) is, we need to state what is a _machine_ and what is _virtualization_.

<div class="definition">

A **machine** is an _execution environment_ capable of _running_ a _program_.

</div>

<br>

<div class="definition">

**Virtualization** involves the construction of an _isomorphism_ that maps a _virtual guest_ to a _real host_. In particular, this isomorphism maps the guest state to the host state, and is such that, for a sequence of operations $e$ that modifies the state in the guest, there is a corresponding sequence of operations $e'$ in the host that performs an equivalent modification to the host's state. 

</div>

Although such an isomorphism can be used to characterize abstraction as well as virtualization, we distinguish the two: virtualization differs from abstraction in that virtualization does not necessarily hide details;

---

the level of detail in a virtual system is often the same as the underlying real system.

We're ready to define what a VM is.

<div class="definition">

A **Virtual Machine** (**VM**) is a logical abstraction able to provide a _virtualized execution environment_. More specifically, a VM:
- _provides_ identical software behavior;
- consists in a combination of physical machine and virtualizing software;
- may appear as different resources than physical machine;
- may (_often_) result in different level of performance. 

</div>

The **tasks of a VM** are:
- to map virtual resources or states to the corresponding physical ones;
- to use physical machine instructions/calls to execute the virtual ones.

## System VM vs Process VM

There are two main classes of VMs: **System VMs** and **Process VMs**.
In order to distinguish between the two, we need to talk about _computer architectures_.

---

The term **architecture**, when applied to **computers**, refers to the functionality and appearance of a computer system or sub-system, <u>but not the details of its implementation</u>.
The architecture is often formally described through a specification of an interface and the logical behavior of resources manipulated via that interface; that is, it is described by a set of instructions.
There is an architecture for each level of abstraction of a computer system.
In particular we distinguish between 6 layers with decreasing level of abstraction of the underlying hardware.

- Level 5: **Problem-oriented language level**.
- Level 4: **Assembly language level**.
- Level 3: **Operating system machine level**.
- Level 2: **Instruction set architecture level**.
- Level 1: **Micro-architecture level**.
- Level 0: **Digital logic level**.

Usually we regard as **software** levels 5, 4, 3, and as **hardware**, levels 2, 1, 0.
The **Instruction Set Architecture** (**ISA**) corresponds to layer 2. Remember that the ISA is composed of two parts.
- The **User ISA** comprehends the aspects of the ISA that are visible to an application program: when an application interacts with the HW, the User ISA is used.
- The **System ISA** comprehends the aspects visible to the supervisor software (i.e. the OS), which is responsible for managing hardware resources. The OS can interact with the hardware both through User ISA or System ISA.

---

The **Application Binary Interface** (**ABI**) corresponds to layer 3. The ABI comprehends the User ISA and the **System Calls** which provide a specific set of operations that an OS may perform on behalf of a user program.
Observe that a program binary compiled to a specific ABI can run unchanged only on a system with the right ISA and OS.

At this point the **distinction** between System VMs and Process VMs is easy: _System VMs virtualize the entire ISA_, while _Process VMs virtualize the ABI_.

In particular, a **System VM** provides a complete system environment that can support an operating system. (_We call "system" a full execution environment that can simultaneously support a number of processes potentially belonging to different users_). In particular, it provides access to underlying hardware resources (networking, I/O, etc.) to the operating system running in it. The VM supports the operating system as long as the system environment is alive. Virtualizing software is placed between the hard and the software, it _emulates the ISA interface seen by software_, and is called **Virtual Machine Monitor** (**VMM**).
The VMM can provide its functionality either **working directly on the hardware**, or **running on another OS**.

A **Process VM** is able to support an individual process. The virtualizing software is placed at the ABI interface, on top of the OS/hardware combination; it emulates both user-level instructions and operating system calls, and is usually called **Runtime Software**.

---

In particular, the Runtime Software supports the levels from 0 to 3.

**Terminology**: we call **host** the underlying platform supporting the environment/system, and **guest** the software that runs in the VM environment as the guest.

We can enrich the VMs taxonomy by making a distinction between the case in which host and guest share the same ISA/ABI and the case in which they don't.
In particular, we call:
- **Multi-programmed system**: a **Process VM** with **same ABI**;
- **Dynamic Translators**: a **Process VM** with **different ABI**;
- **Classic-System VM**: a **System VM** with **same ISA**;
- **Whole-System VM**: a **System VM** with **different ISA**.

### Multi-programmed system

This kind of "VMs" constitute the common approach of all modern OS for **multi-user support**. Each user process is given the illusion og having a complete machine to itself. In particular, each process has its own address space.
The OS timeshares and manages HW resources to permit this.

### Emulation

**Emulation** refers to those software technologies developed to allow an application or OS to run in an environment different from that originally intended.

---

It is required when the VMs have different ISA/ABI from the architecture where they're running on.

### High-Level Language VM

**High-Level Language VM** are _similar_ to Process VMs. In this case, the VM environment does not directly correspond to any real platform. Rather, it is designed for ease of portability and to match the features of a high-level language (HLL) used for application program development. They are focused on minimizing hardware-specific and OS-specific features because these would compromise platform independence. 

An example is the Java Virtual Machine (JVM).

### Classic-System VM

Remember that in Classic-System VM the VM has the same ISA of the underlying platform. In this setting, the VMM is on bare hardware, and virtual machines fit on top. The VMM can intercept guest OS's interaction with hardware resources. This is the most efficient VM architecture. It allows to run rwo different OSs on the same HW.

### Hosted VM

In a **Hosted VM** the virtualizing software is on top of an existing operating system.

---

### Whole-system VM

Since the ISAs are different, both application and OS code require emulation. Usually this kind of VMs are hosted. The VM software must emulate the entire hardware environment and all the guest ISA operations to equivalent OS calls to the host.

## How is virtualization implemented?

