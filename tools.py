from langchain_core.tools import tool

from vector_store import query_vector_store


@tool(description="This Tool Retrieves relevant doc related to Insurance plan by using semantic search based on the query.")
def get_insurance_doc(query:str) -> str:
    """
    This Tool Retrieves relevant doc related to Insurance plan by using semantic search based on the query.
    @param query: The query to search for.
    @return: The content of the document.
    """
    [doc] = query_vector_store(query, collection_name="alltius", k=1, filter_dict={
        "info": "insurance",
    })
    return doc.page_content


@tool(description="This Tool Retrieves relevant doc related to angelone investment platform by using semantic search based on the query.")
def get_angelone_doc(query:str) -> str:
    """
    This Tool Retrieves relevant doc related to angelone investment platform by using semantic search based on the query.
    @param query: The query to search for.
    @return: The content of the document.
    """

    [doc] = query_vector_store(query, collection_name="alltius", k=1, filter_dict={
        "info": "angelone",
    })
    return doc.page_content

