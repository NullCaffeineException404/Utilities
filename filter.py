from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import EmbeddingsFilter
from langchain_huggingface import HuggingFaceEmbeddings

def build_filtered_retriever(base_retriever):
    filter = EmbeddingsFilter(embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"), similarity_threshold=0.7)
    return ContextualCompressionRetriever(base_compressor=filter, base_retriever=base_retriever)
