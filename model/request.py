from pydantic import BaseModel
from typing import Optional

class Request(BaseModel):
    query:str
    context_documents:Optional[str] = None