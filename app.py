from flask import Flask, render_template
from views import views  # Importing the 'views' blueprint from the 'views.py' module

app = Flask(__name__)  # Creating a Flask application instance

app.register_blueprint(views, url_prefix="/views")  # Registering the 'views' blueprint with a URL prefix '/views'

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Running the Flask application in debug mode on port 5000

