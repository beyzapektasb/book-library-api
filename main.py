from fastapi import FastAPI
from app.api.books import router as books_router
from app.repositories.book_repository import create_books_table


app = FastAPI(title="Kitap Kütüphanesi API")

create_books_table()
app.include_router(books_router)


@app.get("/")
def ana_sayfa():
    return {"mesaj": "Kitap Kütüphanesi API çalışıyor"}