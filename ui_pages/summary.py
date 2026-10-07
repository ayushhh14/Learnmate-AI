import streamlit as st

from rag.retriever import get_retriever
from rag.chain import get_llm


def show_summary():

    st.header("📝 Study Summary")

    st.write(
        "Generate an exam-focused summary from your uploaded notes."
    )

    selected_document = st.session_state.get(
        "selected_document"
    )

    if not selected_document:
        st.warning(
            "Please upload and select a document first."
        )
        return

    st.info(
        f"📚 Creating summary from: **{selected_document}**"
    )

    if st.button("Generate Summary"):

        with st.spinner("Generating summary..."):

            retriever = get_retriever(
                selected_document
            )

            docs = retriever.invoke(
                "Find the most important concepts, definitions and topics from this study material."
            )

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            prompt = f"""
You are LearnMate AI, an educational assistant.

Create a clear and exam-focused summary from the
following study material.

Include:

1. Important concepts
2. Important definitions
3. Key points
4. Examples where useful
5. Exam-focused points

Do not invent information that is not present
in the provided material.

Study Material:

{context}

Generate the summary in a well-structured format.
"""

            llm = get_llm()

            response = llm.invoke(prompt)

        st.markdown(response.text)