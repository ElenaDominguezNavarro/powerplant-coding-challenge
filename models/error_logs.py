from sqlalchemy import Column, Integer, DateTime, Text
from datetime import datetime, timezone
from db.session import Base


class ErrorLogs(Base):
    __tablename__ = "tb_error_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False)
    error_message = Column(Text, nullable=False)

