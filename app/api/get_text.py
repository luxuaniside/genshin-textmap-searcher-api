from fastapi import APIRouter
from app.schemas.search_schema import SearchQuery, SearchResponse, MassSearchQuery, MassSearchResponse
from app.services.text_search import search_text, mass_text_search
router = APIRouter(
    prefix="/search",
    tags=["Readable Search"]
)


@router.post("/")
def search_text_query(query: SearchQuery) -> list[SearchResponse]:
    """Initializes a text query search.

    Args:
        query (SearchQuery): Contains the text to look for and the set of versions to look for.

    Returns:
        list[SearchResponse]: All available responses.
    """
    responses = search_text(query.query, query.versions)
    
    results = []
    for text_response in responses:
        result = SearchResponse(
            id=text_response.id,
            en=text_response.en,
            chs=text_response.chs,
            version=text_response.version,
            text_source=text_response.text_source,
        )
        results.append(result)

    return results

@router.post("/mass_search")
def mass_search_text_query(query: MassSearchQuery) -> list[MassSearchResponse]:
    responses = mass_text_search(query)
    

    return responses