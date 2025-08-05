from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

"""
Using LangChain to create a conditional AI response system for user feedback.

1. It first classifies the sentiment of a given feedback as either "positive" or "negative".
2. Based on the sentiment, it dynamically chooses the appropriate response generation prompt.
3. The classification and branching logic is composed using LangChain's Runnable interfaces:
   - `RunnableBranch` allows conditional execution based on model output.
   - `PydanticOutputParser` is used to enforce and parse a structured output for sentiment classification.
4. If the sentiment is not recognized, a default message is returned.

This demonstrates how to build dynamic, structured, and safe chains using LangChain's composable primitives.
"""


model = ChatOpenAI()

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )


parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()},
)

# First chain: classify feedback sentiment (either positive or negative)
classifier_chain = prompt1 | model | parser2

# print(classifier_chain.invoke({"feedback": "This is a beautiful phone"}))
# output: sentiment='positive'


prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"],
)

# Branch logic: choose which prompt to run based on sentiment result
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment"),
)

# Full chain: classify → branch to appropriate responder
chain = classifier_chain | branch_chain

print(chain.invoke({"feedback": "This is a beautiful phone"}))

chain.get_graph().print_ascii()


# output:

# Thank you so much for your kind words! I'm glad to hear that you had a positive experience. Let me know if there's anything else I can help with.

#     +-------------+
#     | PromptInput |
#     +-------------+
#             *
#             *
#             *
#    +----------------+
#    | PromptTemplate |
#    +----------------+
#             *
#             *
#             *
#      +------------+
#      | ChatOpenAI |
#      +------------+
#             *
#             *
#             *
# +----------------------+
# | PydanticOutputParser |
# +----------------------+
#             *
#             *
#             *
#        +--------+
#        | Branch |
#        +--------+
#             *
#             *
#             *
#     +--------------+
#     | BranchOutput |
#     +--------------+
