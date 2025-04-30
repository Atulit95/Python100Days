from turtle import title
from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    # Query the database for all the posts. Convert the data to a python list.
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("day67/index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, index)
    return render_template("day67/post.html", post=requested_post)


# Form creation
class NewBlogForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    name = StringField(label="Your Name", validators=[DataRequired()])
    image_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = NewBlogForm()
    if form.validate_on_submit():
        new_blog = BlogPost(
            title=request.form.get("title"),
            date=date.today().strftime("%B %d, %Y"),
            body=request.form.get("body"),
            author=request.form.get("name"),
            img_url=request.form.get("image_url"),
            subtitle=request.form.get("subtitle"),
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("day67/make-post.html", form=form)


@app.route('/edit-post/<post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    blog_to_edit = db.get_or_404(BlogPost, post_id)
    edit_form=NewBlogForm(title=blog_to_edit.title,
                     subtitle = blog_to_edit.subtitle,
                     name = blog_to_edit.author,
                     image_url = blog_to_edit.img_url,
                     body = blog_to_edit.body)
    if edit_form.validate_on_submit():
        blog_to_edit.title = edit_form.title.data
        blog_to_edit.subtitle = edit_form.subtitle.data
        blog_to_edit.img_url = edit_form.image_url.data
        blog_to_edit.author = edit_form.name.data
        blog_to_edit.body = edit_form.body.data  
        db.session.commit()
        return redirect(url_for('show_post', index=post_id))
    return render_template("day67/make-post.html", edit=True, form=edit_form)

@app.route('/delete/<post_id>', methods=["GET"])
def delete_post(post_id):
    blog_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(blog_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("day67/about.html")


@app.route("/contact")
def contact():
    return render_template("day67/contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
