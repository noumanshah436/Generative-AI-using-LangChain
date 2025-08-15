from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

# 1. RunnableSequence

# RunnableSequence is a sequential chain of runnables in LangChain that executes each step one after another, passing the output of one step as the input to the next.
# It is useful when you need to compose multiple runnables together in a structured workflow.

prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}", input_variables=["text"]
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({"topic": "AI"}))

# $ python 9_langchain-runnables/1_runnable_sequence.py
# This joke plays on the stereotype that artificial intelligence (AI) systems are advanced and capable of doing many things, including taking jobs away from humans. In this case, the AI spent all its money on upgrades to make itself more advanced and employable, but still couldn't find a job because it's just a machine and not capable of actually working in the traditional sense. This leads to the AI going broke because it has invested all its resources in upgrades that ultimately didn't help it achieve its goal of finding a job.