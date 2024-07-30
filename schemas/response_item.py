from pydantic import BaseModel


# Shared properties
class ResponseItemBase(BaseModel):
    name: str
    p: float

# Properties to return to client
class ResponseItem(ResponseItemBase):
    name: str
    p: float

    class Config:
        orm_mode = True