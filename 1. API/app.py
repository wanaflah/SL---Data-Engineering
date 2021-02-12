from flask import Flask, jsonify, request
from db import DB

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=['GET'])
def home():
    return_string = "Hello World!"
    return return_string


@app.route("/data", methods=['GET'])
def send_all():
    path = r"D:\Learning\SL---Data-Engineering\data\lending_club.db"
    dbx = DB()
    conn = dbx.connect(path)
    data = dbx.select_top(conn)
    return jsonify(data)


@app.route("/data/api", methods=['GET'])
def send_specific():
    if 'id' in request.args:
        id = int(request.args['id'])
        return str(id)
    else:
        return "Error: No id field provided. Please specify an id."


app.run()
