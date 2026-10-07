# rag/chain.py

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from rag.retriever import get_retriever
from rag.prompts import RAG_PROMPT


def get_llm():

    llm = ChatOllama(
        model="qwen3:4b",
        temperature=0.2
    )

    return llm


def format_docs(docs):

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


def create_rag_chain():

    retriever = get_retriever()
    llm = get_llm()

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | RAG_PROMPT
        | llm
        | StrOutputParser()
    )

    return rag_chain