---
marp: true
theme: summary
math: mathjax
---
# Ziewitz 2017

<div class="author">

Cristiano Migali

</div>

## Summary

The article aims to examine the **role of algorithms** in _practical reasoning_. In particular, rather than understanding algorithms as a formal-analytic category whose meaning is to be established in advance, I shall demonstrate how people see and recognize just what is going on around them when they do so through the figure of the algorithm. The final goal is to study algorithms as a device for making sense of observations.

According to the author, the issues associated with algorithm and, in particular, with the fact that we don't have a practical grasp of their inner working, are the following:
- _impact_: the effects that algorithms have in various domains of public life;
- _accountability_: a concern about how algorithms and their makers might be held responsible for widespread impact;
- _transparency_: a demand for disclosure as a necessary condition for regulating impacts;
- _ethics_: the idea of algorithms as embodying values that might lead to bias and discrimination.

The authors aim at turning algorithms into _knowledge objects_ through the so-called _documentary method of interpretation_.
The idea is the following: we can interpret a phenomena through the documents of its appearance, and, at the same time, we interpret its manifestations based on what we know about the phenomena.
Indeed, the goal of the paper is, instead of using observations to make sense of algorithms, to use algorithms as a framework for making sense of observations.

The problem has been explored through an _ethnographic_ (i.e., which studies cultures and societies) **experiment** designed around a **simple task**: go on a walk, guided not by maps or GPS but by an algorithm you device _ad hoc_ to give directions.
The authors chose an intuitive definition of algorithm: "as step-by-step procedure for calculating the answer to a problem from a given set of inputs". 

During the experiment, there have been several contingencies caused by the fact that the participants of the experiment (i.e. the author of the article and one of his colleagues) were taking decisions following an algorithmic procedure.

1. The first problem was to define a procedure to start with. The initial procedure chosen by the author as a guiding algorithm was the following:

---

<div class="centered-definition-expression">

_At any junction, take the least familiar road_.

</div>

> The idea is that this procedure would favor exploration.
The first issue with the procedure is that it is not clear how to assess familiarity since there are two participants with different familiarities w.r.t. roads. Since it is impossible to take the average of a quantity that can't be measured, they decided to take turns in assessing similarity:

<div class="centered-definition-expression">

_At any junction, take the least familiar road_.
_Take turns in assessing familiarity_.

</div>

> The second issue is the following: what to do when all the roads are equally familiar? They added a special instruction in the pseudo-code to handle this scenario.

<div class="centered-definition-expression">

_At any junction, take the least familiar road_.
_Take turns in assessing familiarity_.
_If all roads are equally familiar, go straight_.

</div>

2. The second contingency occurred during the experiment is the following: the authors realized that they did not have an unambiguous definition of junction. They recognized the problem when they saw a little alleyway crossing the road on which they were walking. They decided a criterion to determine what is a valid road that creates a junction and updated the pseudo-code.

<div class="centered-definition-expression">

_At any junction, take the least familiar road_.
_Take turns in assessing familiarity_.
_If all roads are equally familiar, go straight_.
_It is only a road if you can walk a bike on it_.

</div>

> Since the alleyway was to narrow to walk a bike, they kept going straight.
Observe that to overcome the issue _through the algorithm_, the participants had to come up with a rule that applies in all the situations of this kind, and not just a singular decision for the specific situation.

3. At some point the participants reached a junction with one road leading to a touristic place. One of the participants wanted to visit the place, while the other did not. Thanks to the algorithm the second participant was able to defer accountability and choose another direction without having to get into a discussion.

4. The fourth contingency occurred when the participants reach a "Y" junction in which there was no road corresponding to the direction "straight". The procedure that they came up with could not handle such scenario. They added a "default" rule to solve the issue.

---

<div class="centered-definition-expression">

_At any junction, take the least familiar road_.
_Take turns in assessing familiarity_.
_If all roads are equally familiar, go straight_.
_It is only a road if you can walk a bike on it_.
_When all else fails, flip a coin_.

</div>

5. The last contingency happened when, while following the algorithmic procedure, the participants violated a private property. The author highlighted the fact that the procedure that they were using had an intrinsic bias: it did not account for the possibility of private properties. According to the procedure, everything which is reachable is public space.

To summarize, the troubles of typical algorithmic reasoning are the following:
1. the role of problematization;
2. the work of parsing observations through the language of the algorithm;
3. how algorithms can be used to defer accountability;
4. the struggle to preserve the robustness of the procedure through additional provisions;
5. the situated and selective rendering of actions as unethical when challenged by an outside intervention.

## Comment


