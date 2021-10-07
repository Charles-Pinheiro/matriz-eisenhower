from app.models.categories_model import Categories
from flask import current_app, request
from flask.json import jsonify
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError


def create_category():

    category_data = request.json

    try:
        category = Categories(**category_data)

        session = current_app.db.session

        session.add(category)
        session.commit()

        return jsonify(category), 201

    except IntegrityError:
        return {'msg': 'category already exists!'}, 409


def update_category(id: int):

    category_data = request.json

    Categories.query.filter_by(id=id).update(category_data)

    current_app.db.session.commit()

    category = Categories.query.get(id)

    if category == None:
        return {'msg': 'category not found!'}, 404

    return jsonify(category), 200


def delete_category(id: int):

    try:
        category = Categories.query.get(id)

        session = current_app.db.session

        session.delete(category)
        session.commit()

        return '', 204
    
    except UnmappedInstanceError:
        return {'msg': 'category not found!'}, 404
