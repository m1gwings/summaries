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

## Advantages of virtualization

The main **advantages** of a VM are the following.

- **Partitioning**: a VM allows the execution of multiple OSs on the same machine by partitioning the physical hardware into multiple virtual resources;

- **Isolation**: the VMs running on the same machine are isolated, making the system fault-tolerant and secure.

- **Encapsulation**: the entire _state_ of a VM can be saved in a file, hence it can also be copied/moved from a physical machine to another.

- **HW-independence**: this is the main goal of virtualization.

## How is virtualization implemented?

Consider a typical layered abstraction of a computer system in which we identify (_from top to bottom_) **applications**, **OS**, and **hardware**.

---

Virtualization is implemented by adding a _virtualization layer_ either between the applications and the OS or the OS and the hardware. Depending on where the new layer is placed, we obtain different types of virtualization.

### Hardware-level virtualization

In **hardware-level virtualization** the virtualization layer is placed between the hardware and the OS. The interface seen by the OS and by the applications can be different from the physical one.

### Application-level virtualization

In **application-level virtualization** a virtualization layer is placed between the OS and some applications (e.g. JVM). It allows applications to run in their environment, independently from the OS.

### VMM vs VMM vs Hypervisor

We've already introduced the concept of **Virtual Machine Monitor** to mean the software which allows to implement System VMs. Now we're going to define the analogous concepts of **Virtual Machine Manager**, and **Hypervisor**; explaining the differences.

A **Virtual Machine Manager** is an application that manages the virtual machines; mediates access to the hardware resources on the physical host system;

---

intercepts and handles any privileged or protected instruction issued by the virtual machines. This type of virtualization typically runs virtual machines whose operating system, libraries, and utilities have been compiled for the same type of processor and instruction set as the physical machine on which the virtual systems are running.

The difference w.r.t. a Virtual Machine Monitor and an Hypervisor is that:
- **Virtual Machine Monitor** refers _just to the virtualization software_.
- **Hypervisor** refers to _virtualization software running directly on the hardware_.
- **Virtual Machine Manager** refers to a _VMM or Hypervisor_ that is also used to _create, configure and maintain virtualized resources_. It provides a user-friendly interface to the underlying virtualization software.

Another equivalent nomenclature identifies two types of VMM.
We call **bare-metal** or **type-1 VMM** an hypervisor.
We cal **type-2 VMM** a VMM running within an host OS.
Type 2 hypervisors are more flexible in terms of underlying hardware, and simpler to manage and configure since VMM can use the host OS to provide GUI, instead of relying only on the BIOS. Anyway the host OS might consume a non-negligible set of physical resources.

---

#### Hypervisor's architecture

We can distinguish two main kinds of hypervisors (type-1 VMMs): **monolithic** and **micro-kernel**.

In a monolithic hypervisor the drivers to control the hardware of the physical machine run directly within the hypervisor.
This leads to better performance and full abstraction from the underlying physical hardware from the VM point of view. The disadvantage is that we can run only hardware for which the hypervisor has drivers.

In a micro-kernel hypervisor instead, device drivers run within a _"Service VM"_. This leads to smaller hypervisors, and allows to leverage the driver ecosystem of an existing OS.

#### Para-virtualization vs Full virtualization

We can distinguish between two main techniques to implement System VMs in the "Same ISA" case: **para-virtualization** and **full virtualization**.

**Full virtualization** provides a **complete simulation of the underlying hardware**: the full instruction set, all I/O operations, interrupts, and memory access.
The privileged instructions issued by the Guest OS are trapped and handled by the Hypervisor. Full virtualization allows to run unmodified OSs, assuming that their target ISA corresponds to the one that is virtualized.

---

The cons is that executing system calls in the virtualized environment is very expensive: when the guest OS is executing a system call, the hypervisor needs to trap and execute on the real hardware every privileged instruction, and it must do so in such a way to keep the physical state of the underlying platform consistent with all the VMs running on it. This can introduce a significative overhead.

In **Para-virtualization** we run a modified version of the guest OS which cooperates with the VMM. In particular, when the modified guest OS has to execute a system call, it can invoke the corresponding service provided by the Hypervisor through "hooks". In this way we don't have to execute every privileged instruction of the original system call in the virtualized environment, instead, the guest OS can acknowledge the Hypervisor of the requested service and the Hypervisor can execute it efficiently outside of the virtualized environment. This approach has very high performance and simplifies the VMM. The cons is that we must run a specially tailored guest OS, hence it could be the case that we need to adapt the application that we wish to run onto such OS.

## Containers

**Containers** are _standardized units_ which package all the dependencies of a certain program to execute it on a target machine.

---

The _main advantage_ of containers is that their behavior is predictable, repeatable and immutable: when I create a "_master_" container and duplicate it on another server, **I know exactly how it will be executed**. There are no unexpected errors when moving it to a new machine or between environments.

### Containers vs VM

VMs provide hardware virtualization, while containers provide virtualization at the operating system level. Furthermore, the main difference is that each container shares the host system kernel with other containers.

### Features of containers

Containers are:
- **flexible**: even the most complex applications can be containerized;
- **light**: the containers exploit and share the host kernel;
- **interchangeable**: updates can be distributed on the fly;
- **portable**: you can create locally, deploy in the Cloud and run anywhere;
- **scalable**: it is possible to automatically increase and distribute replicas of the container;
- **stackable**: containers can be stacked vertically and on the fly.

---

Containers ease the deployment of applications and increase the scalability, but they also impose a **modular application development** where the modules are independent and uncoupled.

Containers have several purposes.
- Helping make your local development and build workflow faster, more efficient, and more lightweight.
- Running stand-alone services and applications consistently across multiple environments.
- Using container to create isolated instances to run tests.
- Building and testing complex application and architectures on a local host prior to deployment into a production environment.
- Building a multi-user Platform-as-a-Service (PaaS) infrastructure.
- Providing lightweight stand-alone sandbox environments for developing, testing, and teaching technologies.
- Building Software-as-a-Service (SaaS) applications.
