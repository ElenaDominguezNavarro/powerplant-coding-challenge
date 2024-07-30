from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from typing import Union


# Shared properties
class ErrorLogsBase(BaseModel):
    id: Union[int, None] = None
    timestamp: Union[datetime, None] = None
    error_message: Union[str, None] = None


# Properties to receive on item creation
class ErrorLogsCreate(ErrorLogsBase):
    error_message: str
    timestamp: datetime
    pass


class ErrorLogsUpdate(ErrorLogsBase):
    pass


# Properties to return to client
class ErrorLogs(ErrorLogsBase):
    id: int

    class Config:
        orm_mode = True
