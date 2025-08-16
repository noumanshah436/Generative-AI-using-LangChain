from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("books/dl-curriculum.pdf")

docs = loader.load()

print(len(docs))  # total pages in pdf

first_page = docs[0]
print(first_page.page_content)
print(first_page.metadata)


# python 2_pdf_loader.py