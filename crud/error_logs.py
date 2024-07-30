from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.error_logs import ErrorLogs
from schemas.error_logs import ErrorLogsCreate, ErrorLogsBase


class CRUDErrorLogs(CRUDBase[ErrorLogs, ErrorLogsCreate, ErrorLogsBase]):
    pass


error_logs = CRUDErrorLogs(ErrorLogs)
