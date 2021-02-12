from flask import Flask, jsonify
from db import DB

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=['GET'])
def home():
    return_string = "Hello World!"
    return return_string

@app.route("/data", methods=['GET'])
def send_snippet():
    path = r"D:\Learning\SL---Data-Engineering\data\lending_club.db"
    dbx = DB()

    conn = dbx.connect(path)
    data = dbx.select_top(conn)

    return jsonify(data)

app.run()
