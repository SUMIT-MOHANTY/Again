from .. import db
from .encryption import encrypt, decrypt

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    _content = db.Column('content', db.Text, nullable=False)

    @property
    def content(self) -> str:
        return decrypt(self._content)

    @content.setter
    def content(self, plain: str):
        self._content = encrypt(plain)

    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'content': self.content}
