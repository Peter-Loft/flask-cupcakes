"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy, Model

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"


def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """ Cupcake Model """

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, default=DEFAULT_IMAGE, nullable=False)

    def serialize(self):
        """Serialize to dictionary"""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }
