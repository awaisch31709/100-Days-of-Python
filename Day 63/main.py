from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# STEP 1: Create the Flask app and tell it where the database file lives.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"


# STEP 2: Set up SQLAlchemy (the tool that lets us use Python instead of raw SQL).
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# STEP 3: Describe the "books" table as a Python class (one attribute = one column).
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# STEP 4: Create the table in the database file if it doesn't exist yet.
with app.app_context():
    db.create_all()


# READ: show every book stored in the database.
@app.route("/")
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template("index.html", books=all_books)


# CREATE: GET shows the form, POST saves the new book then goes home.
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=float(request.form["rating"]),
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


# UPDATE: the book id arrives in the URL (/edit?id=1).
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book = db.get_or_404(Book, book_id)
        book.rating = float(request.form["rating"])
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book)


# DELETE: find the book by id, remove it, go home.
@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
