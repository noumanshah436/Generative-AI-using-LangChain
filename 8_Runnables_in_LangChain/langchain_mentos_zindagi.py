# -*- coding: utf-8 -*-
"""
A simple "nakli" (fake) version of a LangChain-like pipeline.
It demonstrates how:
    - Prompt Templates
    - LLMs
    - Output Parsers
    - Connectors
can work together in sequence.
"""

from abc import ABC, abstractmethod


# ============================================================
# Base class for all pipeline steps
# ============================================================
class Runnable(ABC):
    """Abstract class representing a step in a pipeline."""

    @abstractmethod
    def invoke(self, input_data):
        pass


# ============================================================
# Prompt Template — formats prompts with placeholders
# ============================================================
class NakliPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        """
        template: string with placeholders like {topic}
        input_variables: list of variables that must be in input_data
        """
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        output = self.template.format(**input_dict)
        return output


# ============================================================
# Fake LLM — just returns a dummy response
# ============================================================
class NakliLLM(Runnable):
    def __init__(self):
        print("[NakliLLM] Initialized.")

    def invoke(self, prompt):
        return {"response": f"(NakliLLM) Pretend answer for: {prompt}"}


# ============================================================
# Output Parser — extracts only the response text
# ============================================================
class NakliStrOutputParser(Runnable):
    def invoke(self, input_data):
        return input_data["response"]


# ============================================================
# Connector — runs a list of steps in sequence
# ============================================================
class RunnableConnector(Runnable):
    def __init__(self, runnable_list, name="Pipeline"):
        self.runnable_list = runnable_list
        self.name = name

    def invoke(self, input_data):
        print(f"\n[Pipeline: {self.name}] Starting execution...\n")
        for i, runnable in enumerate(self.runnable_list, start=1):
            print(f"Step {i}: {runnable.__class__.__name__}")
            print(f"  Input:  {input_data}")
            input_data = runnable.invoke(input_data)
            print(f"  Output: {input_data}\n")
        print(f"[Pipeline: {self.name}] Finished.\n")
        return input_data


# ============================================================
# Example 1 — Poem Generator
# ============================================================
poem_template = NakliPromptTemplate(
    template="Write a {length} poem about {topic}", input_variables=["length", "topic"]
)
llm = NakliLLM()
parser = NakliStrOutputParser()

poem_chain = RunnableConnector([poem_template, llm, parser], name="Poem Chain")

poem_result = poem_chain.invoke({"length": "long", "topic": "India"})
print("Final Output:", poem_result)


# Flow:

# PromptTemplate fills "Write a long poem about india".
# LLM returns {"response": "Dummy response from llm for the prompt: Write a long poem about india"}.
# Parser extracts just the "Dummy response..." string.


# ============================================================
# Example 2 — Joke Generator + Joke Explainer
# ============================================================
template1 = NakliPromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)
template2 = NakliPromptTemplate(
    template="Explain the following joke: {response}", input_variables=["response"]
)

joke_chain = RunnableConnector([template1, llm], name="Joke Generator")
explanation_chain = RunnableConnector([template2, llm, parser], name="Joke Explainer")

# Combine chains into a meta-pipeline
final_chain = RunnableConnector([joke_chain, explanation_chain], name="Full Joke Flow")

final_result = final_chain.invoke({"topic": "cricket"})
print("Final Output:", final_result)


# Flow:

# 1. **chain1**:

#    PromptTemplate makes `"Write a joke about cricket"`.
#    LLM returns a dummy response about that joke.

# 2. **chain2**:

#    PromptTemplate makes `"Explain the following joke ..."`, inserting the joke from chain1.
#    LLM returns a dummy explanation.
#    Parser extracts just the explanation text.
