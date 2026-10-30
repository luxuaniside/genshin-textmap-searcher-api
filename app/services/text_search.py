from sqlalchemy import or_, select, func
from sqlalchemy.orm import Session

from app.database.db import engine
from app.database.models.text_entry import TextEntry

from app.schemas.search_schema import MassSearchQuery, MassSearchResponse, SearchResponse

MAX_QUERY_RESULTS = 1000
def search_text(query_text: str, query_versions: list[str]) -> list[TextEntry]:
    """Handles the search from the database.

    Args:
        query_text: Text to be searched.
        query_versions: Versions to be searched from.

    Returns:
        A list of matching TextEntry objects.
    """
    with Session(engine) as session:
        statement = (
            select(TextEntry)
            .where(
                or_(
                    TextEntry.en.ilike(f"%{query_text}%"),
                    TextEntry.chs.ilike(f"%{query_text}%"),
                )
            )
            .order_by(func.length(TextEntry.en).asc())
            .limit(MAX_QUERY_RESULTS)
        )

        if query_versions:
            statement = statement.where(
                TextEntry.version.in_(query_versions)
            )

        results = session.scalars(statement).all()
        return results
    

def mass_text_search(query: MassSearchQuery) -> list[MassSearchResponse]:
    results = []
    version_list = query.versions
    for search_query in query.queries:
        
        entries: list[TextEntry] = search_text(search_query, version_list)

        responses = []
        for entry in entries:
            response = SearchResponse.model_validate(entry)
            responses.append(response)
       
        result = MassSearchResponse(
            query=search_query,
            response=responses
        )
        
        results.append(result)
        
    return results