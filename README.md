📚 Library Management System (Python Project)
🧩 Overview
This project is a simple Library Management System implemented in Python using core programming concepts such as functions, dictionaries, lists, and tuples.
It allows an administrator to manage library operations like adding books, registering members, searching, borrowing, and returning books.
The goal is to simulate a real-world library workflow while practicing Object-Oriented Programming (OOP) and modular design principles.

🏗️ Project Structure
LibraryManagement/
│
├── demo.py           # Main program interface (Admin login and menu options)
├── operation.py   # Core logic for managing books and members
├── test.py           # Testing and validation of library functions
└── README.md         # Project documentation

🧠 Key Concepts Used
•	Dictionaries: To store book records (books dictionary)
•	Lists: To store member information (members list)
•	Tuples: To store valid genres (GENRES tuple)
•	Functions: For adding, updating, searching, borrowing, and returning books
•	Control Flow: For managing user input and program options

⚙️ Data Structures
Name	Type	Description
books	dict	Stores book info with ISBN as key
members	list	Holds all registered members
GENRES	tuple	Contains valid genres (fiction, non-fiction, etc.)

🧩 Functions Overview
Function	Description	Interacts With
add_books()	Adds new books with details like title, author, genre, and copies	books, GENRES
add_member()	Registers new members	members
search_book()	Searches books by title or author	books
borrow_book()	Allows members to borrow a book	books, members
return_book()	Handles book return and updates copies	books, members
update_books()	Updates book information	books
update_member()	Updates member details	members
delete_book()	Deletes a book from the library	books
delete_member()	Deletes a member record	members

🔑 Admin Login (demo.py)
Default admin credentials:
Username: admin
Password: edit
After logging in, the admin can:
1.	Add books or members
2.	Search, update, or delete records
3.	Borrow or return books
4.	View all books

🧪 Testing (test.py)
The test.py file includes sample test cases to verify the core functions of the system, such as:
•	Adding books/members
•	Preventing duplicate entries
•	Searching for books
•	Validating borrow and return logic

🧭 UML Diagram Summary
The UML diagram shows:
•	Data structures (books, members, GENRES)
•	Functions (e.g., add_books, borrow_book)
•	Relationships showing how functions interact with data structures

🚀 How to Run the Project
1.	Clone or download the repository.
2.	Open a terminal and navigate to the project directory.
3.	Run:
4.	python demo.py
5.	Enter the admin credentials and choose an operation.

✨ Future Improvements
•	Implement file-based or database storage
•	Add user authentication for members
•	Create a GUI version using Tkinter or web interface using Flask
•	Track due dates and late return penalties

👩‍💻 Author
Developed by Musa Bayoh
