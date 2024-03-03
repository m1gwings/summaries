---
marp: true
theme: summary
---
# What is Artificial Intelligence?

<div class="author">

Cristiano Migali

</div>

The field of **Artificial Intelligence** (or **AI**) is concerned with _understanding_ and _building_ **intelligent entities**, that is machines that can **compute** how to **act effectively** and safely in a wide variety of novel situations.

There are **4** main alternative definitions of AI that can be classified along the following **2** dimensions:

- **human** _vs_ **rational**:

>> the first refers to defining intelligence in terms of **fidelity to human performance** while the second refers to defining intelligence as **_"doing the right thing"_** (humans not always do the right think);

and

- **thinking** _vs_ **acting**:

>> the first refers to considering intelligence as a property of **internal thought process**, the second focuses on the **behavior** of the intelligent entity, ignoring the reasoning behind it (which in some cases could be quite simple but achieve great performance).

<style>
.definitions-of-ai {
    display: grid;
    grid-template-columns: 7cm 7cm 0.5cm;
    grid-template-rows: 0.5cm 5cm 5cm;
    gap: 0.5cm;
    justify-content: center;
    margin-right: -0.23cm;
}

.definitions-of-ai-diagram-box {
    background: var(--algorithms);
    border-style: solid;
    border-radius: 0.5cm;
    border-color: var(--text);
    
    display: flex;
    flex-direction: column;
    align-content: center;
    justify-content: center;
}

.defintions-of-ai-definition {
    text-align: center;
    font-size: 28pt;
}

.defintions-of-ai-title {
    text-align: center;
}

.definitions-of-ai-flipped-title {
    writing-mode: vertical-rl;
    text-orientation: mixed;
}
</style>


<div class="definitions-of-ai">
    <div class="defintions-of-ai-title">Human performance</div>
    <div class="defintions-of-ai-title">Rational performance</div>
    <div></div>
    <div class="definitions-of-ai-diagram-box"><div class="defintions-of-ai-definition">Acting humanly</div></div>
    <div class="definitions-of-ai-diagram-box"><div class="defintions-of-ai-definition">Acting rationally</div></div>
    <div class="defintions-of-ai-title definitions-of-ai-flipped-title">Acting</div>
    <div class="definitions-of-ai-diagram-box"><div class="defintions-of-ai-definition">Thinking humanly</div></div>
    <div class="definitions-of-ai-diagram-box"><div class="defintions-of-ai-definition">Thinking rationally</div></div>
    <div class="defintions-of-ai-title definitions-of-ai-flipped-title">Thinking</div>
</div>

---

## Acting humanly

With this definition, an entity which shows **human-like** performance is called intelligent.

Of course we have to better define what we require for a performance to be human-like. One suitable definition is the one given by Turing: he viewed the _physical simulation_ of a person unnecessary to demonstrate intelligence. He defined a test to determine if a machine is intelligent (according to the _acting humanly_ framework): the **Turing test**.

### Turing test

The **Turing test** (in its classic definition) is inspired by a party game known as the **imitation game** with three partecipants: a man `A`, a woman `B` and a third person `C`. `C` is separated from the other two and has to determine who is the man and who is the woman through a series of questions.
Furthermore `A` has to trick `C` making them belive that he is a woman and `B` has to help `A`.
Questions and answers are all in written form.
In the **Turing test** a **machine** takes the place of `A`. If the percentage of times in which `C` is able to identify who is the woman is similar before and after the substitution of `A`, then the machine has passed the test.

## Thinking humanly

To say that a program thinks like a human, we must know how humans think. We can learn about human thought in three ways:

- **introspection**: trying to catch our own thoughts;

- **psychological experiments**: observing a person in action;

- **brain imaging**: observing the brain in action.

Once we have a sufficiently precise theory of the mind, it becomes possible to express the theory as a computer program. It the program's input-output behavior matches the corresponding human behavior, that is **evidence** that some of the program's mechanisms could also be operating in humans.

## Thinking rationally

We can define **_right thinking_** as irrefutable reasoning process. The field which studies **laws of thought** which allow right thinking is known as **logic**. Logicians in the 19th century developed a precise notation for statements about objects of the world and the relations among them. By 1965, programs could, in principle. solve _any_ solvable problem described in logical notation. The so-called **logistic** tradition within artificial intelligence hopes to build on such programs to create intelligent systems.

---

## Acting rationally

An **agent** is just _something that acts_. A **rational agent** is one that acts so as to achieve the _best outcome_ or, when there is uncertainty, the best expected outcome.

In the _"laws of thought"_ approach to AI, the emphasis was on correct inferences. Making correct inferences is sometimes _part_ of being a rational agent, because one way to act rationally is to deduce that a given action is best and then to act on that conclusion. On the other hand, there are ways of acting rationally that cannot be said to involve inference. For example, recoiling from a hot stove is a reflex action that is usually more successful than a slower action taken after careful deliberation.

The rational approach to AI has two advantages over the other approaches:

- It is more general than the _"laws of thought"_ approach because correct inference is just one of several possible mechanisms for achieving rationality;

- It is more amenable to scientific development: the standard of rationality is mathematical well defined and completely general. We can often work back from this specification to derive agent designs that provably achieve it.
