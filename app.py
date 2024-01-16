from flask import Flask, render_template
import json
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

app = Flask(__name__)

with open('data/data.json', 'r') as file:
    data = json.load(file)

db_url = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(db_url)

Base = declarative_base()

class Book(Base):
    """
    SQLAlchemy model representing a Book entity.

    Attributes:
    id (int): Primary key for the Book entity.
    title (str): Title of the book.
    author (str): Author of the book.
    publication_year (int): Year of publication.
    genre (str): Genre of the book.
    isbn (str): International Standard Book Number.
    rating (float): Rating of the book.
    """
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(255))
    publication_year = Column(Integer)
    genre = Column(String(255))
    isbn = Column(String(13))
    rating = Column(Float)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if session.query(Book).count() == 0:
    for book_data in data['Buecher']:
        book = Book(
            title=book_data['Titel'],
            author=book_data['Autor'],
            publication_year=int(book_data['Veroeffentlichungsjahr']),
            genre=book_data['Genre'],
            isbn=book_data['ISBN'],
            rating=float(book_data['Bewertung'])
        )
        session.add(book)

    session.commit()

@app.route('/')
def index():
    """
    Endpoint for rendering the index page with a list of distinct books.

    Returns:
    str: Rendered HTML template with book information.
    """
    books = session.query(Book).distinct(Book.title).all()

    for book in books:
        book.background_color = f"#{random.randint(0, 0xFFFFFF):06x}"

    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
