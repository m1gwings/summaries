---
marp: true
theme: summary
math: mathjax
---
# Buffer overflows

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Michele Carminati's slides_)

</div>

Intuitively, we get a **buffer overflow** when we fill a buffer in memory with an oversized input.

For simplicity, in this summary we will assume that the binaries are **ELFs** running on **Linux >= 2.6** on top of a **32 bit x86** machine.

## Binary formats

The **binary** of a program holds information about:
- How the file is organized on disk.
- Hot to load the file in memory.
- If the file is an **executable** or a library (executables have entry points).
- The machine class (e.g. x86).
- Sections:
>> a. Data
>> b. Code
>> c. ... .

The **ELF header** describes the high-level structure of the binary. It defines the file type and the section and program headers boundaries.
**Program headers** describe how the file will be loaded in memory. Data is divided into segments. Each section is mapped to a segment.
**Segments** constitute the runtime view of the ELF. **Sections** contain linking and relocation information.
**Section headers** describe the binary as on disk. The define the sections:
- **.init** contains the executable instructions that initialize the process.
- **.text** contains the executable instruction of the program.
- **.bss** contains the statically-allocated **variables**, i.e., uninitialized data.
- **.data** contains the initialized data.

## Process creation in Linux

When a program is **executed**, it is mapped in memory and laid out in an organized manner. The following operations are carried out in sequence:
1. The kernel creates a **virtual** address space in which the program runs.

---

2. The information is loaded or _mmapped_ from the executable file to the newly allocated address space:
>> 2.a. The loader and dynamic linked, called by the kernel, loads the segments defined by the program headers.

3. The kernel sets up the _stack_ and _heap_ and jumps at the _entry point_ of the program.

The **stack** contains statically allocated local variables (including environment variables), and function activation records. It grow "down", toward **lower addresses**. It starts at **0xC0000000**.
The **heap** conversely contains dynamically allocated data and grows up toward **higher addresses**. Between the stack and the heap there is _unallocated memory_.
The **.data** segment contains the initialized data (e.g. global variables).
The **.bss** segment contains uninitialized data, zeroed when the program begins to run.
The **.text** segment contains executable code.

## Recall on registers

**General purpose** registers (EAX, EBX, ECX) are used for common mathematical operations. They store data and addresses.
The **ESP** is the address of the last stack operation: the **top of the stack**.
The **EBP** is the address of the **base of the current function frame**.

The **segment** registers are 16 bit registers used to keep track of segments and for backward compatibility.

The **control registers** control the function of the processor. An example is the **EIP** register which contains the address of the next machine instruction to be executed.

There are **other** registers, like **EFLAG**: a 1 bit register which stores the result of a test performed by the processor.

## Recall on stack instruction

The **push** instruction allocates and writes a value. This is achieved with the following sequence of operations:
1. The ESP is decremented by 4 bytes.
2. A Dword is written to the new address stored in the ESP register.

The **pop** instruction retrieves a value and deallocate the previously occupied memory. This is achieved with the following sequence of operations:
1. The value at the top of the stack is loaded into the specified register.
2. The ESP is incremented by 4 bytes.

---

### Calling a function

Functions alter the control flow of execution of a program.
When a function is called, its activation record is allocated on the stack, and the control goes to the called function.
When a function ends, it returns the control to the original function caller.
The **parameters** are **passed** to the callee by pushing them in <u>reverse order</u> onto the stack.
Before jumping to the first instruction of the callee, the CPU pushes the **current EIP** on the stack, then it jumps.
We need a way to remember where the **caller** activation record is located on the stack, so that it can be restored once the **callee** is over. We can do so by pushing the EBP of the caller on the stack before updating it with the current value of the ESP which is also the correct EBP value for the callee. This set of operations is known as function prologue.
Analogously, at the end of the callee, the value of the EBP is written on the ESP to restore the ESP of the caller, the saved EBP on the stack is popped in the EBP, finally the ret instructions allow to jump to the instruction corresponding to the saved EIP.

## Stack smashing

In **stack smashing** we overflow a buffer to overwrite the saved EIP or the saved EBP.
Overwriting the saved EBP results in the _Frame Teleporting Attack_.
We can also simply overwrite some variables.

When we overwrite the saved EIP we need to jump to a valid memory location that contains, or that can be filled with, **valid executable machine code**.
There are several solutions:
- Jump to an environment variable.
- Jump to a built-in, existing function.
- Jump to a memory location that we can control, like the **buffer itself** or some other variable.

### Jumping to the buffer itself

Let's assume that the **overflowed buffer** has enough room for our **arbitrary machine code**. How do we guess the **buffer address**? It is somewhere around ESP (we can find the ESP value with **gdb**). Unluckily, the exact address may change at each execution and/or from machine to machine We have a **problem of precision** in the location.
Notice that some debuggers, including **gdb**, add an **offset** to the allocated process in memory. So the ESP obtained from gdb differs of a few words from the ESP obtained by reading directly withing the process.
To alleviate the problem of precision, a **NOP sled** is often used: the buffer is filled with NOPs before the actual code we want to run. If we jump anywhere inside the NOP sled, we're good to go.

The advantage of jumping to the buffer itself is that we can do this **remotely**: i.e. the input is the code.

---

The issues are that the buffer could not be large enough, memory must be marked as executable and you need to guess the address reliably.

### Shellcode

We need to understand what code to put inside the buffer. Historically, the goal of the attack was to spawn a privileged shell on a local/remote machine. The shellcode is a sequence of machine instructions that are needed to open a shell. In general, a shellcode may do just anything (e.g., open a TCP connection, launch a VPN server, a reverse shell).

### Jumping to an environment variable

The idea is the following: we allocate an area of memory that contains the exploit. Then, we put the content of that memory in an **environment variable** named **\$EGG**
Finally, we have to overwrite the saved EIP of the vulnerable program with the address of **\$EGG** by filling the buffer.

The advantages of this approach is that it is easy to implement since we have unlimited space and it is easy to target, since we can know precisely the addresses.
The disadvantages is that it works for local exploiting only, the program may wipe the environment, and memory must be marked as executable.

### Jumping to built-in, existing functions

The idea is to overwrite the saved EIP with the address of a function or system library (e.g., `system()` for a return to libc attack).
The advantages is that this works remotely and reliably and there is no need for an executable stack.
The disadvantage is that we need to prepare the stack frame carefully.

**Remark**: when we write a linux path, the leading "/////..." is analogous to a NOP sled.

## Defending against buffer overflow

There are multiple approaches to defend from buffer overflows, at different layers.
- Defenses at **source code** level: finding or removing the vulnerabilities.
- Defenses at **compiler** level: making the vulnerabilities non-exploitable.
- Defenses at the **operating system** level: to make more difficult attacks.

### Defenses at source code level

`C/C++` do not cause buffer overflows. The programmers cause buffer overflows by leaving bugs in their code.
To prevent buffer overflow, you should use safe standard libraries: str**n**copy, str**n**cat, etc. (which take a length parameter).

---

Another option is to use languages with Dynamic memory managements that makes them more resilient to these issues.

### Defenses at compiler level

The first option is to put warnings at compile time.
Another option, the **stopgap measure**, is randomized reordering of stack variables.
Finally, we have the **canary mechanism**. It works as follows. During the epilogue, we verify that the frame has not been tampered with a canary (_a 4 byte value_) inserted between local variables and control values (saved EIP/EBP). When the function returns, the canary is checked and if tampering is detected, the program is killed. 

There are different **types of canaries**:
- **Random canaries** are random sequences of bytes, chosen when the program is run.
- **Random XOR canaries** are the same as above, but canaries are XORed with part of the structure that we want to protect instead of being inserted in between.
- **Terminator canaries** are made with terminator characters that cannot be copied by string-copy functions and therefore cannot be overwritten (this is effective against string-based buffer overflow attacks).

### Defenses at OS level

The first defense at the OS level is to make the stack **non-executable**. This prevents stack smashing on local variables. The issue is that some programs (e.g., older versions of the JVM) actually need to execute code on the stack.
This can be by-passed to "return to libc" kind of attack and their generalization: Return Oriented Programming (ROP).

The second (and most effective) defense is **Address Space Layout Randomization** (**ASLR**). The idea is to reposition the stack, among other things, at each execution at random. It is harder to guess the return addresses correctly.
