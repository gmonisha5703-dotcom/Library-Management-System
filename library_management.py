library = {}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    if book_id in library:
        print("Book already exists!")
    else:
        library[book_id] = {
            "title": title,
            "author": author,
            "available": True
        }
        print("Book added successfully!")

def view_books():
    if not library:
        print("No books available.")
    else:
        print("\nLibrary Books:")
        for book_id, details in library.items():
            status = "Available" if details["available"] else "Issued"
            print(
                book_id,
                details["title"],
                details["author"],
                status
            )

def issue_book():
    book_id = input("Enter Book ID to issue: ")

    if book_id in library:
        if library[book_id]["available"]:
            library[book_id]["available"] = False
            print("Book issued successfully!")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")

def return_book():
    book_id = input("Enter Book ID to return: ")

    if book_id in library:
        if not library[book_id]["available"]:
            library[book_id]["available"] = True
            print("Book returned successfully!")
        else:
            print("Book is already available.")
    else:
        print("Book not found.")

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")


