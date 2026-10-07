import streamlit as st

from rag.retriever import get_retriever
from rag.chain import get_llm
from rag.prompts import RAG_PROMPT


def show_chat():

    st.header("💬 Ask LearnMate")

    selected_document = st.session_state.get(
        "selected_document"
    )

    if not selected_document:
        st.warning(
            "Please upload and select a document first."
        )
        return

    st.info(
        f"📚 Answering from: **{selected_document}**"
    )

    question = st.text_input(
        "Ask a question about your uploaded notes:"
    )

    if question:

        with st.spinner("Searching your notes..."):

            retriever = get_retriever(
                selected_document
            )

            docs = retriever.invoke(question)

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            llm = get_llm()

            prompt = RAG_PROMPT.format(
                context=context,
                question=question
            )

            response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response.text)

        st.subheader("📚 Sources")

        for doc in docs:

            source = doc.metadata.get(
                "source",
                selected_document
            )

            page = doc.metadata.get(
                "page",
                "Unknown"
            )

            if page != "Unknown":
                page = page + 1

            st.write(
                f"📄 {source} — Page {page}"
            )