from langchain_core.prompts import ChatPromptTemplate

from rag.chain import get_llm


RESOURCE_PROMPT = ChatPromptTemplate.from_template("""
You are an educational resource recommendation assistant.

Based on the following study material, identify the major topics
and suggest useful learning resources.

For each topic provide:

Topic:
Resource type:
Suggested search/query:
Why it is useful:

Do not invent specific books, URLs, or citations.
If you are unsure about a specific resource, provide a search query
instead.

Material:

{context}
""")


def generate_resources(context):

    llm = get_llm()

    chain = RESOURCE_PROMPT | llm

    response = chain.invoke({
        "context": context
    })

    return response.content