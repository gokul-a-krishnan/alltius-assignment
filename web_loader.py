from bs4 import BeautifulSoup, Comment
import requests
from urllib.parse import urlparse

from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import Html2TextTransformer


def get_all_links_from_page(target_link, whitelisted_paths=None, remove_page_anchor=False):
    response = requests.get(target_link)
    soup = BeautifulSoup(response.content, 'html.parser', )
    links = [a['href'] for a in soup.find_all('a', href=True)]

    parsed_url = urlparse(target_link)
    host = f"{parsed_url.scheme}://{parsed_url.netloc}"

    links = [host + link if link[0] == '/' else link for link in links] # convert relative links to absolute
    links = [target_link + link if link.startswith("#") else link for link in links] # convert page anchors to absolute
    links = [link for link in links if link.startswith(host)] # filter out links that don't belong to the same host

    if whitelisted_paths:
        links = [link for link in links if any(path in link for path in whitelisted_paths)] # filter out links that don't belong to the whitelisted paths
    if remove_page_anchor:
        links = [link.split('#')[0] for link in links] # remove page anchors
    links = list(set(links))
    return sorted(links)

def scrap_webpages(target_links):
    loader = AsyncChromiumLoader(target_links)
    docs = loader.load()
    transformer = Html2TextTransformer()
    transformed_docs = transformer.transform_documents(docs)
    return transformed_docs

