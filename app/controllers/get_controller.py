from flask.json import jsonify
from app.models.categories_model import Categories
from app.configs.database import db


def get_all():

    categories = db.session.query(Categories).all()

    categories_return = []
    for category in categories:
        categories_return.append(category.serialize())

    return jsonify(categories_return), 200
