from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config.config import CHROMA_PATH


def get_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings


def create_vectorstore(chunks):

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    return vectorstore