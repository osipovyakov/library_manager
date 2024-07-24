from typing import List, Optional
from book_model import Book


#Создаем класс Librar в котором будут описаны методы работы с книгами
class Library:
    #Инициализируем экземпляр класса Library
    def __init__(self, filename: str = 'library.txt'):
        self.filename = filename
        self.books = self.load_books()

    #Загружаем книги из файла и переводим их в список объектов Book
    def load_books(self) -> List[Book]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return [Book.from_string(line.strip()) for line in f]
        except FileNotFoundError:
            return []

    #Метод для записи новых книг в файл
    def save_books(self) -> None:
        with open(self.filename, 'w', encoding='utf-8') as f:
            for book in self.books:
                f.write(book.to_string() + '\n')

    #Метод для добавления новых книг в библиотеку
    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.books.append(book)
        self.save_books()
        print(f'Книга {title} добавлена с ID {book.id}')

    #Метод для удаления книг из библиотеки по ID
    def remove_book(self, book_id: int) -> None:
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f'Книга с ID {book_id} удалена')
        else:
            print(f'Книга с ID {book_id} не найдена')

    #Метод поиска книг по ID
    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        return next((book for book in self.books if book.id == book_id), None)
    
    #Метод поиска книг по title/author/year
    def search_books(self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None) -> List[Book]:
        return [book for book in self.books if
                (title is None or title.lower() in book.title.lower()) and
                (author is None or author.lower() in book.author.lower()) and
                (year is None or year == book.year)]

    #Метод для отображения списка книг в библиотеке
    def display_books(self) -> None:
        if not self.books:
            print('Библиотека пуста')
        else:
            for book in self.books:
                print(f'ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}')

    #Метод для изменения статуса книги по ID
    def update_status(self, book_id: int, status: str) -> None:
        book = self.find_book_by_id(book_id)
        if book:
            if status in ['в наличии', 'выдана']:
                book.status = status
                self.save_books()
                print(f'Статус книги с ID {book_id} обновлен на {status}')
            else:
                print('Неверный статус. Используйте "в наличии" или "выдана"')
        else:
            print(f'Книга с ID {book_id} не найдена')

def main():
    library = Library()
    
    while True:
        print('\n1. Добавить книгу')
        print('2. Удалить книгу')
        print('3. Искать книгу')
        print('4. Отобразить все книги')
        print('5. Изменить статус книги')
        print('6. Выйти')

        choice = input('Выберите опцию: ')

        if choice == '1':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            year = int(input('Введите год издания книги: '))
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input('Введите ID книги для удаления: '))
            library.remove_book(book_id)
        elif choice == '3':
            search_by = input('Искать по (title/author/year): ').strip().lower()
            if search_by == 'title':
                title = input('Введите название книги: ')
                books = library.search_books(title=title)
            elif search_by == 'author':
                author = input('Введите автора книги: ')
                books = library.search_books(author=author)
            elif search_by == 'year':
                year = int(input('Введите год издания книги: '))
                books = library.search_books(year=year)
            else:
                print('Неверный критерий поиска.')
                continue

            if books:
                for book in books:
                    print(f'ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}')
            else:
                print('Книги не найдены')
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = int(input('Введите ID книги: '))
            status = input('Введите новый статус (в наличии/выдана): ').strip().lower()
            library.update_status(book_id, status)
        elif choice == '6':
            break
        else:
            print('Неверное значение. Пожалуйста, выберите снова')

if __name__ == '__main__':
    main()
