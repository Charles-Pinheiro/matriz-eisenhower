from app.models.categories_model import Categories
from app.models.tasks_model import Tasks
from flask import current_app, request
from flask.json import jsonify
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError


def create_task():

    task_data = request.json

    session = current_app.db.session

    importance_urgency = {(1, 1): 1, (1, 2): 2, (2, 1): 3, (2, 2): 4}

    try:        
        task_data['eisenhower_id'] = importance_urgency[(task_data['importance'], task_data['urgency'])]

    except KeyError:
        return {
            'error': {
                'valid_options': {
                    'importance': [1, 2],
                    'urgency': [1, 2]
                },
                'recieved_options': {
                    'importance': task_data['importance'],
                    'urgency': task_data['urgency']
                }
            }
        }

    categories = task_data.pop('categories')

    try:
        task = Tasks(**task_data)

        for category in categories:
            db_category = Categories.query.filter_by(name=category['name']).first()

            if not db_category:
                db_category = Categories(**category)
                session.add(db_category)
                session.commit()

            task.categories.append(db_category)

        session.add(task)
        session.commit()

    except IntegrityError:
        return {'msg': 'Task already exists!'}, 409

    return jsonify(task.serialize(categories)), 201


def update_task(id: int):

    task_data = request.json

    task = Tasks.query.get(id)
    
    if not task:
        return {'msg': 'task not found!'}, 404

    importance_urgency = {(1, 1): 1, (1, 2): 2, (2, 1): 3, (2, 2): 4}

    if task_data.get('importance') or task_data.get('urgency'):
        if not task_data.get('importance'):
            task_data['importance'] = task.importance

        if not task_data.get('urgency'):
            task_data['urgency'] = task.urgency

        task_data['eisenhower_id'] = importance_urgency[(task_data['importance'], task_data['urgency'])]
    
    Tasks.query.filter_by(id=id).update(task_data)

    current_app.db.session.commit()

    task = Tasks.query.get(id)

    return jsonify(task), 200


def delete_task(id: int):

    try:
        task = Tasks.query.get(id)

        session = current_app.db.session

        session.delete(task)
        session.commit()

        return '', 204
    except UnmappedInstanceError:
        return {'msg': 'task not found!'}, 404
