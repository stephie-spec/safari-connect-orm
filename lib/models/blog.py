from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
	pass

class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now )

    user = relationship("User", back_populates="blogs")
    destinations = relationship("Destination", secondary="blog_destinations", back_populates="blogs")
    
    
    def __repr__(self):
        return f"<Blog(id={self.id}, title='{self.title}')>"