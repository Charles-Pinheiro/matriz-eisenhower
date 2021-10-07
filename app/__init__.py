from flask import Flask

from app.configs import env_configs, database, migration
from app.routes import category_blueprint, task_blueprint, get_blueprint


def create_app():

    app = Flask(__name__)
    env_configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)

    app.register_blueprint(category_blueprint.bp)
    app.register_blueprint(task_blueprint.bp)
    app.register_blueprint(get_blueprint.bp)

    return app
