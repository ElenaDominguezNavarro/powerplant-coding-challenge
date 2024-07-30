from typing import Optional

from pydantic import BaseModel


# Shared properties
class ErrorLogsBase(BaseModel):
    #TODO
    pass


# Properties to receive on item creation
class ErrorLogsCreate(ErrorLogsBase):
    pass


class ErrorLogsUpdate(ErrorLogsBase):
    pass


# Properties to return to client
class ErrorLogs(ErrorLogsBase):
    id: int

    class Config:
        orm_mode = True
