from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base_class import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255), nullable=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
