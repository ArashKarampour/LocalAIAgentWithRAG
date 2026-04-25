This is a simple AI Agent with RAG(Retrieval Augmented Generation) capabilities. It can be used to create a chatbot that can answer questions based on a given knowledge base.

Here the csv file is used as a knowledge base for a restaurant reviews.
It could be also a website or reviews from google.
Different types of data loaders could be used from langchain data loaders to load the data into the vector store.

Here is an Ollama model and embedding model used , you can replace it with any other model and embedding model of your choice.

Below you can have an overview of the RAG Architecture and how it works.

![RAG Architecture](images/RAG_Architecture.avif)

The RAG architecture consists of three main components:
1. **Retriever**: This component is responsible for retrieving relevant documents from the knowledge base based on the user's query. It uses a vector store to store the documents and an embedding model to convert the documents and the query into vectors for similarity search.
2. **Generator**: This component is responsible for generating a response based on the retrieved documents. It uses a language model to generate a response that is coherent and relevant to the user's query.
3. **Knowledge Base**: This is the source of information that the retriever uses to find relevant documents. It can be a database, a collection of documents, or any other source of information.

Here also you can see the flow of the RAG architecture:

![RAG flow](images/rag_retrieval_generation.avif)

The flow of the RAG architecture is as follows:
1. The user inputs a query.
2. The retriever retrieves relevant documents from the knowledge base based on the query.
3. The generator takes the retrieved documents and the user's query as input and generates a response.
4. The response is returned to the user.
