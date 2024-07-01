from flask import Flask
from flask_smorest import Api
from db import init_db
from resources import blp as PostBlueprint


app = Flask(__name__)  # Flask app 인스턴스를 생성합니다.
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:ozcoding@localhost/flask_board"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Flask Board API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

init_db(app)  # db.py의 init_db를 호출합니다.

api = Api(app)  # flask_smorest API 문서 생성기 인스턴스를 생성합니다.
api.register_blueprint(PostBlueprint)

if __name__ == "__main__":
    app.run(debug=True)
