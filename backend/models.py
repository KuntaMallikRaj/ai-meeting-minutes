from sqlalchemy import Column, Integer, String, DateTime, Text, func
from db import Base

class Meeting(Base):
    __tablename__ = "meetings"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    raw_text = Column(Text, nullable=True)
    chunks_count = Column(Integer, default=0)
