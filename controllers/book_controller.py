from crypt import methods
from flask import Flask, render_template, Blueprint, request, redirect
from repositories import book_repository
from repositories import author_repository
from models.books import Book
from models.authors import Author

books_blueprint = Blueprint("books", __name__)

#index
@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)