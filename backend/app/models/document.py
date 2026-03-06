from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import EncryptedType, AesEngine
from backend.app.db.base import Base
from backend.app.security.encryption import get_encryption_key

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(EncryptedType(String, get_encryption_key, AesEngine, 'pkcs5'), nullable=False)
    metadata = Column(EncryptedType(String, get_encryption_key, AesEngine, 'pkcs5'))
