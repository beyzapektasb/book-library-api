from app.repositories.book_repository import create_book, delete_book, get_all_books, update_book


def list_books():
    return get_all_books()


def add_book(title: str, author: str, isbn: str):
    return create_book(title, author, isbn)


def edit_book(book_id: int, title: str, author: str, isbn: str):
    return update_book(book_id, title, author, isbn)


def remove_book(book_id: int):
    return delete_book(book_id)