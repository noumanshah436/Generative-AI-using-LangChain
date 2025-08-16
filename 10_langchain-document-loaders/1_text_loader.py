from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


# TextLoader:
# TextLoader is a simple and commonly used document loader in LangChain that reads plain text 
# (.txt) files and converts them into LangChain Document objects.

# Use Case:
# Ideal for loading chat logs, scraped text, transcripts, code snippets, or any plain text data 
# into a LangChain pipeline.

# Limitation:
# Works only with .txt files•


model = ChatOpenAI()

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=["poem"],
)

parser = StrOutputParser()

loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({"poem": docs[0].page_content}))


# python 1_text_loader.py 