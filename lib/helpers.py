import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Database setup
engine = create_engine('sqlite:///safariconnect.db')
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    """Initialize the database with all tables"""
    Base.metadata.create_all(engine)
    print("Database initialized")

def exit_program():
    """Exit the program"""
    print("Goodbye from SafariConnect")
    exit()

def add_sample_data():
    """Add sample data to the database"""
    from models import User, Destination, Blog
    
    
    # Create sample users
    user1 = User(username="safari_expert", email="expert@safariconnect.com")
    user2 = User(username="conservationist", email="conserve@safariconnect.com")
        
    session.add_all([user1, user2])
    session.commit()
        
    # Create sample destination
    destination1 = Destination(
        name="Maasai Mara National Reserve",
        category="National Parks & Reserves",
        location="Narok County, Kenya",
        key_feature="Great Wildebeest Migration",
        conservation_status="Protected",
        established=1961,
        area="1,510 km²",
        description="East Africa's premier wildlife destination...",
        images=[
            "data/images/maasaimara-1.jpg",
            "data/images/maasaimara-2.jpg",
            "data/images/maasaimara-3.jpg"
        ],
        user=user1
    )
        
    session.add(destination1)
    session.commit()
        
    # Create sample blog
    blog1 = Blog(
        title="Endangered Species of Samburu",
        category="Learn",
        content="The Grevy's zebra, native to Samburu...",
        user=user2
    )
        
    # Link blog to destination
    blog1.destinations.append(destination1)
        
    session.add(blog1)
    session.commit()
        
    print("Sample data added")

def list_users():
    """List all users"""
    from models import User
    users = session.query(User).all()
    
    if not users:
        print("No users found.")
        return
    
    print("\nUsers:")
    print("-" * 40)
    for user in users:
        print(f"ID: {user.id}")
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Destinations: {len(user.destinations)} | Blogs: {len(user.blogs)}")
        print("-" * 20)

def list_destinations():
    """List all destinations"""
    from models import Destination
    destinations = session.query(Destination).all()
    
    if not destinations:
        print("No destinations found.")
        return
    
    print("\nDestinations:")
    print("-" * 60)
    for dest in destinations:
        print(f"ID: {dest.id}")
        print(f"Name: {dest.name}")
        print(f"Location: {dest.location}")
        print(f"Category: {dest.category}")
        print(f"Images: {len(dest.images)}")
        print("-" * 30)

def list_blogs():
    """List all blogs"""
    from models import Blog
    blogs = session.query(Blog).all()
    
    if not blogs:
        print("No blogs found.")
        return
    
    print("\nBlogs:")
    print("-" * 60)
    for blog in blogs:
        print(f"ID: {blog.id}")
        print(f"Title: {blog.title}")
        print(f"Category: {blog.category}")
        print(f"Author: {blog.user.username if blog.user else 'Unknown'}")
        print(f"Destinations: {len(blog.destinations)}")
        print("-" * 30)

def create_user():
    """Create a new user"""
    from models import User
    
    print("\nCreate New User")
    print("-" * 30)
    
    username = input("Username: ")
    email = input("Email: ")
    
    if not username or not email:
        print("Username and email are required!")
        return
    
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print(f"Username '{username}' already exists")
        return
        
    existing_email = session.query(User).filter_by(email=email).first()
    if existing_email:
        print(f"Email '{email}' already exists")
        return
        
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
        
    print(f"\nUser created")
    print(f"   User ID: {user.id}")
    print(f"   Username: {user.username}")
    print(f"   Email: {user.email}")

def create_destination():
    """Create a new destination"""
    from models import Destination, User
    
    print("\nCreate New Destination")
    print("-" * 40)
    
    # List users simply
    users = session.query(User).all()
    if not users:
        print("No users found. Please create a user first!")
        return
    
    print("\nAvailable Users:")
    print("-" * 30)
    for user in users:
        print(f"ID: {user.id} | Username: {user.username}")
    
    # Get user selection
    user_id = int(input("\nEnter Uploader User ID: "))
    user = session.query(User).filter_by(id=user_id).first()
        
    if not user:
        print("User not found!")
        return
    
    # Get destination details
    name = input("\nDestination Name: ")
    category = input("Category: ")
    location = input("Location: ")
    
    # Optional fields
    key_feature = input("Key Feature (optional): ")
    conservation_status = input("Conservation Status (optional): ")
    established_input = input("Established Year (optional): ")
    area = input("Area (optional): ")
    description = input("Description (optional): ")
    
    # Get images
    images_input = input("Image URLs (comma-separated, optional): ")
    images = []
    if images_input:
        images = [url.strip() for url in images_input.split(',')]
    
    # Validate required fields
    if not name or not category or not location:
        print("Name, category, and location are required!")
        return
    
    established = None
    if established_input and established_input.isdigit():
        established = int(established_input)
        
    destination = Destination(
        name=name,
        category=category,
        location=location,
        key_feature=key_feature if key_feature else None,
        conservation_status=conservation_status if conservation_status else None,
        established=established,
        area=area if area else None,
        description=description if description else None,
        images=images,  # This is a Python list
        user=user
    )
        
    session.add(destination)
    session.commit()
        
    print(f"\nDestination created successfully!")
    print(f"   Destination ID: {destination.id} (auto-generated)")
    print(f"   Name: {destination.name}")
    print(f"   Images added: {len(images)}")
        
def create_blog():
    """Create a new blog"""
    from models import Blog, User, Destination
    
    print("\nCreate New Blog")
    print("-" * 40)
    
    # 1. LIST USERS
    users = session.query(User).all()
    if not users:
        print("No users found. Please create a user first!")
        return
    
    print("\nAvailable Users:")
    print("-" * 30)
    for user in users:
        print(f"ID: {user.id} | Username: {user.username}")
    
    # 2. GET USER SELECTION
    user_id = int(input("\nEnter User ID: "))
    user = session.query(User).filter_by(id=user_id).first()
        
    if not user:
        print("User not found!")
        return
    
    # 3. GET BLOG DETAILS
    title = input("\nBlog Title: ")
    category = input("Category: ")
    content = input("Content: ")
    
    if not title or not category or not content:
        print("Title, category, and content are required!")
        return
    
    # 4. LIST DESTINATIONS
    destinations = session.query(Destination).all()
    
    if destinations:
        print("\nAvailable Destinations:")
        print("-" * 50)
        for dest in destinations:
            print(f"ID: {dest.id} | Name: {dest.name} | Location: {dest.location}")
    
    # 5. GET DESTINATION SELECTION
    dest_ids_input = input("\nEnter Destination IDs to link or press Enter for none): ")
    
    # 6. CREATE BLOG 
    blog = Blog(
        title=title,
        category=category,
        content=content,
        user=user
    )
        
    # ADD TO SESSION FIRST
    session.add(blog)
    session.flush()  
        
    # 7. LINK DESTINATIONS IF PROVIDED
    if dest_ids_input.strip():
        for dest_id_str in dest_ids_input.split(','):
            dest_id_str = dest_id_str.strip()
            if dest_id_str: 
                dest_id = int(dest_id_str)
                destination = session.query(Destination).filter_by(id=dest_id).first()
                if destination:
                    blog.destinations.append(destination)
                    print(f"  Linked to destination: {destination.name}")
                else:
                    print(f"  Destination ID {dest_id} not found")

        
    # 8. COMMIT EVERYTHING
    session.commit()
    print(f"\nBlog created successfully!")
    print(f"   Blog ID: {blog.id} (auto-generated by database)")
    print(f"   Title: {blog.title}")
    print(f"   Destinations linked: {len(blog.destinations)}")
        
        
def search_destinations():
    """Search destinations by name or location"""
    from models import Destination
    
    search_term = input("\nEnter search term (name or location): ")
    
    if not search_term:
        print("Please enter a search term.")
        return
    
    destinations = session.query(Destination).filter(
        (Destination.name.ilike(f"%{search_term}%")) | 
        (Destination.location.ilike(f"%{search_term}%"))
    ).all()
    
    if not destinations:
        print(f"No destinations found for '{search_term}'")
        return
    
    print(f"\nSearch Results for '{search_term}':")
    print("-" * 60)
    for dest in destinations:
        print(f"ID: {dest.id}")
        print(f"Name: {dest.name}")
        print(f"Location: {dest.location}")
        print(f"Images: {len(dest.images)}")
        print("-" * 30)

def view_blog_destinations():
    """View all destinations linked to a blog"""
    from models import Blog
    
    list_blogs()
    
    blog_id = int(input("\nEnter Blog ID to view destinations: "))
    blog = session.query(Blog).filter_by(id=blog_id).first()
        
    if not blog:
        print("Blog not found!")
        return
        
    print(f"\nBlog: {blog.title}")
    print(f"Destinations mentioned:")
    print("-" * 40)
        
    if not blog.destinations:
        print("No destinations linked to this blog.")
    else:
        for dest in blog.destinations:
            print(f"{dest.name} ({dest.location})")
    

def view_destination_blogs():
    """View all blogs about a destination"""
    from models import Destination
    
    list_destinations()
    
    dest_id = int(input("\nEnter Destination ID to view blogs: "))
    destination = session.query(Destination).filter_by(id=dest_id).first()
        
    if not destination:
        print("Destination not found!")
        return
    
    print(f"\nDestination: {destination.name}")
    print(f"Blogs about this destination:")
    print("-" * 50)
        
    if not destination.blogs:
        print("No blogs about this destination.")
    else:
        for blog in destination.blogs:
            print(f"{blog.title} (by {blog.user.username})")

def clear_table(table_name):
    """Clear all data from a specific table"""
    from models import User, Destination, Blog
    if table_name.lower() == "users":
        count = session.query(User).count()
        session.query(User).delete()
        print(f"Cleared {count} users from database")
            
    elif table_name.lower() == "destinations":
        count = session.query(Destination).count()
        session.query(Destination).delete()
        print(f"Cleared {count} destinations from database")
            
    elif table_name.lower() == "blogs":
        count = session.query(Blog).count()
        session.query(Blog).delete()
        print(f"Cleared {count} blogs from database")
            
    else:
        print("Invalid table name. Use: users, destinations, or blogs")
        return
        
    session.commit()
        

def clear_all_data():
    """Clear ALL data from ALL tables"""
    from models import Blog, Destination, User
            
    # Delete blogs first (references destinations)
    blog_count = session.query(Blog).count()
    session.query(Blog).delete()
            
    # Delete destinations next (references users)
    dest_count = session.query(Destination).count()
    session.query(Destination).delete()
            
    # Delete users last
    user_count = session.query(User).count()
    session.query(User).delete()
            
    session.commit()
            
    print(f"Cleared all data:")
    print(f"   - {blog_count} blogs deleted")
    print(f"   - {dest_count} destinations deleted")
    print(f"   - {user_count} users deleted")
            
        

    