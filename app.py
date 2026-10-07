import os
import streamlit as st

from ingestion.loader import load_pdf
from ingestion.splitter import split_documents
from ingestion.vectorstore import create_vectorstore

from ui_pages.chat import show_chat
from ui_pages.summary import show_summary
from ui_pages.practice import show_practice
from ui_pages.resources import show_resources


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="LearnMate AI",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# DIRECTORIES
# ============================================================

UPLOAD_DIR = "data/uploads"
CHROMA_DIR = "data/chroma"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CHROMA_DIR, exist_ok=True)


# ============================================================
# SIDEBAR - NAVIGATION
# ============================================================

st.sidebar.title("🎓 LearnMate AI")

st.sidebar.markdown("### Features")

page = st.sidebar.radio(
    "Choose a feature",
    [
        "💬 Ask LearnMate",
        "📝 Summary",
        "🎯 Practice Questions",
        "📚 Resources"
    ]
)


# ============================================================
# HEADER
# ============================================================

st.title("🎓 LearnMate AI")

st.write(
    "Your personalized AI learning assistant powered by "
    "LangChain and RAG."
)


# ============================================================
# UPLOAD SECTION
# ============================================================

st.markdown("## 📄 Study Material")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)


# ============================================================
# SAVE UPLOADED PDF
# ============================================================

if uploaded_file:

    file_path = os.path.join(
        UPLOAD_DIR,
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(
        f"📄 {uploaded_file.name} uploaded successfully!"
    )

    if st.button(
        "⚙️ Process PDF",
        use_container_width=True
    ):

        with st.spinner(
            "Processing your study material..."
        ):

            documents = load_pdf(
                file_path
            )

            chunks = split_documents(
                documents
            )

            if not chunks:

                st.error(
                    "❌ No text could be extracted from this PDF."
                )

                st.warning(
                    "This PDF may be scanned/image-based."
                )

            else:

                # Add document name to metadata
                for chunk in chunks:

                    chunk.metadata["document"] = (
                        uploaded_file.name
                    )

                create_vectorstore(
                    chunks
                )

                st.success(
                    "✅ PDF processed successfully!"
                )

                st.info(
                    f"Created {len(chunks)} text chunks."
                )


# ============================================================
# DOCUMENT SELECTION
# ============================================================

existing_files = [
    f for f in os.listdir(UPLOAD_DIR)
    if f.lower().endswith(".pdf")
]


if existing_files:

    st.markdown("---")

    st.subheader("📚 Select Study Material")

    selected_document = st.selectbox(
        "Choose the document you want LearnMate to use:",
        existing_files
    )

    # Store globally for other pages
    st.session_state["selected_document"] = (
        selected_document
    )

    st.success(
        f"Currently using: **{selected_document}**"
    )

else:

    st.session_state["selected_document"] = None


# ============================================================
# KNOWLEDGE BASE STATUS
# ============================================================

if os.path.exists(CHROMA_DIR) and os.listdir(CHROMA_DIR):

    st.info(
        "🧠 Knowledge base is ready."
    )


# ============================================================
# PAGE ROUTING
# ============================================================

st.markdown("---")


if page == "💬 Ask LearnMate":

    show_chat()


elif page == "📝 Summary":

    show_summary()


elif page == "🎯 Practice Questions":

    show_practice()


elif page == "📚 Resources":

    show_resources()