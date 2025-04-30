# After learning SQLite we will add that to this website.

# ------------*******------------- Code Before adding database -----------------********------------------------------------

# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# all_books = []

# @app.route('/')
# def home():
#     return render_template('day63/index.html', books=all_books)


# @app.route("/add", methods=['GET','POST'])
# def add():
#     if request.method == 'POST':
#         all_books.append({"title": request.form.get('title'),
#                         "author": request.form.get('author'),
#                         "rating": request.form.get('rating')})
#         return redirect(url_for('home'))
#     else:
#         return render_template('day63/add.html')


# if __name__ == "__main__":
#     app.run(debug=True)

# ------------*******------------- Code After adding database -----------------********------------------------------------

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-collection.db'
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float,nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template('day63/index.html', books=all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        # Create record
        with app.app_context():
            new_book = Book(title=request.form.get('title'),
                            author=request.form.get('author'),
                            rating=request.form.get('rating'))
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('day63/add.html')
    
@app.route("/id",methods=['GET','POST'])
def edit_rating():
    if request.method == 'POST':
        id_to_change = request.form['id']
        book_to_update = db.get_or_404(Book, id_to_change)
        book_to_update.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    else:
        book_id = request.args.get('id')
        book_selected = db.get_or_404(Book, book_id)
        return render_template("day63/rating_edit.html", book=book_selected)
    
@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

