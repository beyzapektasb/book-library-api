from app.database.connection import get_connection


def create_books_table():
    connection = get_connection()

    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT NOT NULL UNIQUE
            )
            """
        )
        connection.commit()
    finally:
        connection.close()


def get_all_books():
    connection = get_connection()

    try:
        rows = connection.execute(
            "SELECT id, title, author, isbn FROM books ORDER BY id"
        ).fetchall()

        return [dict(row) for row in rows]
    finally:
        connection.close()


def create_book(title: str, author: str, isbn: str):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)",
            (title, author, isbn),
        )

        connection.commit()

        return {
            "id": cursor.lastrowid,
            "title": title,
            "author": author,
            "isbn": isbn,
        }
    finally:
        connection.close()


def update_book(book_id: int, title: str, author: str, isbn: str):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            UPDATE books
            SET title = ?, author = ?, isbn = ?
            WHERE id = ?
            """,
            (title, author, isbn, book_id),
        )

        connection.commit()

        if cursor.rowcount == 0:
            return None

        row = connection.execute(
            "SELECT id, title, author, isbn FROM books WHERE id = ?",
            (book_id,),
        ).fetchone()

        return dict(row)
    finally:
        connection.close()


def delete_book(book_id: int):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "DELETE FROM books WHERE id = ?",
            (book_id,),
        )

        connection.commit()

        return cursor.rowcount > 0
    finally:
        connection.close()