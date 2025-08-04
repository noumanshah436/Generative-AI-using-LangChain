from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html

model = ChatOpenAI()

# detailed way
template2 = PromptTemplate(
    template="Greet this person in 5 languages. The name of the person is {name}",
    input_variables=["name"],
)

# fill the values of the placeholders
prompt = template2.invoke({"name": "Nouman"})
# Or we can use format method:
# prompt = template2.format(name="Nouman")


result = model.invoke(prompt)

print(result.content)

# python "4_langchain-prompts/1_prompt_template.py"

# 1. English: Hello Nouman!
# 2. French: Bonjour Nouman!
# 3. Spanish: ¡Hola Nouman!
# 4. Arabic: أهلاً وسهلاً نعمان!
# 5. German: Hallo Nouman!