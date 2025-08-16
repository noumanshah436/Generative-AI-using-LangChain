from langchain_community.document_loaders import CSVLoader


# CSVLoader is a document loader used to load CSV files into LangChain
# Document objects —one per row, by default.

loader = CSVLoader(file_path="Social_Network_Ads.csv")

docs = loader.load()

print(len(docs))  # For each row it gives separate Document object
print(docs[0])  # document for the first row of csv
