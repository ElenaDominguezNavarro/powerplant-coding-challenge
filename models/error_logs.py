from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, VARCHAR, DateTime
from sqlalchemy.orm import relationship
from db.session import Base


class ErrorLogs(Base):
    __tablename__ = "tb_error_logs"

    id = Column(Integer, primary_key=True, index=True)
    #TODO

