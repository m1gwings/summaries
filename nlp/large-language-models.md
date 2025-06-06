---
marp: true
theme: summary
math: mathjax
---
# Large Language Models

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Mark Carman's slides_)

</div>

**Large Language Models** are, as the name suggests, just really large language models.

## LLMs vs Chatbots

LLMs and **Chatbots** are similar but not the same:
- LLMs are trained to predict the next token in text;
- Chatbots are trained to converse with the user.

Reinforcement Learning from Human Feedback (RLHF) allows to fine-tune LLMs into Chatbots by having **lots of conversations** with **real users** and receiving **feedback** from them on which answers they found appropriate/correct.

Chatbots are designed to generate responses that please users.

## Prompting LLMs

During the fine-tuning of a LLM into a chatbot, the model has been trained to have conversations with users. It recognizes special tokens used to separate different parts of the conversation.
There are three different types of message:
- **System messages**: they contain instructions on how chatbot should respond during conversation.
- **User messages**: they are the requests from the user to the chatbot.
- **Assistant messages**: they contain the chatbot's response.

LLMs are just text-in/text-out models, so all messages (even past responses from the chatbot) are serialized by inserting special tokens and concatenating messages into a single conversation. Chat templates contain the information on formatting the conversation as text.

## Chain-of-thought (CoT) reasoning

For **complicated tasks**, such as solving maths homework problems, it makes sense to get the model to **explain its reasoning**. In fact, by **prompting the model to explain** while answering we can get **better performance** from the LLM. For example, we can pre-append to the task in the prompt the sentence "Let's think step by step". This is known as **zero-shot Chain-of-Thought**.

---

For question answering, we can find answers the LLM is most confident about with the following process. We sample multiple outputs from the LLM, thereby generating multiple responses to the question. Then we count the frequency of each distinct response generated and choose the response with the highest frequency since the most common response should be the most likely to be right. Another approach could get the model to critique its own answer and provide information to the user only when the model agrees that the response was correct.

## Test-time Compute Scaling

Recent models like Deepseek-R1 [Januray 2025] are trained to improve the reasoning ability by structuring the output into two fields: think and answer. The model learns how much time to invest in reasoning about the problem before committing to the answer.
This process is called **test-time compute scaling**. Over training iterations, the model learns to produce longer responses, i.e. to spend more time "thinking".

## Limitations of LLM-based chatbots

There are some limitations to LLM-based chatbots.

The first and most important are **hallucinations**: LLMs sometimes just make up stuff. Indeed, the models are trained to produce content that people like to read and this goal can be in conflict with the requirement to **report only facts** (and tell the truth). There are different types of hallucinations:
- **Conflicting with the task**: the chatbot doesn't perform the requested task.
- **Conflicting with the source**: the chatbot response is in contrast with the information provided by the user.
- **Conflicting with the world knowledge**: the chatbot response is in contrast with its background knowledge of the world.

LLM chatbots lack of robustness: small changes in the prompt can cause big changes in the performance on some tasks. In general, the better written (clearer, less ambiguous) the prompt, the better the performance.

Some people (particularly ethics researchers) try to get the chatbot to say something **harmful** or in violation of its system prompt. This is known as **jailbreaking**.
Other people try to get the chatbot to reveal **training data** which it has potentially memorized: this is known as **extraction**.

## Scaling laws for LLMs

Various papers have investigated the scaling performance of LLMs. There is a linear relationship for performance with respect to:
- log of the computation time;

---

- log of the training dataset size;
- log of the number of parameters in model.

The **Chinchilla scaling law** for training transformer language models suggests that wen given an **increased budget** (in FLOPs), to achieve compute-optimal, the **number of model parameters** (N) and the **number of tokens** for training the model (D) **should scale in approximately equal proportions**. 

When training a large model, the **learning rate** needs to drop proportionally as model size increases. There exist techniques to predict the best rate.

## Recent extensions to transformer architecture

Now we list some of the recent extensions to the transformer architecture.
- Normalization performed on the input to the **self-attention** and **FFNN** blocks rather than on the residual stream.
- 
