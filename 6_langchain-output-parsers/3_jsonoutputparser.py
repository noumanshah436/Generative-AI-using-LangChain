from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Load environment variables (e.g. Hugging Face API key)
load_dotenv()

# Set up the Hugging Face model
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

# Create chat model wrapper
model = ChatHuggingFace(llm=llm)

# Parser to extract JSON output
parser = JsonOutputParser()

# Create prompt with topic and format instructions
template = PromptTemplate(
    template="Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# This is a LangChain pipeline: prompt → model → parser
# It builds a full chain that:
#   - Formats the prompt with the topic and format instructions
#   - Sends it to the model
#   - Parses the model's response as JSON
chain = template | model | parser

# Run the chain with a topic
result = chain.invoke({"topic": "black hole"})

# Print the result
print(result)

# [
#     {
#         "fact": "Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape.",
#         "details": "Once an object becomes massive enough, gravity begins to bend the fabric of spacetime so that even light's path is disrupted.",
#     },
#     {
#         "fact": "Black holes have immense density:",
#         "details": "They pack the mass of a typical star into a space smaller than a city.",
#     },
#     {"fact": "Black holes are typically not "},
# ]


# ************************************

# Drawbacks of JsonOutputParser:
# 1) It does not enforce schema validation.
