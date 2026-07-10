from langchain_tavily import TavilySearch
from langchain.tools import tool


@tool
def web_search(query: str, n_results: int = 5) -> str:
    """
    Search the web for information relevant to the user's query.
    """
    response = TavilySearch(query=query, max_results=n_results).invoke({"query": query})
    return str(response)