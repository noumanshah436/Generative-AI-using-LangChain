import os
from langchain_openai import OpenAIEmbeddings

# from langchain.vectorstores import Chroma   # deprecated
from langchain_chroma import Chroma  # ✅ new import
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()
print("API key loaded?", os.getenv("OPENAI_API_KEY") is not None)


from langchain.schema import Document

# !pip install langchain chromadb openai tiktoken pypdf langchain_openai langchain-community
# !pip install -U langchain-chroma

# Create LangChain documents for IPL players

doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"},
)
doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"},
)
doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"},
)
doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"},
)
doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"},
)

docs = [doc1, doc2, doc3, doc4, doc5]

vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="my_chroma_db",
    collection_name="sample",
)

# add documents
vector_store.add_documents(docs)

# view documents
docs = vector_store.get(include=["embeddings", "documents", "metadatas"])

# Similarity search
results = vector_store.similarity_search(query="Who among these are a bowler?", k=2)
print(results)
# [
#     Document(
#         id="1bf64bac-fa51-4bf3-b5b2-cdfd6f60f568",
#         metadata={"team": "Mumbai Indians"},
#         page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
#     ),
#     Document(
#         id="38b7623e-43f4-47f0-8c4b-a3e4035ac39b",
#         metadata={"team": "Mumbai Indians"},
#         page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
#     ),
# ]
