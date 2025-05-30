from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

llm = ChatOpenAI()
embeddings = OpenAIEmbeddings()

def create_retriever(vector_path):
    vectorstore = FAISS.load_local(vector_path, embeddings)
    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
