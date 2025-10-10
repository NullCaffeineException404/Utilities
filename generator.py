from langchain_community.llms import GPT4All
from langchain.chains import RetrievalQA


def build_qa_chain(filtered_retriever):
    llm = GPT4All(
    model="./models/gpt4all-falcon-newbpe-q4_0.gguf",
    verbose=True
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=filtered_retriever,
        return_source_documents=True
    )
