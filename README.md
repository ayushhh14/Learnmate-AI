# 🎓 LearnMate AI

> An AI-powered personalized learning assistant that transforms students' study material into interactive learning experiences using Retrieval-Augmented Generation (RAG).

---

## 📌 Overview

**LearnMate AI** is a LangChain and Retrieval-Augmented Generation (RAG) based learning assistant designed to help students study more effectively from their own notes and educational material.

Students can upload PDF study material and interact with it through an AI-powered interface.

LearnMate AI can:

- Answer questions from uploaded study material
- Generate exam-focused summaries
- Generate practice questions
- Identify important topics
- Recommend useful learning resources
- Retrieve relevant source pages from the uploaded document

The system uses **semantic search and vector embeddings** to retrieve relevant information from the student's documents before generating a response.

This helps keep responses grounded in the uploaded study material and reduces unnecessary hallucination.

---

# 🎯 Problem Statement

Students often have large amounts of study material such as:

- Lecture notes
- PDF textbooks
- Placement preparation documents
- Study guides
- Technical documentation

Manually searching through these documents can be time-consuming, especially during exam and placement preparation.

Traditional chatbots may also provide generic answers that are not directly related to the student's study material.

### LearnMate AI solves this problem by providing:

> **A personalized AI learning assistant that understands and interacts with the student's own study material.**

---

## 🛠️ Tech Stack

- **Python** – Core programming language
- **Streamlit** – Web application and user interface
- **LangChain** – RAG pipeline and LLM orchestration
- **Ollama** – Local LLM inference
- **Qwen3:4b** – Local language model
- **ChromaDB** – Vector database
- **Hugging Face** – Text embeddings
- **Sentence Transformers** – Semantic embeddings
- **PyPDF** – PDF text extraction
- **Git & GitHub** – Version control and project hosting
