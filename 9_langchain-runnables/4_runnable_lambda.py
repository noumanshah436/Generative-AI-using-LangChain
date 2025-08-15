from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)

load_dotenv()

# slide 73

# RunnableLambda:

# RunnableLambda is a runnable primitive that allows you to apply custom Python functions within an AI pipeline.
# (simply means we can convert out python function into a runnable)
# It acts as a middleware between different AI components, enabling preprocessing,
# transformation, API calls, filtering, and post-processing in a LangChain workflow.


def word_count(text):
    return len(text.split())


prompt = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "word_count": RunnableLambda(word_count),
        # 'word_count': RunnableLambda(lambda x: len(text.split()))
    }
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

final_result = """{} \n word count - {}""".format(result["joke"], result["word_count"])


print(final_result)

# python "9_langchain-runnables/4_runnable_lambda.py"

# Why did the artificial intelligence break up with his girlfriend?
# Because she didn't have enough RAM to handle his emotions!
#  word count - 20
