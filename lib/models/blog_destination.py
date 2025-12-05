from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.sql import func
from datetime import datetime
from . import Base

class BlogDestination(Base):
    __tablename__ = 'blog_destinations'
    
    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, ForeignKey('blogs.id'), nullable=False)
    destination_id = Column(Integer, ForeignKey('destinations.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
        
    __table_args__ = (
        UniqueConstraint('blog_id', 'destination_id', name='uq_blog_destination'),
    )
    
    def __repr__(self):
        return f"<BlogDestination(blog_id={self.blog_id}, destination_id={self.destination_id})>"