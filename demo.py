from operation import *

admin_username = 'admin'
admin_password = 'edit'
attempt = 3

while attempt > 0:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username == admin_username and password == admin_password:
        print('\nLogin Successful')
        while True:
            print('\nChoose an option:')
            print('1. ADD BOOK')
            print('2. ADD MEMBER')
            print('3. SEARCH BOOK')
            print('4. UPDATE BOOK')
            print('5. UPDATE MEMBER')
            print('6. DELETE BOOK')
            print('7. DELETE MEMBER')
            print('8. BORROW BOOK')
            print('9. RETURN BOOK')
            print('10. VIEW ALL BOOKS')
            print('11. EXIT')

            choose_option = int(input('Enter option: '))

            if choose_option == 1:
                isbn = input('ISBN: ')
                title = input('Title: ')
                author = input('Author: ')
                genre = input('Genre: ')
                total_copies = int(input('Total copies: '))
                add_books(isbn, title, author, genre, total_copies)



            elif choose_option == 2:
                member_id = input('Member ID: ')
                name = input('Name: ')
                email = input('Email: ')
                add_member(member_id, name, email)

            elif choose_option == 3:
                query = input('Search by title or author: ')
                by = input('Search by (title/author): ')
                search_books(query, by)

            elif choose_option == 4:
                isbn = input('ISBN: ')
                title = input('New Title (optional): ') or None
                author = input('New Author (optional): ') or None
                genre = input('New Genre (optional): ') or None
                copies = input('New Copies (optional): ')
                copies = int(copies) if copies else None
                update_book(isbn, title, author, genre, copies)

            elif choose_option == 5:
                mid = input('Member ID: ')
                name = input('New Name (optional): ') or None
                email = input('New Email (optional): ') or None
                update_member(mid, name, email)

            elif choose_option == 6:
                isbn = input('ISBN to delete: ')
                delete_book(isbn)

            elif choose_option == 7:
                mid = input('Member ID to delete: ')
                delete_member(mid)

            elif choose_option == 8:
                isbn = input('ISBN to borrow: ')
                mid = input('Member ID: ')
                borrow_book(isbn, mid)

            elif choose_option == 9:
                isbn = input('ISBN to return: ')
                mid = input('Member ID: ')
                return_book(isbn, mid)

            elif choose_option == 10:
                print("\nLibrary Books:")
                for k, v in books.items():
                    print(f"{k}: {v}")

            elif choose_option == 11:
                print("Goodbye!")
                exit()

            else:
                print("Invalid option. Try again.")


    else:
        attempt -= 1
        print(f'Wrong password. {attempt} attempt(s) left.')
