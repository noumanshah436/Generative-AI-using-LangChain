from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
]

vector = embedding.embed_documents(documents)

print(str(vector))


# this will download the 90 MB model on local and use it.

# we can use the inference API to use it without downloading