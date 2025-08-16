from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# DirectoryLoader is a document loader that lets you load multiple documents from a directory
# (folder) of files.

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader,
)

# docs = loader.load() # eager loading, return list of Document objects
docs = loader.lazy_load()  # lazy loading, return generator of Document objects

for document in docs:
    print(document.metadata)
