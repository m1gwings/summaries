---
marp: true
theme: summary
math: mathjax
---
# Summary of Newell and Simon

<div class="author">

Cristiano Migali

</div>

## Summary

Through the article, the authors argue why Computer Science should be regarded as an empirical discipline. According to them, even though some of its unique forms of observation and experience do not fit a narrow stereotype of the experimental method, they are still experiments. Each new machine that is built is an experiment. Constructing the machine poses a question to nature; computer scientists listen for the answer by observing the machine in operation and analyzing it by all analytical and measurement means available. Analogously, each new program that is built is an experiment.

The author starts by defining the so-called "Laws of Qualitative Structure". All sciences characterize the essential nature of the systems they study. These characterizations are invariably qualitative in nature, for they set the terms within which more detailed knowledge can be developed. An example is the _cell doctrine_ in biology. It states that the basic building block of all living organisms is the cell. Cells come in a large variety of forms, though they all share a similar structure. It is important to remark that the specific internal structure was not, historically, part of the specification of the cell doctrine; it was subsequent specifically developed by intensive investigation. The cell doctrine can be conveyed almost entirely by the statement stated above, along with some vague notions about what size a cell can be.

The authors proceed by highlighting the role of experiments in Computer Science through two examples: _symbolic systems_, and _heuristic search_.

First they focus on _Physical Symbol Systems_. According to the authors, one of the fundamental contributions to knowledge of Computer Science has ben to explain, at a rather basic level, what symbols are. In what follows they argue why "symbols lie at the root of intelligent action", where by intelligence we mean the ability of a system to achieve stated ends in the face of variations, difficulties, and complexities posed by the task environment. The adjective _physical_ denotes two important features:
1. such systems clearly obey the laws of physics and they are realizable by engineered systems made of engineered components;
2. although our use of the term "symbol" prefigures our intended interpretation, it is not restricted to human symbol systems.

---

<div class="centered-definition-expression">

A physical symbol system consists of a set of entities, called symbols, which are physical patterns that can occur as components of another type of entity, called an expression (or symbol structure). Thus, a symbol structure is composed of a number of instances (or token) of symbols related in some physical way. At any instant of time the system will contain a collection of these symbol structures. Besides these structures, the system also contains a collection of processes that operate on expressions to produce other expressions. processes of creation, modification, reproduction, and destruction. A physical symbol system is a machine that produces through time an evolving collection of symbol structures. Such system exists in a world of objects wider than just these symbolic expressions themselves.

</div>

Two notations are central to this structure of expressions, symbols, and objects: **designation**, and **interpretation**.

- _Designation_: An expression designates an object if, given the expression, the system can either affect the object itself or behave in ways dependent on the object. In either case, access to the object via the expression has been obtained, which is the essence of designation.

- _Interpretation_: The system can interpret an expression if the expression designates a process and if, given the expression, the system can carry out the process. Interpretation implies a special form of dependent action: given an expression the system can perform the indicated process, which is to say, it can evoke an execute its own processes from expressions that designate them.

A system capable of designation and interpretation in the sense just indicated, must also meet a number of additional requirements, of completeness and closure.
1. A symbol may be used to designate any expression whatsoever. This property is known as **arbitrariness**. This arbitrariness pertains only to symbols; the symbol tokens and their mutual relations determine what object is designated by a complex expression.

2. There exist expressions that designate every process of which the machine is capable.

3. There exist processes for creating any expression and for modifying any expression in arbitrary ways.

4. Expressions are stable; once created they will continue to exist until explicitly modified or deleted.

5. The number of expressions that the system can hold is essentially unbounded.

The authors then state a law of qualitative structure for symbols systems: _The Physical Symbol System Hypothesis_.

<div class="centered-definition-expression">

A physical symbol system has the necessary and sufficient means for general intelligent action.

</div>

---

By "necessary", the authors mean that any system that exhibits general intelligence will prove upon analysis to be a physical symbol system. By "sufficient" the authors mean that any physical symbol system of sufficient size can be organized further to exhibit general intelligence. By "general intelligent action" the authors wish to indicate the same scope of intelligence of human action.

The Physical Symbol System Hypothesis clearly is a law of qualitative structure. it specifies a general class of systems within which one will find those capable of intelligent action.
This is an empirical hypothesis. It is important to ask if it is actually reasonable according to the observations of phenomena in the real world. Observe that, since a physical symbol system is an instance of a universal machine, the physical symbol system hypothesis implies that intelligence can be realized through a universal computer.

Then the authors give an historical perspective on the development of the symbol system hypothesis.
**Formal logic**: The root of the hypothesis go back to the development of formal logic. Frege, Whitehead, and Russel wanted to capture the basic conceptual notions of mathematics, in logic, putting the notions of proof and deduction on secure footing. This effort culminated in mathematical logic, the familiar propositional, first-order, and higher-order logics. It developed a characteristic view, often referred to as the "symbol game". Logic, and by incorporation all of mathematics, was a game played with meaningless tokens according to certain purely syntactic rules. All meaning had been purged. One had a mechanical, though permissive system about which various things could be proved.
**Theory of Computation**: Another important step in the definition of the hypothesis is the development of the first digital computers and of automata theory, starting with Turing's work. These information processing systems all operate on symbols. But, in none of these there is a concept of symbol as something that _designates_, they are detached from the physical world. The data are regarded as just strings of zeroes and ones. What was accomplished at this stage was half the principle of interpretation, showing that a machine could be run from a description. Thus, this is the stage of automatic symbol manipulation.
**Stored program**: With the development of the second generation of electronic machines in the mid.forties came hte stored program concept. Programs now can be data, and can be operated on as data. The next 
**List processing**: The next step, taken in the fifties, was list processing. The contents of the data structures were now symbols, in the sense of the physical symbol system: patterns that designated, that had referents. Lists held addresses which permitted access to other lists, thus the notion of list structures.
List processing is simultaneously three things in the development of Computer Science:
1. It is the creation of a genuine dynamic memory structure;
2. It was an early demonstration of the basic abstraction that a computer consists of a set of data types and a set of operations proper to these data types;
3. List processing produced a model of designation, thus defining symbol manipulation in the sense in which we use this concept in Computer Science today.

---

One more step  is worth noting is the creation of LISP: a new formal system with S-expressions, which could be shown to be equivalent to the other universal schemes of computation.

After this historical treatment, the authors present the evidence which supports the physical symbol system hypothesis. Since the goal is to show that Computer Science is a field of empirical inquiry, the authors don't go in much detail: they just indicate what kind of evidence there is. Some of the evidence regards the _sufficiency_ part in the hypothesis, while the remaining evidence regards the _necessity_ part. The evidence which supports the sufficiency of the hypothesis comes from the field of Artificial Intelligence. The initial approach to AI was to consider a bunch of task which were thought to require intelligence in order to be solved, and then develop ad-hoc programs to cope with them. From the original tasks, research has extended to building systems that handle and understand natural language in a variety of ways, systems for interpreting visual scenes, systems for hand-eye coordination. All the systems developed to solve these tasks happened to be instances of physical symbols systems. In particular they are a special subclass of physical symbol systems: they all rely on a technique known as _heuristic search_, which is discussed in the second part of the article.

The necessity part of the physical symbols systems hypothesis implies that the humans, being capable of intelligent actions,a re instances of physical symbols systems. The search fro explanations of human's intelligent behavior in terms of symbols systems has had a large measure of success over the past twenty years; to the point where information processing theory is the leading contemporary point of view in cognitive psychology.  Research in information processing psychology involves two main kinds of empirical activity. The first is the conduct of observations and experiments on human behavior in tasks requiring intelligence. The second, very similar to the parallel activity in artificial intelligence, is the programming of symbol systems to model the observe human behavior. The psychological observations and experiments lead to the formulation of hypotheses about the symbolic processes the subjects are using, and these are an important source of ideas that go into the construction of the programs.

According to the author, additional evidence supporting the physical symbols systems hypothesis comes from the absence of specific competing hypothesis as to how intelligent activity might be accomplished. Most attempts to build such hypotheses have taken place within the field of psychology. There is a continuum of theories from the points of view usually labeled "behaviorism" to those usually labeled "Gestalt theory". neither of these points of view stands as a real competitor to the symbol system hypothesis, and this for two reasons. First, neither behaviorism nor Gestalt theory has demonstrated that the explanatory mechanisms it postulates are sufficient to account for intelligent behavior in complex tasks. Second, neither theory has been formulated with anything like the specificity of artificial programs.

---

The second part of the article regards _Heuristic Search_. The reason which justifies the introduction of this topic is the following: knowing that physical symbol systems provide the matrix for intelligent action does not tell how they accomplish this. Here the author presents a second law of qualitative structure.

<div class="centered-definition-expression">

_Heuristic Search Hypothesis_. The solutions to problems are represented as symbol structures. A physical symbol system exercises its intelligence in problem solving by search, that is, by generating and progressively modifying symbol structures until it produces a solution structure.

</div>

Then the authors give a formal definition of what a problem is.

<div class="centered-definition-expression">

To state a problem is to designate:
1. a (solution) _test_ for a class of symbol structures (solutions of the problem),
2. a (move) _generator_ of symbol structures (potential solutions).
To solve a problem is to generate a structure using (2) that satisfies the test of (1). In particular, there is a problem when we have a test for solutions but the generator doesn't immediately provide a symbol structure satisfying the test.

</div>

Before there can be a move generator for a problem, there must be a problem space: a space of symbol structures in which problem situations, including the initial and goal situations can be represented. Move generators are processes for modifying one situation in the problem space into another. The basic characteristic of physical symbol systems guarantee that they can represent problem spaces and that they posses move generators. How, in any concrete situation they synthesize a problem space and move generators appropriate to the situation is a tricky question.
The task that a symbol system is faced with when it is presented with a problem and problem space, is to use its limited processing resources to generate all possible solutions, one after another, until it finds one that satisfies the problem-defining test. If the system had some control over the order in which potential solutions were generated, then it would be desirable to arrange this order of generation so that actual solutions would have a high likelihood of appearing early. A symbol system would exhibit intelligence to the extent that it succeeded in doing this. Intelligence for a system with limited processing resources consists in making wise choices of what to do next. This can happen only when the problem space exhibits some sort of structure. If solutions appear randomly in the problem space, it is not possible to perform better than random search. A second condition necessary to allow problem solving systems to exhibit intelligence is the pattern in the space of symbol structures can be more or less detectible. A third condition is that the generator of potential solutions is able to behave differently, depending on what pattern it detected.
In short: there must be information in the problem space and the move generator should be able of exploiting it.
Usually, in symbols systems for intelligent problem solving, each successive expression is not generated independently, but is produced by modifying one produced previously.

---

Observe that, even though, according to the heuristic search hypothesis, successive generation of potential solution structures is a fundamental aspect of a symbol system's exercise of intelligence; the amount of search is not a measure of the amount of intelligence being exhibited. Actually, it is quite the contrary. What makes a problem a problem is not that a large amount of search is required for its solution, but that a large amount would be required if a requisite level of intelligence were not applied.

There are two main families of heuristic search:
1. in serial heuristic search we modify a potential solution by producing a new potential solution, hopefully moving towards the goal;
2. in tree search we first choose a node of the tree from which the search should continue, then we understand how this node such be expanded to move towards the goal, possibly generating more than one new potential solution.

The techniques just discussed are dedicated to the control of exponential expansion rather than its prevention. For this reason, they are known as "weak methods". Weak methods are used when the problem doesn't have sufficient structure.
In highly structured problems like linear programming, instead, each new possible solution is for sure a move towards the goal.

Finally the authors list some approaches which reduce the amount of search needed in problem solving.

**Non-local use of information**: usually, information gathered in the course of three search is used only locally, to help make decisions at the specific node where the information is generated. A few exploratory approaches efforts have been made to transport information from its context of origin to other appropriate contexts.

**Semantic Recognition Systems**: a second active possibility for raising intelligence is to supply the symbol system with a rich body of semantic information about the task domain it is dealing with.

**Selecting Appropriate Representations**: a third line of inquiry is concerned with the possibility that search can be reduced or avoided by selecting an appropriate problem space. Observe that maybe this approach is not escaping from search processes: instead of searching for solutions, we search for representations.

---

## Comment


