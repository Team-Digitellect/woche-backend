from flask import Flask
from config import setup_db,db
from api import api as API
from user import user as USER

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.debug = True
    setup_db(app)
    #CORS(app)
    # Initialize Flask extensions here
    app.register_blueprint(API, url_prefix='/api')
    app.register_blueprint(USER, url_prefix='/auth/')
       
       
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app