from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base

class Destination(Base):
    __tablename__ = 'destinations'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    location = Column(String, nullable=False)
    key_feature = Column(String)
    conservation_status = Column(String)
    established = Column(Integer)
    area = Column(String)
    description = Column(Text)
    images = Column(JSON, default=[]) 
    created_at = Column(DateTime, default=datetime.now)
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user = relationship("User", back_populates="destinations")
    blogs = relationship("Blog", secondary="blog_destinations", back_populates="destinations")
    
    def __repr__(self):
        return f"<Destination(id={self.id}, name='{self.name}')>"