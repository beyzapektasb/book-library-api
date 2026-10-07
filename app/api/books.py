from fastapi import APIRouter, HTTPException

from app.schemas.book import BookCreate, BookResponse
from app.services.book_service import add_book, edit_book, list_books, remove_book


router = APIRouter(prefix="/api/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def get_books():
    return list_books()


@router.post("/", response_model=BookResponse, status_code=201)
def create_book_endpoint(book: BookCreate):
    return add_book(book.title, book.author, book.isbn)


@router.put("/{book_id}", response_model=BookResponse)
def update_book_endpoint(book_id: int, book: BookCreate):
    updated_book = edit_book(book_id, book.title, book.author, book.isbn)

    if updated_book is None:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")

    return updated_book


@router.delete("/{book_id}")
def delete_book_endpoint(book_id: int):
    deleted = remove_book(book_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")

    return {"message": "Kitap silindi"}