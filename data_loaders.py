from doc_loader import read_files_in_directory
from web_loader import scrap_webpages, get_all_links_from_page


def load_data(target_link, whitelisted_paths, remove_page_anchor, docs_path):
    # Load Documents
    docs = read_files_in_directory(docs_path)

    # Load Web Pages
    target_links = get_all_links_from_page(
        target_link, whitelisted_paths, remove_page_anchor)
    web_docs = scrap_webpages(target_links)

    all_docs = docs + web_docs

    for doc in all_docs:
        source = doc.metadata["source"]
        if source.endswith(".pdf"):
            doc.metadata["type"] = "pdf"
            doc.metadata["info"] = "insurance"
        if source.endswith(".docx"):
            doc.metadata["type"] = "docx"
            doc.metadata["info"] = "insurance"
        if source.startswith("https"):
            doc.metadata["type"] = "web"
            doc.metadata["info"] = "angelone"

    return all_docs