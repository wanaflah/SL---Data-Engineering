from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def home():
    return_string = "Hello World!"
    return return_string
