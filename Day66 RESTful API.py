import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     #Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("day66/index.html")


# HTTP GET - Read Record
# -----------to Get a single random cafe from database----------
@app.route("/random")
def random_cafe_data():
    random_no = random.randint(1, 21)
    result = db.session.execute(db.select(Cafe).where(Cafe.id == random_no)).scalar()
    # return jsonify(cafe = {"id": result.id,
    #     "name": result.name,
    #     "map_url": result.map_url,
    #     "img_url": result.img_url,
    #     "location": result.location,
    #     "seats": result.seats,
    #     "has_toilet": result.has_toilet,
    #     "has_wifi": result.has_wifi,
    #     "has_sockets": result.has_sockets,
    #     "can_take_calls": result.can_take_calls,
    #     "coffee_price": result.coffee_price,
    #     })
    #                       Or(if to_dict() defined)

    return jsonify(cafe=result.to_dict())


# --------- to Get all cafe from database as API response -----------------
@app.route("/all")
def all_cafe():
    all_cafe = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafe])


# --------- to Get a cafe from database using location parameter as API response -----------------


@app.route("/search")
def get_the_cafe():
    parameter = request.args.get("loc")  # Access the 'location' parameter
    the_cafe = db.session.execute(
        db.select(Cafe).where(Cafe.location == parameter)
    ).scalars()
    return jsonify(cafe=[cafe.to_dict() for cafe in the_cafe])


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_price(id):
    data = request.args.get("new_price")
    cafe_to_update = db.get_or_404(Cafe, id)
    cafe_to_update.coffee_price = data
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>", methods=["DELETE"])
def closed_cafe(id):
    key = request.args.get("api-key")
    if key == "TopSecretAPIKey":
        cafe_to_update = db.get_or_404(Cafe, id)
        db.session.delete(cafe_to_update)
        db.session.commit()
        return jsonify(response={"success": "Successfully removed the new cafe."})
    else:
        return jsonify(
            response={
                "error": "Sorry, that's not allowed. Make sure you have the correct api_key"
            }
        )


if __name__ == "__main__":
    app.run(debug=True)
