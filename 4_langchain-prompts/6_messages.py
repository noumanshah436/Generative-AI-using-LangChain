from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about LangChain"),
]

result = model.invoke(messages)
print(result.content)
# LangChain is a decentralized blockchain-based platform that focuses on supporting the language industry. 
# It aims to provide solutions for language translation, interpretation, and localization services through the 
# use of blockchain technology. LangChain aims to increase transparency, security, and efficiency in the 
# language industry by leveraging blockchain technology to connect language service providers and clients, 
# facilitate payments, and ensure the quality of language services. Overall, LangChain seeks to revolutionize 
# the language industry by creating a decentralized and trustless ecosystem for language professionals and clients 
# to collaborate and transact securely.


messages.append(AIMessage(content=result.content))

print(messages)
# [
#     SystemMessage(
#         content="You are a helpful assistant",
#         additional_kwargs={},
#         response_metadata={},
#     ),
#     HumanMessage(
#         content="Tell me about LangChain", additional_kwargs={}, response_metadata={}
#     ),
#     AIMessage(
#         content="LangChain is a decentralized blockchain-based platform that focuses on supporting the language industry. It aims to provide solutions for language translation, interpretation, and localization services through the use of blockchain technology. LangChain aims to increase transparency, security, and efficiency in the language industry by leveraging blockchain technology to connect language service providers and clients, facilitate payments, and ensure the quality of language services. Overall, LangChain seeks to revolutionize the language industry by creating a decentralized and trustless ecosystem for language professionals and clients to collaborate and transact securely.",
#         additional_kwargs={},
#         response_metadata={},
#     ),
# ]
