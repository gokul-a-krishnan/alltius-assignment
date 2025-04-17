import os

from data_loaders import load_data
from vector_store import add_documents_to_vector_store

def main():
    if not os.listdir("vector_store"):
        print("No vector store")
        # Load Documents
        all_docs = load_data("https://www.angelone.in/support", whitelisted_paths=[
            "/support", "/knowledge-center"], remove_page_anchor=True, docs_path="docs")
        add_documents_to_vector_store(all_docs, "alltius")
        print("Vector store created")
    else:
        print("Vector store already exists")


if __name__ == "__main__":
    main()
