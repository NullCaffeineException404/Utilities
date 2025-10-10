from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def build_retriever(docs):
    vectorstore = FAISS.from_documents(docs, HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
)
    return vectorstore.as_retriever()
