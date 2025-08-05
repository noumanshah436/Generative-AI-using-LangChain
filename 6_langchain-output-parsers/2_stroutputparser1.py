from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# The StrOutputParser is the simplest output parser in LangChain. 
# It is used to parse the output of a Language Model (LLM) and return it as a plain string. 

model = ChatOpenAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n{text}",
    input_variables=["text"],
)

# Output parser to convert model responses into simple strings
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)

# This uses LangChain's **pipe (`|`) operator** to pass data through multiple steps:

# 1. Format topic with `template1` (→ "Write a detailed report on black hole")
# 2. Send to `model` → generates detailed report
# 3. `parser` → extracts string output
# 4. Pass that string into `template2` (→ "Write a 5 line summary on the following text: ...")
# 5. Send to `model` again → generates 5-line summary
# 6. `parser` again → extracts the final summary string
