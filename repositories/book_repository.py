import sqlite3
from db.run_sql import run_sql
from models.authors import Author
from models.books import Book
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(author, row['title'], row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(author, result['title'], result['id'])
    return book


