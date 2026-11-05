from fastapi import FastAPI, HTTPException

import uvicorn
from schemas import *
from datetime import timezone, datetime


app = FastAPI()


books = [
    {
        "id": 1,
        "title": "1984",
        "theme": 1
    },
    {
        "id": 2,
        "title": "Neizche",
        "theme": 1
    }        
]


users = []



@app.get('/', summary='Главная ручка', tags='основые ручки')
def main():
    return "Hello World"




@app.get('/books', summary='Получить список книг', tags=['Книги'])
def get_books():
    return {"books": books}




@app.get('/books/{book_id}', summary='получить книгу', tags=['Книги'])
def get_book(book_id: int, theme: int):
    for book in books:
        if book['id'] == book_id and book['theme'] == theme:
            return book
        else:
            continue
    raise HTTPException(status_code=404, detail='Book not found')



@app.post('/create_books', tags=['Книги'])
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "theme": new_book.theme,
    })

    return {"success": True, "message": "Книга успешно добавлена"}



@app.post("/users/create", tags=['Пользователи'])
def authenticate_user(user: UserSchema):
    users.append(user)


    return {"success": True, "message": "Пользователь успешно добавлен", "time": datetime.now().strftime("%d.%m.%Y %H:%M:%S")}


@app.delete("/users/{user_id}", tags=['Пользователи'])
def delete_user(user_id: int):
    for user in users:
        if user['user_id'] == user_id:
            users.remove(user)
            return {"success": True, "message": "Пользователь успешно удален"}
    

@app.get("/users", tags=['Пользователи'])
def get_users():
    return {"users": users}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
