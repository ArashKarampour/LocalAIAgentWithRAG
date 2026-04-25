from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2:3b")

template = """
You are an exeprt in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while True:
    print("\n\n----------------------------------------\n\n")
    question = input("Enter your question about the pizza restaurant (or 'q' to quit): ")
    print("\n\n")
    if question.lower() == 'q':
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": [], "question": "What is the best pizza in town?"})
    print(result)