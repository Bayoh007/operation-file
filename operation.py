books = {}
members = []

GENRES = ("fiction", "non-fiction", "sci-fi", "romance", "fantasy")

def add_books(isbn, title, author, genre, total_copies):
    if isbn in books:
        print("Book already exists.")
        return False
    if genre.lower() not in GENRES:
        print("Invalid genre.")
        return False

    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre.lower(),
        "total_copies": total_copies
    }
    print(f"Book '{title}' added successfully.")
    return True


def add_member(member_id, name, email):
    for member in members:
        if member["member_id"] == member_id:
            print("Member already exists.")
            return False

    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    print(f"Member '{name}' added successfully.")
    return True



def search_books(query, by="title"):
    """Search for books by title or author."""
    results = []
    query = query.lower()

    for isbn, book in books.items():
        if by == "title" and query in book["title"].lower():
            results.append(book)
        elif by == "author" and query in book["author"].lower():
            results.append(book)

    if results:
        print("Search results:")
        for r in results:
            print(r)
    else:
        print(" No matching books found.")
    return results



def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        print("Book not found.")
        return False

    if genre and genre.lower() not in GENRES:
        print("Invalid genre.")
        return False

    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre.lower()
    if total_copies is not None:
        books[isbn]["total_copies"] = total_copies

    print(f"Book '{isbn}' updated successfully.")
    return True


def update_member(member_id, name=None, email=None):
    for member in members:
        if member["member_id"] == member_id:
            if name:
                member["name"] = name
            if email:
                member["email"] = email
            print(f"✅ Member '{member_id}' updated successfully.")
            return True
    print("Member not found.")
    return False


def delete_book(isbn):
    """Delete a book if it exists and has no borrowed copies."""
    if isbn in books:
        del books[isbn]
        print(f"✅ Book '{isbn}' deleted successfully.")
        return True
    print("Book not found.")
    return False


def delete_member(member_id):
    """Delete a member if they exist and have no borrowed books."""
    for member in members:
        if member["member_id"] == member_id:
            if member["borrowed_books"]:
                print("Cannot delete member; they have borrowed books.")
                return False
            members.remove(member)
            print(f"✅ Member '{member_id}' deleted successfully.")
            return True
    print("Member not found.")
    return False

def borrow_book(isbn, member_id):
    """Borrow a book if available and member has fewer than 3 borrowed books."""
    if isbn not in books:
        print("Book not found.")
        return False

    for member in members:
        if member["member_id"] == member_id:
            if len(member["borrowed_books"]) >= 3:
                print("Cannot borrow more than 3 books.")
                return False
            if books[isbn]["total_copies"] <= 0:
                print("Book unavailable.")
                return False

            books[isbn]["total_copies"] -= 1
            member["borrowed_books"].append(isbn)
            print(f"{member['name']} borrowed '{books[isbn]['title']}'.")
            return True

    print("Member not found.")
    return False


def return_book(isbn, member_id):
    """Return a borrowed book."""
    if isbn not in books:
        print("Book not found.")
        return False

    for member in members:
        if member["member_id"] == member_id:
            if isbn not in member["borrowed_books"]:
                print("This book was not borrowed by the member.")
                return False

            member["borrowed_books"].remove(isbn)
            books[isbn]["total_copies"] += 1
            print(f"{member['name']} returned '{books[isbn]['title']}'.")
            return True

    print("Member not found.")
    return False

def return_library_books():
    return books
