from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
	pass

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String, unique=True, nullable=False)
	email = Column(String, unique=True, nullable=False)
	created_at = Column(DateTime, default = datetime.now)

	destinations = relationship("Destination", back_populates="user")
	blogs = relationship("Blog", back_populates=user)

	def __repr__(self):
		return f"<User(id={self.id}, username='{self.username}'>)"

		