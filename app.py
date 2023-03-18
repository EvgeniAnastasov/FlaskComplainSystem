from decouple import config
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')  # TODO: get_config from env

db = SQLAlchemy(app)
from resources.auth import RegisterResource, LoginResource

api = Api(app)
migrate = Migrate(app, db)

api.add_resource(RegisterResource, "/register")
api.add_resource(LoginResource, "/login")

if __name__ == '__main__':
    app.run()
