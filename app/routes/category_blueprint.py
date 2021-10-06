from flask import Blueprint
from app.controllers.categories_controller import get_all_categories, create_category, delete_category_by_id, update_category_by_id, delete_category_by_id

bp_category = Blueprint ('category', __name__)

bp_category.get('/')(get_all_categories)
bp_category.post('/category')(create_category)
bp_category.patch('/category/<int:category_id>')(update_category_by_id)
bp_category.delete('/category/<int:category_id>')(delete_category_by_id)