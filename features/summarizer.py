from langchain_core.prompts import ChatPromptTemplate

from rag.chain import get_llm


SUMMARY_PROMPT = ChatPromptTemplate.from_template("""
You are an expert educational assistant.

Create a clear study summary from the following material.

Include:

1. Key concepts
2. Important definitions
3. Important points
4. Examples where useful
5. Exam-focused points

Material:

{context}

Create a concise but useful study summary.
""")


def generate_summary(context):

    llm = get_llm()

    chain = SUMMARY_PROMPT | llm

    response = chain.invoke({
        "context": context
    })

    return response.content