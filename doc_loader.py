import os
from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_community.document_loaders.word_document import Docx2txtLoader

def files_in_directory(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            absolute_path = os.path.join(os.path.abspath(root), file)
            file_paths.append(absolute_path)
    return file_paths

def read_files_in_directory(directory):
    file_paths = files_in_directory(directory)
    docs = []
    for file_path in file_paths:
        file_path = str(file_path)
        if file_path.endswith(".pdf"):
            doc_loader = PyMuPDF4LLMLoader(file_path)
            docs.extend(doc_loader.load())
        elif file_path.endswith(".docx"):
            doc_loader = Docx2txtLoader(file_path)
            docs.extend(doc_loader.load())
    return docs
