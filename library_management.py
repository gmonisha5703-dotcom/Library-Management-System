books = {}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    books[book_id] = {
        "Title": title,
        "Author": author,
        "Status": "Available"
    }

    print("Book Added Successfully!")

def view_books():
    if not books:
        print("No Books Available")
    else:
        for book_id, details in books.items():
            print(book_id, details)

def issue_book():
    book_id = input("Enter Book ID to Issue: ")

    if book_id in books:
        if books[book_id]["Status"] == "Available":
            books[book_id]["Status"] = "Issued"
            print("Book Issued Successfully!")
        else:
            print("Book Already Issued")
    else:
        print("Book Not Found")

def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            print("Thank You!")
            break
        else:
            print("Invalid Choice")

main()
