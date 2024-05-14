from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


def main():
    query_text = input("Ask your question: ")
    #carregando o bd
    db = Chroma.load('chroma')
    #procurando as respostas
    results = db.similarity_search_with_relevance_scores(query_text, k = 4)
    if results[0][1] < 0.7 and len(results) == 0:
        print("Sorry, I don't know the answer to that question.")
        return
    

