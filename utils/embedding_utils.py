from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

def save_vectors(docs, path):
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(path)

def load_vectors(path):
    return FAISS.load_local(path, embeddings)
