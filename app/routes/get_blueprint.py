from flask import Blueprint
from app.controllers.get_controller import get_all

bp = Blueprint('get_bp', __name__)

bp.get('/')(get_all)
