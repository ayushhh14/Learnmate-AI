import streamlit as st

from rag.retriever import get_retriever
from rag.chain import get_llm


def show_practice():

    st.header("🎯 Practice Questions")

    selected_document = st.session_state.get(
        "selected_document"
    )

    if not selected_document:
        st.warning(
            "Please upload and select a document first."
        )
        return

    st.info(
        f"📚 Generating questions from: **{selected_document}**"
    )

    difficulty = st.selectbox(
        "Select difficulty:",
        ["Easy", "Medium", "Hard"]
    )

    count = st.slider(
        "Number of questions:",
        min_value=1,
        max_value=20,
        value=5
    )

    if st.button("Generate Questions"):

        with st.spinner(
            "Creating questions from your notes..."
        ):

            retriever = get_retriever(
                selected_document
            )

            docs = retriever.invoke(
                "Find the important concepts and topics from this study material."
            )

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            prompt = f"""
You are LearnMate AI, an expert exam preparation assistant.

Generate {count} practice questions based ONLY on
the following study material.

Difficulty: {difficulty}

Requirements:

- Questions must be based on the provided material.
- Do not introduce unrelated concepts.
- Include conceptual and application-based questions.
- Provide the correct answer after every question.

Study Material:

{context}

Format:

Q1. Question

Answer:
...

Q2. Question

Answer:
...

Continue until {count} questions are generated.
"""

            llm = get_llm()

            response = llm.invoke(prompt)

        st.markdown(response.text)