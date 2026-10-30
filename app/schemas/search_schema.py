from pydantic import BaseModel, ConfigDict, Field
from typing import Literal

class SearchQuery(BaseModel):
    query: str = Field(description="The text to be searched on the textmap.")
    versions: list[str] = Field(description="List of versions to look for.", default_factory=list,)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "query": "Hyperborea",
                "versions": []
            }
        },
    )
    
class MassSearchQuery(BaseModel):
    queries: list[str] = Field(description="Variety of queries to be searched on the textmap.")
    versions: list[str] = Field(description="List of versions to look for.", default_factory=list,)
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "queries": [
                    "Hyperborea",
                    "Koitar",
                    "Seutervoinen",
                    "Anacharsis",
                    "First Angel"
                ],  
                "versions": []
            }
        }
    )

class SearchResponse(BaseModel):
    id: str = Field(description="ID of the text response. Can be numerical or alphanumerical.")
    en: str | None  = Field(description="English version of the text.")
    chs: str | None = Field(description="Original (chinese) version of the text.")
    version: str = Field(description="Information about the version from where the text comes from.")
    text_source: Literal["textmap", "readable", "subtitle"] = Field(description="Information about the source from where the text comes from.")
    model_config = ConfigDict(from_attributes=True)

class MassSearchResponse(BaseModel):
    query: str = Field(description="The text to be searched on the textmap.")
    response: list[SearchResponse] = Field(description="Response of the query")