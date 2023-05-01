from config import db
import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Table(db.Model):
    __tablename__ = 'table'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(80), nullable=False)
    #description = Column(String(1000), nullable=True)
    user_id = Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    items = db.relationship('Items', backref=db.backref('table', lazy=True))
    #date_created
    __table_args__ = (
        db.UniqueConstraint('name', 'user_id'),
    )

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }
    def adminformat(self):
       return {
           'id': self.id,
           'name': self.name,
           'user_id': self.user_id,
           'items':self.items
       }


class Items(db.Model):
    __tablename__ = 'item'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(80), nullable=False)
    type = Column(String(80), nullable=False)
    table_id = Column(UUID(as_uuid=True), db.ForeignKey('table.id'), nullable=False)
    #date_created
    #date_updated
    __table_args__ = (
        db.UniqueConstraint('name', 'table_id'),
    )

    def __init__(self, name, type, table_id):
        self.name = name
        self.type = type
        self.table_id = table_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'table_id': self.table_id
        }

class Data(db.Model):
    __tablename__ = 'data'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    value = Column(String(80), nullable=False)
    item_id = Column(UUID(as_uuid=True), db.ForeignKey('item.id'), nullable=False)
    #date_created
    #date_updated
    def __init__(self, value, item_id):
        self.value = value
        self.item_id = item_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id': self.id,
            'value': self.value,
            'item_id': self.item_id
        }