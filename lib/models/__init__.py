from sqlalchemy.orm import declarative_base

# Create declarative base
Base = declarative_base()

# Import all models
from .user import User
from .destination import Destination
from .blog import Blog
from .blog_destination import BlogDestination

# Export all models
__all__ = ['Base', 'User', 'Destination', 'Blog', 'BlogDestination']