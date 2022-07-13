import pdb
from models.authors import Author
from models.books import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author1 = Author("J.R.R. Tolkien")
author_repository.save(author1)

book1 = Book(author1, "The Hobbit")
book_repository.save(book1)

