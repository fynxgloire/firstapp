from flask import Flask

app = Flask(__name__)

'''This is a decorator, this line of coe means this function
will be called whenever a user visits the main root page of the
web application
'''


@app.route("/")
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(port=5001, debug=True)
