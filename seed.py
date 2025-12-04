#!/usr/bin/env python3

from lib.models import Base, User, Destination, Blog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

# Database setup
engine = create_engine('sqlite:///safariconnect.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_database():
    """Seed the database with sample data"""
    
    print("Seeding SafariConnect database...")
    
    # Clear existing data
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    # Create users
    users = [
        User(username="safari_expert", email="expert@safariconnect.com"),
        User(username="conservationist", email="conserve@safariconnect.com"),
        User(username="travel_writer", email="writer@safariconnect.com"),
    ]
    
    session.add_all(users)
    session.commit()
    
    # Create destinations
    destinations = [
        Destination(
            name="Maasai Mara National Reserve",
            category="National Parks & Reserves",
            location="Narok County, Kenya",
            key_feature="Great Wildebeest Migration",
            conservation_status="Protected",
            established=1961,
            area="1,510 km²",
            description="The Maasai Mara National Reserve is East Africa's premier wildlife destination...",
            images=[
                "data/images/maasaimara-1.jpg",
                "data/images/maasaimara-2.jpg",
                "data/images/maasaimara-3.jpg",
                "data/images/maasaimara-4.jpg",
                "data/images/maasaimara-5.jpg"
            ],
            user=users[0]
        ),
        Destination(
            name="Samburu National Reserve",
            category="National Parks & Reserves",
            location="Samburu County, Kenya",
            key_feature="Endemic Species",
            conservation_status="Protected",
            established=1985,
            area="165 km²",
            description="Samburu National Reserve is home to unique species like the Grevy's zebra...",
            images=[
                "data/images/samburu-1.jpg",
                "data/images/samburu-2.jpg",
                "data/images/samburu-3.jpg"
            ],
            user=users[1]
        ),
    ]
    
    session.add_all(destinations)
    session.commit()
    
    # Create blogs
    blogs = [
        Blog(
            title="Endangered Species of Samburu: The Grevy's Zebra",
            category="Learn",
            content="The Grevy's zebra, native to Samburu National Reserve, is one of Kenya's most endangered mammals...",
            user=users[1]
        ),
        Blog(
            title="The Great Migration Explained",
            category="Conservation",
            content="The annual Great Wildebeest Migration is one of nature's most spectacular events...",
            user=users[0]
        ),
    ]
    
    # Link blogs to destinations (many-to-many)
    blogs[0].destinations.append(destinations[1])  # Grevy's zebra blog -> Samburu
    blogs[1].destinations.append(destinations[0])  # Migration blog -> Maasai Mara
    blogs[1].destinations.append(destinations[1])  # Migration blog -> also mentions Samburu
    
    session.add_all(blogs)
    session.commit()
    
    print("Database seeded")
    print(f"   Created: {len(users)} users, {len(destinations)} destinations, {len(blogs)} blogs")

if __name__ == "__main__":
    seed_database()