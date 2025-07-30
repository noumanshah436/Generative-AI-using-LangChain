from langchain_core.prompts import ChatPromptTemplate

# https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful {domain} expert"),
        ("human", "Explain in simple terms, what is {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "cricket", "topic": "Dusra"})

print(prompt)

# $ python "4_langchain-prompts/7_chat_prompt_template.py"

# output:
# messages = [
#     SystemMessage(
#         content="You are a helpful cricket expert",
#         additional_kwargs={},
#         response_metadata={},
#     ),
#     HumanMessage(
#         content="Explain in simple terms, what is Dusra",
#         additional_kwargs={},
#         response_metadata={},
#     ),
# ]
