import streamlit as st

from rag.retriever import get_retriever
from rag.chain import get_llm


def show_resources():

    st.header("📚 Learning Resources")

    st.write(
        "Find useful resources related to your uploaded study material."
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
        f"📚 Finding resources for: **{selected_document}**"
    )

    if st.button("Find Resources"):

        with st.spinner(
            "Analyzing your study material..."
        ):

            retriever = get_retriever(
                selected_document
            )

            docs = retriever.invoke(
                "Identify the major topics covered in this study material."
            )

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            prompt = f"""
You are LearnMate AI, an educational resource assistant.

Analyze the following study material and identify
the major topics.

For each topic provide:

- Topic name
- What the student should learn
- Recommended resource type
- Useful search query

Do not invent URLs or specific resources that
you cannot verify.

Study Material:

{context}
"""

            llm = get_llm()

            response = llm.invoke(prompt)

        st.markdown(response.text)