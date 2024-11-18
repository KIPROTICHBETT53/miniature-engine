from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from database.db_setup import db
from routes.blog_routes import blog_blueprint

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

# Initialize Extensions
db.init_app(app)

# Register Blueprints
app.register_blueprint(blog_blueprint)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensures database tables are created
    app.run(debug=True)
