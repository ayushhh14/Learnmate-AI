from langchain_chroma import Chroma

from ingestion.vectorstore import get_embeddings
from config.config import CHROMA_PATH, TOP_K


def get_retriever(document_name=None):

    embeddings = get_embeddings()

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    if document_name:

        retriever = vectorstore.as_retriever(
            search_kwargs={
                "k": TOP_K,
                "filter": {
                    "document": document_name
                }
            }
        )

    else:

        retriever = vectorstore.as_retriever(
            search_kwargs={
                "k": TOP_K
            }
        )

    return retriever