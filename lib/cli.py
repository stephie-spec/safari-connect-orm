from helpers import (
    exit_program,
    init_db,
    add_sample_data,
    list_users,
    list_destinations,
    list_blogs,
    create_user,
    create_destination,
    create_blog,
    search_destinations,
    view_blog_destinations,
    view_destination_blogs
)


def main():
    print("\n" + "=" * 50)
    print("Welcome to SafariConnect")
    print("=" * 50)
    
    # Initialize database if needed
    init_db()
    
    while True:
        menu()
        choice = input("\n> Enter your choice (0-10): ").strip()
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_users()
        elif choice == "2":
            list_destinations()
        elif choice == "3":
            list_blogs()
        elif choice == "4":
            create_user()
        elif choice == "5":
            create_destination()
        elif choice == "6":
            create_blog()
        elif choice == "7":
            search_destinations()
        elif choice == "8":
            view_blog_destinations()
        elif choice == "9":
            view_destination_blogs()
        elif choice == "10":
            add_sample_data()
        else:
            print("Invalid choice. Please try again.")


def menu():
    """Display the main menu"""
    print("\n" + "-" * 40)
    print("MAIN MENU")
    print("-" * 40)
    print("0. Exit SafariConnect")
    print("1. List all users")
    print("2. List all destinations")
    print("3. List all blogs")
    print("4. Create new user")
    print("5. Create new destination")
    print("6. Create new blog")
    print("7. Search destinations")
    print("8. View blog destinations")
    print("9. View destination blogs")
    print("10. Add sample data")
    print("-" * 40)


if __name__ == "__main__":
    main()