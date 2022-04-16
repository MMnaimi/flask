from app import app
@app.route("/")
def index():
    return "the value of __name__ is ={}".format(__name__)
@app.route("/about")
def about():
    return("<h1 style='color:red'>About!!!!!</h1>")