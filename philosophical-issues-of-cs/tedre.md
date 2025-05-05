---
marp: true
theme: summary
math: mathjax
---
# Summary of "Experiments in Computing: A Survey"

<div class="author">

Cristiano Migali

</div>

The paper studies the **role of experiments** in **computer science** and, in particular, it studies the so-called _experimental computer science_.
It tries to answer the following question: "What do computer scientists mean when they talk about experiments in computer science?".

The "_Experimentation in Computing_" section of the paper describes _experimentation_ in computing from 4 view points.

1. _Empirical dimensions of computing_. Computing and computers are, for one thing, _subjects_ of research. Second they are _instruments_ of research. Third, they may be both at once. Indeed, one popular way of discussing computing and experimentation is to see computers and phenomena around them as a subject of research. Specifications, program texts and programming languages can be considered to be certain kinds of models. The experiment is a central part of validating models or testing the fit between the model and the world. Another popular way of discussing experimentation in computing is through seeing computers as research instruments in other fields. The paper, however, does not focus on the instrumental aspect of computing.

2. _Subjects and topics_. Another angle at describing the context of experimentation in computing is to look at its subjects and topics. Examples are: research on memory policies in time sharing, research on queueing networks, robot competition, research on data-intensive super-computing, and research of future network architectures.

3. _Activities_. One can also take a look at what kind of activities the term "_experimental computer science_" might cover. They comprehend: exploration, construction and testing, hypothesis testing, demonstration, modeling, and performance analysis. One unique formulation of an experiment-like procedure in computing, one with automated and repeatable experiments, can be found in the cycle of test-driven development. In test-driven development, each cycle in software construction starts with writing a test for an added software feature. The procedure continues with running all the tests and seeing the previously added test fail, writing code that implements the wanted feature, and, running the test again to see if the newly written code really implements the desired functionality. In other words, the programmer starts from a certain functionality requirement, designs an automated experiment that is aimed at testing that functionality, and implements code that passes all the new and previous tests.

---

> Zelkowitz and Wallaca categorized "experimental approaches" in software engineering into three categories: _observational_ methods, which collect data throughout the project; _historical_ methods, which collect data from already completed projects; and _controlled_ methods, which attempt to increase the statistical validity of results by providing multiple instances of observations.

4. _Terminology and classifications_. We can distinguish three uses of the term "_experimental computer science_". The most prominent use of the term is to use it as a counterpart of theoretical computer science. The second use of the term is as a part of a feedback loop for the development of models, systems, and various other elements of computer science. The third notion refers to the adoption of scientific experimental methods for the evaluation of computer systems. It is important to observe that, experimentation terminology is by no means used in the same way it is used in, for instance, physics, biology, or chemistry. There are various views on the role of computing regarding experiments, there is a diversity of opinions on methods applicable,there are various examples of appropriate subjects and topics, and there are many existing analyses of experimentation in computing.

The section "_Critique of Experimentation_" of the paper presents the main critical views towards experimental computer science.

- The _mathematical reductionists_ think that experiments are necessary in computer science only when programs are not constructed with mathematical rigor. Thus, the only way of finding out what they do is by experiment. Their proposal is to rigorously prove that systems satisfy their requirements instead.

- The second source of objections was concerned with the differences between experiment in natural sciences and in computing. Emphasizing the view that computing is a constructive discipline. Hartmanis argued that experimentation in computer science is different from the natural sciences, as it focuses "_more on the how than the what_". The role of experiments in computing, according to Hartmanis and Line, is to uncover practical issues with theoretical work instead of proving those theories wrong.

- The third common type of objection was concerned with the artificial nature of data and subject matter of computing. McKnee noted that in natural sciences research is based on observations (data), which scientists can explain, predict, and replicate. In the field of computing, McKnee continued that there is no data beyond the computer and programs, which behave exactly as they were designed to behave.

---

In the "_Five View on Experimental Computer Science_" section, the paper lists 5 common uses of the term "_experiment_" in the field of computer science.

1. _Feasibility experiment_. The first and loosest use of the term "experiment" can be found in many texts that report and describe new techniques and tools. Typically, in those texts, it is not known if task $t$ can be automated efficiently, reliably, feasibly, cost-efficiently, or by meeting some other simple criterion, A demonstration of experimental (novel, untested, and newly implemented) technology shows that it can indeed be done. In this case, "experiment" is used nearly synonymously with "demonstration", "proof of concept".

2. _Trial experiment_. The second use of the term "experiment" in computing goes further than demonstrations of feasibility. The trial experiment evaluates various aspects of the system using some predefined set of variables. Typically, in those studies, it is not known how well a new system $s$ meets its specifications or how well it performs. A trial is designed to evaluated the qualities of the system $s$. Those tests are often laboratory based but can also be conducted in the actual context of use with various limitations.

3. _Field experiment_. A third common use of the term experiment is similar to trial experiments in that it is also concerned with evaluating a system's performance against some set of measures. However, the field experiment takes the system out of the laboratory. Typically, in those studies, it is not known how well a system fulfills its intended purpose and requirements in its socio-technical context of use. The system is tested in a live environment and measured for things such as performance, usability, attributes, or robustness.

4. _Comparison experiment_. A fourth common use of the term "experiment" refers to comparison between solutions. Many branches of computing research are concerned with looking for the "best" solution for a specific problem or developing a new way of doing things "better" in one way or another. Typically, in reports of those studies, it is now known if system $A$ outperforms system $B$ with data set $d$ and parameters $p$. an experiment is set up to measure and compare $A(d, p)$ and $B(d, p)$ and the report shows that the new system beats its predecessors in terms of a set of criteria $C$.

5. _Controlled experiment_. A fifth common use of the term "experiment" refers to the _controlled experiment_. THe controlled experiment is the gold standard of scientific research in many fields of science, especially when researchers aim at eliminating confounding causes, and it typically enables generalization and prediction. There are numerous uses for the controlled experiment setup; for instance, it is often used for situations where it is not known if two or more variables are associated, or if $x$ causes $y$.
