import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import AzureOpenAIEmbeddings
from pydantic import SecretStr

load_dotenv(override=True)
from time import sleep

embedding = AzureOpenAIEmbeddings(
    azure_endpoint=os.environ.get("AZURE_OAI_EMBEDDING_ENDPOINT"),
    azure_deployment=os.environ.get("AZURE_OAI_EMBEDDING_DEPLOYMENT"),
    api_key=SecretStr(os.environ.get("AZURE_OAI_EMBEDDING_KEY")),
    api_version=os.environ.get("AZURE_OAI_EMBEDDING_API_VERSION"),
)


def add_documents_to_vector_store(docs, collection_name):
    chroma = Chroma(
        collection_name=collection_name,
        embedding_function=embedding,
        persist_directory="vector_store",
    )
    ids = []
    print("Adding documents to vector store...", len(docs))
    for doc in docs:
        [idx] = chroma.add_documents([doc])
        sleep(1) # To avoid rate limit
        ids.append(idx)
    return ids


def query_vector_store(query, collection_name, k, filter_dict=None):
    chroma = Chroma(
        collection_name=collection_name,
        embedding_function=embedding,
        persist_directory="vector_store",
    )
    results = chroma.similarity_search(query, k=k, filter=filter_dict)
    return results