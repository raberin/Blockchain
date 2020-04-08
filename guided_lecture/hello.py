from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, world!"


@app.route('/newpage')
def newpage():
    return "New Page!"


if __name__ == "__main__":
    app.run()
