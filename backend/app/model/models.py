from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Text
from datetime import datetime
Base = declarative_base()
class ApiCallLog(Base):
    __tablename__ = 'api_call_log'
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(String, index=True)
    endpoint = Column(String)
    status_code = Column(Integer)
    response_body = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
class CircuitBreakerState(Base):
    __tablename__ = 'circuit_breaker_state'
    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, unique=True)
    state = Column(String)  # OPEN, CLOSED, HALF_OPEN
    failure_count = Column(Integer, default=0)
    last_failure = Column(DateTime, nullable=True)
