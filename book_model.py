import os
from typing import Optional


#Описываем модель Book с необходимыми полями
class Book:
    def __init__(self, title: str, author: str, year: int, book_id: Optional[int] = None, status: str = 'в наличии'):
        self.id = book_id if book_id else self.generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    #Используем генератор случайных байтов для создания id книги
    @staticmethod
    def generate_id() -> int:
        return int.from_bytes(os.urandom(4), 'little')

    #Метод преобразования объекта Book в строковое представление
    def to_string(self) -> str:
        return f'{self.id},{self.title},{self.author},{self.year},{self.status}'

    #Метод преобразования строкового представления в объект класса Book
    @staticmethod
    def from_string(data: str) -> 'Book':
        book_id, title, author, year, status = data.split(',')
        return Book(title, author, int(year), int(book_id), status)
