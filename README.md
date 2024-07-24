# Library Manager

Консольное приложение для управления библиотекой книг

## Функционал

1. **Добавление книги**: Пользователь вводит `title`, `author` и `year`, после чего книга добавляется в библиотеку с уникальным `id` и статусом "в наличии".
2. **Удаление книги**: Пользователь вводит `id` книги, которую нужно удалить.
3. **Поиск книги**: Пользователь может искать книги по `title`, `author` или `year`.
4. **Отображение всех книг**: Приложение выводит список всех книг с их `id`, `title`, `author`, `year` и `status`.
5. **Изменение статуса книги**: Пользователь вводит `id` книги и новый статус ("в наличии" или "выдана").

## Запуск приложения
Клонируем репозиторий с помощью команды:
```bash
git clone https://github.com/osipovyakov/library_manager.git
```
Для запуска из директории приложения выполните команду:
```bash
python library_manager.py
```
