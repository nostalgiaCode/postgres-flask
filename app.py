from flask import Flask
from flask_restful import Api

from config import postgresql
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = postgresql
api = Api(app)

from resources.get_question import GetQuestion

api.add_resource(GetQuestion, '/')

if __name__ == "__main__":
    with app.app_context():
        from db import db
        db.init_app(app)
        db.create_all()
        app.run(host='0.0.0.0')