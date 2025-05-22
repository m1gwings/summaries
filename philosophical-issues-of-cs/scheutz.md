---
marp: true
theme: summary
math: mathjax
---
# Summary of Scheutz 2002

<div class="author">

Cristiano Migali

</div>

## Summary

The article studies the _notion_ of **<u>computation</u>**. The author starts by introducing the concept of computation. According to Webster's dictionary, "to compute" derives from the latin "com + putare" - to consider, which means something like "to determine or to calculate especially by mathematical means". However, this definition is rather vague and furthermore too restrictive to justify the variety of uses to which the notion of computation is put in computer science alone.
A better _definition_ of computation is <u>the execution of algorithms</u>. This new definition however moves the problem to the definition of the _algorithm_ and to what "_executing an algorithm_" means. Roughly speaking, an algorithm consists of a finite set of instructions, which operate on certain entities and can be _implemented_ in some mechanism. To execute an algorithm then intuitively means to have the mechanism carry out the instructions for any given input in a deterministic, discrete, stepwise fashion. The mechanism goes through a sequence of atomic steps in such a way that (one or more of) these steps correspond to some instruction, for all the instructions specified by the algorithm. Note that nothing is said about the nature of the mechanism yet: it could be concrete or abstract, natural or artificial.

After the introduction to the concept, the author presents an historical perspective on computation. The history of computation traces back to the idea of some philosophers (like Leibniz) that it is possible to use mechanical systems to aid humans in performing calculations and even calculate by themselves.  The first functioning mechanical calculators were built in the seventeenth century and were composed of various mechanical parts. Leibniz, having constructed calculators himself, was one of the first to envision an application quite different from their typical use. In particular, Leibniz thought of calculators as "mechanical reasoners". His view that calculations, in particular, and logical reasoning, in general, could be _mechanized_ lies at the hearth of the notion of computation used in cognitive science today.
Another crucial contribution to the modern notion of computation is also a product of that time (due to Descartes, Hobbes, Locke, and others), namely the idea that reasoning or, more generally, thinking involves _representations_. The mathematical practice of using marks and signs as representations in calculations became a paradigm for thought itself.
Computations already very much tied to the idea of mechanically manipulating representations.
Many attempts were made at building mechanical calculators up to the end of the nineteenth century, but the computing capabilities of these machines remained very modest. The construction of computers saw a major progress only in the twentieth century due to:

---

1. the thorough logical analysis of the notions of "formal system" and "formal proof";
2. the rapid progression in the engineering of electronic components.

Then the author presents the formal definition of computation from a logico-philosophical perspective. In the 1930s, logicians laid the main philosophical groundwork for a well-defined formal notion of computation in their attempt to make the intuitive notion of computation, then called "effective calculability", formally precise. Being logicians, they were solely concerned with the class of functions over positive integers that can be effectively calculated in principle.
Church was the first to give this class of effective calculable functions a formal characterization through the so-called recursive functions.
The notion of "effectively calculable function" implies that two ingredients are needed to understand computation: a notion of "effective procedure or algorithm" and a notion of "function computed by an algorithm". The latter can be straightforwardly explicated: it is the mapping obtained by pairing all possible inputs with the corresponding outputs resulting from applying the algorithm to them. The former, however, received a satisfactory account only after Turing had introduced his machine model of a "computer".
Turing formulated his model trying to abstract the process that a human goes through when performing calculations with pen and paper. He found the following five constraints:
1. Only a finite number of symbols can be written down and used in any computation.
2. There is a fixed bound on the amount of scratch paper (and the symbols on it) that a human can "take in" at a time in order to decide what to next.
3. At any time a symbol can be written down or erased (in a certain area of the scratch paper).
4. There is an upper limit to the distance between cells that can be considered in two consecutive computational steps.
5. There is an upper bound to the number of "states of mind" a human can be in, and the current state of mind together with the last symbol written or erased determine what to do next.

Turing then defined a mathematical model of an "imagined mechanical device" that satisfies all of the above, later referred to as a "Turing machine". A **TM** consists of:
- an unbounded **tape** divided into squares, each of which can hold exactly one symbol;
- a **tape head** for reading and writing symbols from a given alphabet on the squares;
- a **controller** which is in exactly one of finitely many states at any given time.

Each _computational step_ of the machine involves:
1. reading the symbol under the tape head;
2. depending on the current state of the controller, writing a new symbol on the square, possibly switching to another state and possibly moving the tape head one square to the left or to the right.

---

The computation proceeds by discrete steps and produces a record consisting of a finite (but unbounded) number of cells, each of which is blank or contains a symbol from a finite alphabet. At each step the action is local and is locally determined, according to a finite table of instructions. This way, the TM became a model of human computing, an _idealized_ model to be precise, since it could process and store _arbitrarily long_, _finite sequences of symbols_.

The logico-philosophical analyses of the intuitive notion of computation led to the crucial insight that different attempts to characterize it can all be proven extensionally equivalent: recursive functions, $\lambda$-definable functions, and TM-computable functions all define the same class of functions. These equivalence results are possible, because what "computing" means with respect to any of the suggested formalisms is expressed in terms of functions from inputs to outputs, which are used as mediators in the comparison of the various classes of functions defined by the different formalisms. Later, other formalisms were shown to give rise to the same class of functions. Hence, by CT, any of the above mentioned formalisms captures out intuitive notion of computation, that is, _what_ it _means_ to _compute_.

Common to all the above computational formalisms is their property of being independent from the physical.
The first to incorporate physically motivated mathematical constraints into a formal model of computation was Gandy (1980) in his attempt to define a notion of computation for any discrete, deterministic, physical machine. He formulated five conditions to determine whether any system qualifies as a "mechanical machine" and proved that any function computable by a discrete deterministic device (in his sense) is effectively computable and vice versa. Hence, TM-computability (i.e., effective computability) and computability by mechanical devices are equivalent notions.
It is not clear, however, whether computation should be equated with "effective computability", since there are, at least in principle, imaginable computing devices that give rise to "Super Turing computability". An example of such a device is Turing's "oracle machine" (O-TM), which is a TM with additional atomic operations to query an "oracle". The oracle itself is a device that somehow produces values of a particular (possibly TM-uncomptuable) function.
Whether such a machine could be physically realized is an open question (maybe there are physical quantities that heppen to encode some TM-uncomputable function). The interesting point is simply that an O-TM would be perfectly mechanistic.

Although TMs have become the canonical models of computation, there are alternative construals. The following views should all be distinguished as they emphasize and capture different aspects of computation:

---

1. _formal symbol manipulation_: the manipulation of symbols by virtue of their formal properties (without regard to possible interpretations or semantic content);
2. _effective computability_: what can be done effectively by a mechanism;
3. _rule-following_, or _execution of an algorithm_: what is involved in following rules or instructions;
4. _finite_ (_digital_) _state machines_: automate with a finite set of internal states;
5. _information processing_: what is involved in storing, manipulating, and displaying information;
6. _interactive systems_: computation as interaction and communication embedded in an environment;
7. _dynamical systems_: computation expressed in the language of dynamic systems.

Despite the theoretical success of TM-computability, computer science in practice is concerned not so much with the limits of what can be computed in theory, but rather with the more modest mundane question of what can be computed withing reasonable limits. A whole new discipline within computer science called "complexity theory" is dedicated to the study of what is computationally feasible. Still other issues arise from computational practice with which the TM model, for example, can hardly cope, in particular, the need for computational systems to continually interact with their environments: what function does an operating system compute?
As a consequence the notion of "computation of a function", and with it the classical notion of algorithm, had to make room for the notion of interaction.

The independence of computations (in the sense of TM-computations) from their physical realizers was one major source of attraction for cognitive psychologists in the late 1950s. The information-processing capabilities of computers, an ability thought to underlie human cognition, and the potential of computer programs to specify exactly _how_ information is processed was another. Together they led to the thought that cognition, viewed as "the processing of information", could be completely understood and explained in terms of computations: if cognitive functions _are_ computations, then explanations of mental processes in terms of programs are scientifically justifiable without having to take the "implementing" neurological mechanisms into account, similar to computers where it is the programs implemented on the computer hardware, not the hardware itself, that explain what the computer does. The _computer metaphor_ implicit in this view has been summarized as the claim that "the mind is to the brain as the program is to the hardware" (actually, it should be, "the mind is to the brain as _computational processes_ are to the hardware"). The _computational claim about mind_ is also called _computationalism_.

---

Computationalism is not a unified view. Common to different views of computationalism are the assumptions that:
1. mental processes are computational processes;
2. the same kind of relation that holds between programs and computer hardware (i.e., the implementation relation) holds between mental descriptions and brains too.

It follows that cognitive functions can be described by and explained in terms of programs, and that the right level of abstraction at which to understand cognition is the computational level and not the level of the implementing mechanism (i.e. the brain), even though it might be helpful to know the functional organization and role of certain brain areas in determining what they implement.

Computational processes manipulate symbols by virtue of their formal and not their semantic processes. While computationalists take this to be a virtue of their approach, it is a major shortcoming for others and various arguments have been advanced to establish that formal symbol manipulation is not sufficient for human intentionality and semantics.
Anyway, even those opposed to computationalism agree at least that computation is still a valuable tool in the study of cognition. In particular, computer simulations, and computational models of congnition have become increasingly important in cognitive science.

## Comment

TODO...
