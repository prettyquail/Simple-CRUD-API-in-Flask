from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import Student

admin = Admin(app)
admin.add_view(ModelView(Student, db.session))

if __name__ == '__main__':
    app.run(debug=True)