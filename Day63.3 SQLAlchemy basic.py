from flask import Flask
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float

# Initialize the extension
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Create the app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"   # Remember '///' slashes.

# Initialize the app
db.init_app(app)

# Define the MOdel
class User(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email:Mapped[str]
    
# Create the tables
with app.app_context():
    db.create_all()