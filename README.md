# Annotating and Classifying the Readability of Python Scripts

Contributors: Zhihao Du, Zeyi Yan, Dong Bu

## Overview 

This project is a submission to the assignment called the Annotation Project for [INFO159: Natural Language Processing](https://people.ischool.berkeley.edu/~dbamman/nlp23.html) at UCBerkeley of the Spring 2023 iteration, taught by Professor David Bamman.

The assignment description is as follows:

> You will decide on a new document classification NLP task, annotate data to support it (including creating annotation guidelines), measure your inter-annotator agreement rate, and build a classifier to predict those labels using the methods we discuss in class.

We have decided to classify the readibility of a python script file (file in `.py`). Since we are looking at code files written in a programming language, the content is in a formal language with unambiguous instructions and grammar. However, having an unambiguous language doesn’t mean it is easy to understand, and because programming languages generally have very different syntax and grammar from natural languages, a well-written and functionally-correct code can be very hard to understand and maintain.

**Thus we don’t emphasize the codes themselves. Rather, we look at the comments or comments-like strings that are 1): optional and 2): that do not influence the actual functionalities of the script**, including:

- Comments/function docstring.
- Type hints/Variable annotations.
- Meta-info like file structure, paper references, API references, links to more detailed documentation, etc.
- Coding style, including variable and function names, and whether they are explanatory of their functions.

Please refer to the annotation guideline [here](/deliverables/guidelines.pdf).

## Classification

As Part 4 of the assignment, we set off to build models to approach the task that we have defined ourself. We used classifical logistic regression ([notebook](classification/LogReg.ipynb)) and BERT ([notebook](classification/BERT.ipynb)) to solve the task. Read more in our analysis [here](classification/analysis.pdf).
