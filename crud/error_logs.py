from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.error_logs import ErrorLogs
from schemas.error_logs import ErrorLogsCreate, ErrorLogsBase


class CRUDErrorLogs(CRUDBase[ErrorLogs, ErrorLogsCreate, ErrorLogsBase]):
    pass

    async def create_error_log(self, db: Session, error:ErrorLogsCreate):
        error_log_data = error.dict()
        db_error_log = ErrorLogs(**error_log_data)
        db.add(db_error_log)
        db.commit()
        db.refresh(db_error_log)
        return db_error_log


error_logs = CRUDErrorLogs(ErrorLogs)
