from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD (only if the book isn't already in the table)
with app.app_context():
    existing = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    if existing is None:
        new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()
        print("Book added.")
    else:
        print("Harry Potter is already in the database, skipping insert.")
