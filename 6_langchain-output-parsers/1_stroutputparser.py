from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# example without any parser

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

model = ChatHuggingFace(llm=llm)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=["text"],
)

prompt1 = template1.invoke({"topic": "black hole"})

result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})

result1 = model.invoke(prompt2)

print(result1.content)
# Black holes are regions of spacetime with such immense gravity that their event horizon prevents escape. Formed from 
# the collapse of massive stars, black holes range in size from stellar-mass to supermassive, with the latter playing a 
# critical role in galaxy formation and evolution.  Their inescapable gravitational pull can be observed through their 
# effects on nearby matter and the creation of gravitational waves. Their existence challenges our current understanding 
# of physics and is a critical area of ongoing research. Further research will focus on unraveling the mysteries of 
# singularities and investigating their impact on the universe.  
