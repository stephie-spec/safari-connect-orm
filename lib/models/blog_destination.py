from sqlalchemy import Column, Integer, ForeignKey, DateTime, Table
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
	pass

blog_destinations = Table('blog_destinations', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('blog_id', Integer, ForeignKey('blogs.id'), nullable=False),
    Column('destination_id', Integer, ForeignKey('destinations.id'), nullable=False),
    Column('created_at', DateTime, default=datetime.now)
)