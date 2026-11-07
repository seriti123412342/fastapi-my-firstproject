from fastapi import FastAPI, HTTPException, APIRouter, Depends
from models import *
import uvicorn
from schemas import *
from datetime import timezone, datetime
from db import setup_database, SessionDep
router = APIRouter()
from sqlalchemy import select
from typing import List

books = []

users = []

@router.get('/books', summary='Получить список книг', tags=['Книги'], response_model=List[BookSchema])
async def get_books(session: SessionDep):

    query = select(BookModel)
    result = await session.execute(query)

    books = result.scalars().all()

    return books



@router.get('/books/{book_id}', summary='получить книгу', tags=['Книги'])
def get_book(book_id: int, theme: int):
    for book in books:
        if book['id'] == book_id and book['theme'] == theme:
            return book
        else:
            continue
    raise HTTPException(status_code=404, detail='Book not found')




@router.post('/create_books', tags=['Книги'])
async def create_book(data: BookAddSchema, session: SessionDep):
    new_book = BookModel(
        title=data.title,
        theme=data.theme,
        author=data.author
    )

    session.add(new_book)
    await session.commit()

    return {"success": True, "message": "Книга успешно добавлена"}



@router.post("/users/create", tags=['Пользователи'])
def authenticate_user(user: UserSchema):
    users.append(user)


    return {"success": True, "message": "Пользователь успешно добавлен", "time": datetime.now().strftime("%d.%m.%Y %H:%M:%S")}



    

@router.get("/users", tags=['Пользователи'])
def get_users():
    return {"users": users}
