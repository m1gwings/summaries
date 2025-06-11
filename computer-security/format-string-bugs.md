---
marp: true
theme: summary
math: mathjax
---
# Format string bugs

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Michele Carminati's slides_)

</div>

**Format strings** provide the solution to the problem of having an **output string** including **variables formatted** according to the programmer. They allow to specify how data is formatted into the string. They are available in practically any programming language's printing functions (e.g., **`printf`** in C).

In `printf` there are several placeholder to identify the formatting type:
- **`%d`** or **`%i`**: decimal;
- **`%u`**: unsigned decimal;
- **`%o`**: unsigned octal;
- **`%X`** or **`%x`**: unsigned hex;
- **`%c`**: unsigned char;
- **`%s`**: string (prints chars until "\0").

Examples of format print functions are: **printf**, **fprintf**, **vfprintf**, **sprintf**, **vsprintf**, **snprintf**, **vsnprintf**.

We have a vulnerability due to format string when one of the functions above (or the equivalent) is called passing as first argument a user-controller input. In this way, the user has direct control on the format and can use it to access areas of the memory they should not be able to access.
The calling convention of the printing function expects that the parameters are pushed onto the stack. Thus, if the user was to specify a format string "\%i \%i \%i", they would be able to read three memory cells from the stack. In other words, we can read what is already in the stack.
We can use the syntax "%N$x" to scan the stack: it prints the Nth parameter.
This is an information leakage vulnerability: we can use this technique to search for interesting data in memory.

A "useful" (in this case) placeholder is **\%n**: it allows to write the **number of chars printed so far** in the address pointed by the corresponding argument (_treated as a pointer to int_).

We can exploit this fact in the following way:
1. We put on the stack the address (**addr**) of the memory cell (**target**) to modify.
2. We use **\%x** to go find it on the stack (**\%N$x**).
3. We use **\%n** instead of that **\%x** to write a number in the cell pointed to by **addr**, i.e. **target**.

We still need a way to control the number that we're going to write in the target cell.

---

We can use **\%050c** (for example) to print 50 characters (we can't control the printed character, but we don't care). Observe that usually, in the exploit format string, we prepend the address of the target cell, thus we need to add 4 to get the actual number of printed characters.

We still have an issue if we want to write a <u>valid 32 bit address</u>, being such number so large that we can't print that many characters. To do so, we split the DWORD in 2 WORDS and write them one at the time. We can use **\%hn** to write a WORD instead of a DWORD so that we don't have overwrite issue.

**Remember**: once we start counting up with **\%c**, we cannot count down. We can only keep going up. So, we need to do some math: in the 1st round we print the word with the lower absolute value, then we print the word with the higher absolute value.

To do so, we need the target addresses of the two writes (which will be at 2 bytes of distance), which we need to put in the format string. Once we know the position of the displacement of the cell containing the first address, we simply add one to get the second (_we put them one after the other in the format string_).

In the generic case, the format string looks like this (_left to right_):
1. \<tgt (1st two bytes)\>;
2. \<tgt+2 (2nd two bytes)\>;
3. \%\<low value - printed\>c;
4. \%\<pos\>$hn;
5. \%\<high value - low value\>c;
6. \%\<pos+1\>$hn.

Always remember that the memory is in **little endian**, thus:
- The least significant WORD is is written as a smaller (-2) address than the most significant WORD.
- The addresses in the format string should be put in reverse order.

Memory error countermeasures seen in the previous slides help to prevent exploitation. Modern compilers will show warnings when potentially dangerous calls to printf-like functions are found. There are patched versions of libc to mitigate the problem (e.g., count the number of expected arguments and check that they match the number of placeholders).

Conceptually, format string bugs are not specific to printing functions. In theory, any function with a **unique combination** of characteristics is potentially affected:
- A so-called <u>variadic function</u>, i.e. a function with a variable number of parameters with parameters resolved at runtime by pulling from the stack.
- A mechanism (e.g., placeholders) to (in)directly read/write arbitrary locations.
- The ability of the user to control them.
