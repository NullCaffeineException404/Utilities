from sample_docs import load_sample_docs
from retriever import build_retriever
from filter import build_filtered_retriever
from generator import build_qa_chain

def main():
    docs = load_sample_docs()
    retriever = build_retriever(docs)
    filtered_retriever = build_filtered_retriever(retriever)
    qa_chain = build_qa_chain(filtered_retriever)

    query = "What is the coverage for death during extreme sports in this policy?"
    response = qa_chain.invoke(query)
    answer = response["result"]

    print("Answer:", answer)

if __name__ == "__main__":
    main()
