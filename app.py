from flask import Flask
from main import home

app = Flask(__name__)

app.add_url_rule('/', 'home', home, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
