from pydantic import BaseModel


class PostFile(BaseModel):
    id: int
    name: str
    link: str
