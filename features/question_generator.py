from langchain_core.prompts import ChatPromptTemplate

from rag.chain import get_llm


QUESTION_PROMPT = ChatPromptTemplate.from_template("""
You are an expert exam question generator.

Generate {count} questions from the provided study material.

Difficulty:
{difficulty}

Rules:

- Questions must be based on the material.
- Do not introduce unrelated topics.
- Mix conceptual and application-based questions.
- Provide answers.
- Keep the questions suitable for students.

Study Material:

{context}

Generate the questions in this format:

Q1. Question

Answer:
...

Q2. Question

Answer:
...
""")


def generate_questions(context, count=5, difficulty="Medium"):

    llm = get_llm()

    chain = QUESTION_PROMPT | llm

    response = chain.invoke({
        "context": context,
        "count": count,
        "difficulty": difficulty
    })

    return response.content