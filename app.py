"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True


connect_db(app)
db.create_all()


@app.get('/')
def render_homepage():
    """Renders HTML for homepage used to query API.
    """

    return render_template("index.html")


@app.get('/api/cupcakes')
def get_all_cupcakes():
    """Returns json about all cupcakes.
       Responds with JSON like:
       {cupcakes: [{id, flavor, size, rating, image}, ...]}.
       The values should come from each cupcake instance.
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.get('/api/cupcakes/<int:cupcake_id>')
def get_single_cupcake(cupcake_id):
    """Get data about a single cupcake.
       Responds with JSON like:
       {cupcake: {id, flavor, size, rating, image}}.
       Should raise a 404 if the cupcake cannot be found.
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.post('/api/cupcakes')
def create_cupcake():
    """Create a cupcake with flavor, size,
       rating and image data from the body of the request.
       Respond with JSON like:
       {cupcake: {id, flavor, size, rating, image}}
    """

    flavor = request.json.get("flavor")
    size = request.json.get("size")
    rating = request.json.get("rating")
    image = request.json.get("image") or None

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.patch('/api/cupcakes/<int:cupcake_id>')
def update_cupcake(cupcake_id):
    """Updates a cupcake.
       The request body may include flavor, size, rating
       and image data but not all fields are required.
       This should raise a 404 if the cupcake cannot be found.
       Respond with JSON of the newly-updated cupcake:
       {cupcake: {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)

    db.session.commit()
    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized))


@app.delete('/api/cupcakes/<int:cupcake_id>')
def delete_cupcake(cupcake_id):
    """Delete cupcake with the id passed in the URL. 
       Respond with JSON like {deleted: [cupcake-id]}.
       This should raise a 404 if the cupcake cannot be found.
    """
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return (jsonify({"deleted": cupcake_id}))
