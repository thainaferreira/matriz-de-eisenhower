from flask import Flask

def init_app(app: Flask):
    
    from app.routes.category_blueprint import bp_category
    from app.routes.tasks_blueprint import bp_task

    app.register_blueprint(bp_category)
    app.register_blueprint(bp_task)