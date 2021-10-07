from app.controllers.categories_controller import (create_category,
                                                   delete_category,
                                                   update_category)
from flask import Blueprint

bp = Blueprint('category_bp', __name__, url_prefix='/category')

bp.post('')(create_category)
bp.patch('<int:id>')(update_category)
bp.delete('<int:id>')(delete_category)
