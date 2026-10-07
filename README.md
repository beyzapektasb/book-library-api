# Book Library API

A simple RESTful API for managing books, built with FastAPI and SQLite using a layered architecture.

## Features

- Create a new book
- List all books
- Update an existing book
- Delete a book
- SQLite database integration
- Request and response validation with Pydantic
- Interactive API documentation with Swagger UI

## Tech Stack

- Python
- FastAPI
- SQLite
- SQL
- Pydantic
- Uvicorn

## Architecture

The project follows a layered architecture:

API → Service → Repository → Database

- **API:** Handles HTTP requests and responses.
- **Service:** Connects the API layer with the repository layer.
- **Repository:** Handles database operations using SQL.
- **Database:** Manages the SQLite database connection.
- **Schemas:** Defines request and response models using Pydantic.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/` | List all books |
| POST | `/api/books/` | Create a new book |
| PUT | `/api/books/{book_id}` | Update a book |
| DELETE | `/api/books/{book_id}` | Delete a book |

## Installation

Clone the repository:

```bash
git clone https://github.com/beyzapektasb/book-library-api.git
cd book-library-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the development server:

```bash
fastapi dev main.py
```

The API will be available at:

`http://127.0.0.1:8000`

## API Documentation

After starting the application, Swagger UI is available at:

`http://127.0.0.1:8000/docs`