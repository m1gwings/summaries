---
marp: true
theme: summary
math: mathjax
---
# Malicious software

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Michele Carminati's slides_)

</div>

**Malware** stands for Malicious Software: it is a code that is intentionally written to violate a security policy.
There are several categories of malwares:
- **Viruses**: code that **self-propagates** by infecting executables or other files.
- **Worms**: programs that **self-propagate**, even remotely, often by exploiting host vulnerabilities, or by social engineering.
- **Trojan horses**: apparently benign programs that hide a malicious functionality and allow remote control.

Fred Cohen theorized the existence and produced the first examples of viruses. From a theoretical computer science point of view, it is an interesting concept of **self modifying** and **self propagating code**. Soon, the security challenges were understood.
From the theory, it has been proved that it is **impossible** to build the **perfect virus detector**. The proof is now outlined. Let $\mathbf{P}$ be the perfect detection program. We can build a virus $\mathbf{V}$ with $\mathbf{P}$ as a sub-routine:
- If $\mathbf{P}(\mathbf{V}) = T \rightarrow \mathbf{V} \text{ halts} \rightarrow \mathbf{V} \text{ is NOT a virus}$.
- If $\mathbf{P}(\mathbf{V}) = F \rightarrow \mathbf{V} \text{ spreads} \rightarrow \mathbf{V} \text{ is a virus}$.

The malicious code has the following lifecycle:
1. Reproduce.
2. Infect.
3. Stay hidden.
4. Run payload.

In the reproduction and infection phase (in order to build an effective malware), it is important to balance **infection versus detection** possibility. You need to identify a suitable **propagation vector**.

There are different infection techniques for viruses:
- **Boot viruses**: they use the Master Boot Record (MBR) of hard disk (the first sector on disk) or the boot sector of partitions. This is a rather old approach, but interest is growing again.
- **File infector**: we distinguish between <u>simple overwrite virus</u>, <u>parasitic virus</u>, which append codes and modifies the program entry point, <u>(multi)cavity virus</u>, which injects code in unused region(s) of the program.

---

- **Macro viruses**: they use the "_macro_" functionality that allows to add code to data files.

## Defending against malware

The first way of defending against malware is through **patches**: most worms exploit known vulnerabilities.
A second approach is to try to **detect** them. It is possible to detect malwares thorugh:
- **Signatures**: what the malware is (i.e., known unique patterns or sequence of code).
- **Behaviors**: what the malware does (i.e., known actions performed ona system).
- **Intrusion or anomaly detection**: effect on infected system/network.

**Antivirus** and **anti-malware** are software designed to detect, block and remove malicious software from computers and networks.
The basic strategy is **signature-based detection**. Some heuristics are often employed and some behavioral detection.

With **static analysis** we analyze a malware by looking at its code (e.g., through disassembly, decompilation, string extraction, etc.).
With **dynamic analysis** we analyze a malware by executing it in a controlled environment and monitoring its behavior.

The advantages of static analysis are full code visibility and coverage, including dormant or unreachable code. Plus it is safe: no risk of code execution.
The disadvantages are that obfuscation-resistant techniques can hinder the analysis. Furthermore, we have no visibility into runtime behavior or environment-dependent logic.

TThe advantages of dynamic analysis is that it bypasses obfuscation, focusing on real behavior. It reveals runtime artifacts. The disadvantages are limited code coverage (dormant branches may not execute) and risk of environment detection.

## Virus stealth techniques

Virus scanners quickly discover viruses by searching around the entry point.

**Obfuscation** is the set of techniques used in viruses to make detection harder:
- **Polymorphism**: the idea is to change the code structure (layout), with each infection. The payload remains functionally identical but is encrypted or packed with a different key at each infection. It makes signature-based detection highly ineffective. However, antivirus tools may detect the decryption routine if not obfuscated.

- **Metamorphism**: the idea is to generate entirely new variants of the code for each infection. Code appears different, but preserves the semantic. It is harder to detect even with heuristic or behavioral analysis.

---

Other malware general stealth techniques are:
- **Dormant period**: during which no malicious behavior is exhibited.
- **Event-triggered payload**.
- **Anti-virtualization techniques**.
- **Encryption/Packing**: similar to polymorphism but more advanced techniques are available in more complex malware.
- **Rootkit techniques**.

### Anti-virtualization techniques

Malware detect virtualization for the following reason: if a program is not run natively on a machine, it may be under analysis, being scanned, or debugged. Modern malware checks the execution environment to evade detection and hinder analysis.
Virtual machines are easily detectable via timing analysis or environmental artifacts.
Hardware-assisted VM requires more advanced checks, but still often detectable.
Emulator are the hardest to detect in theory, but in practice they are vulnerable to timing discrepancies, incomplete instruction set implementations and behavioral deviations among emulators.

### Packing

The idea is to **encrypt** the malicious payload to evade detection. It uses a small **encryption/decryption routine** changing the key at each execution to avoid signature matching.

Typical packing functions are:
- compression/decompression;
- encryption/decryption;
- inclusion of metamorphic components;
- anti-debugging techniques;
- anti-VM techniques;
- code virtualization to hide real instructions.

## Rootkits

The name **rootkit** comes from the fact that you become **root** ona machine, and you plant your **kit** to remain root. Can be either userland or kernel-space.

Userland rootkits are the easier to build, but are often incomplete. They are easier to detect.
Kernel space rootkit are more difficult to build, but can hide artifacts completely. They can only be detected via post-mortem analysis.
