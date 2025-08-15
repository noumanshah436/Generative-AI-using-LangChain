from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
)

load_dotenv()

# slide 72

# RunnablePassthrough is a special Runnable primitive that simply returns the input as output
# without modifying it.

prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}", input_variables=["text"]
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),  # i also want to print the joke, so i use RunnablePassthrough to gireturn the input joke as it is
        "explanation": RunnableSequence(prompt2, model, parser),
    }
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({"topic": "cricket"}))

# $ python 9_langchain-runnables/3_runnable_passthrough.py

# {
#     "joke": "Why did the cricket team go to the bank?\n\nBecause they needed to open a savings account for all their runs!",
#     "explanation": 'In cricket, "runs" refer to the points scored by the team by running between two wickets. In this joke, the cricket team is going to the bank to open a savings account to store all the runs they are scoring during their matches. It is a pun on the word "runs," as it can also refer to money in this context.',
# }
