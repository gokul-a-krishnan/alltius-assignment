# RAG-Powered Chatbot with Dual Knowledge Base

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot system that leverages two distinct knowledge sources:
1.  **Insurance Documents:** PDF and DOCX files stored locally in the `docs/` directory.
2.  **AngelOne Web Content:** Information scraped from specified paths on the `angelone.in` website.

The system uses Azure OpenAI for language model capabilities and ChromaDB for efficient vector storage and retrieval. A Gradio interface provides a user-friendly way to interact with the chatbot.

## Features

*   **Dual Knowledge Base:** Seamlessly queries both insurance documents and AngelOne web content based on the user's query context.
*   **Document Processing:** Handles PDF and DOCX file loading and text extraction.
*   **Web Scraping:** Intelligently scrapes relevant content from specified web paths.
*   **Vector Storage:** Utilizes ChromaDB for persistent vector storage, enabling efficient semantic search.
*   **Azure OpenAI Integration:** Leverages powerful Azure OpenAI models for generation and embeddings.
*   **Gradio Web Interface:** Provides an interactive chat interface for users.
*   **Session Management:** Maintains chat history within a session.

## Project Structure

| File                | Purpose                                                                 |
|---------------------|-------------------------------------------------------------------------|
| `app.py`            | Gradio web interface for chat interaction                              |
| `data_loaders.py`   | Combines document and web data loading, adds metadata                  |
| `doc_loader.py`     | Loads PDF/DOCX files from the `docs/` directory                         |
| `main.py`           | Entry point to initialize the vector store if it doesn't exist          |
| `rag_agent.py`      | Core RAG agent logic using LangGraph, Azure OpenAI, and custom tools   |
| `tools.py`          | Defines custom LangChain tools for retrieving insurance/AngelOne docs |
| `vector_store.py`   | Manages ChromaDB vector store creation and querying                     |
| `web_loader.py`     | Handles web scraping, link filtering, and HTML-to-text conversion       |
| `docs/`             | Directory containing insurance-related PDF and DOCX documents           |
| `vector_store/`     | Directory where the ChromaDB vector store is persisted                |
| `.env`              | (Not included) File to store environment variables (Azure keys/endpoints) |
| `pyproject.toml`    | Project metadata and dependencies (managed by Poetry)                   |
| `Readme.md`         | This documentation file                                                 |

## Configuration Requirements

1.  **Environment Variables:** Create a `.env` file in the project root and add the following Azure credentials:
    ```dotenv
    AZURE_OAI_CHAT_ENDPOINT=YOUR_AZURE_CHAT_ENDPOINT
    AZURE_OAI_CHAT_DEPLOYMENT=YOUR_AZURE_CHAT_DEPLOYMENT_NAME
    AZURE_OAI_CHAT_KEY=YOUR_AZURE_CHAT_API_KEY
    AZURE_OAI_CHAT_API_VERSION=YOUR_AZURE_CHAT_API_VERSION

    AZURE_OAI_EMBEDDING_ENDPOINT=YOUR_AZURE_EMBEDDING_ENDPOINT
    AZURE_OAI_EMBEDDING_DEPLOYMENT=YOUR_AZURE_EMBEDDING_DEPLOYMENT_NAME
    AZURE_OAI_EMBEDDING_KEY=YOUR_AZURE_EMBEDDING_API_KEY
    AZURE_OAI_EMBEDDING_API_VERSION=YOUR_AZURE_EMBEDDING_API_VERSION
    ```
2.  **Documents:** Place insurance-related PDF and DOCX files into the `docs/` directory.
3.  **Dependencies:** Install required Python packages. If using Poetry (recommended, based on `pyproject.toml`), run:
    ```bash
    poetry install
    ```
    Otherwise, you might need to manually install packages listed in `pyproject.toml` using `pip`.

4.  **Playwright Browser Setup:** 
    The web scraper requires Playwright browsers. After installing dependencies, run:
    ```bash
    playwright install
    ```

## Usage

1.  **Initialize Vector Store (First Time Only):**
    Run the `main.py` script to load documents/web content and create the vector store.
    ```bash
    python main.py
    ```
    This process might take some time depending on the number of documents and web pages. It only needs to be run once unless the source documents change.

2.  **Start the Chat Application:**
    Run the `app.py` script to launch the Gradio web interface.
    ```bash
    python app.py
    ```
    Access the chat interface through the URL provided by Gradio (usually `http://127.0.0.1:7860` or `http://0.0.0.0:7860`).
