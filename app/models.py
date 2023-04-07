from app import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    id: int = Column(Integer, primary_key=True)
    username: str = Column(String(64), index=True, unique=True)
    email: str = Column(String(64), index=True, unique=True)

    def __repr__(self) -> str:
        return f"<User {self.username}>"
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }