import os
import sqlite3
import json
from config import * 

from flask import Flask, render_template, jsonify, request
from flask import g

# from flask_script import Manager

# print(f'Name: {__name__}')
# print(f"{GAME_MODES}")
# print(SCHEMAS)

app = Flask(__name__)
DATABASE = "osu.db"
reset_db = False
can_run_server = True

# table schema
prefix_path = "schema/"
table_name = "osu_country_rankings"

# Database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Enable foreign key check
        db.execute("PRAGMA foreign_keys = ON")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource(taiko_schema, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def remove_db():
    if os.path.isfile(DATABASE):
        os.remove(DATABASE) 

def init():
    if(reset_db):
        remove_db()
        init_db()

# Router
@app.route("/")
def index():
    res = get_country_rankings_data()
    data = res.get_json()
    print(data)
    return render_template("index.html", data=data)

@app.route("/chart")
def chart():
    return render_template("chart.html")

@app.route("/hello")
def hello_world():
    return render_template("hello.html")


@app.route("/api/country_rankings", methods = ["GET"])
def get_country_rankings_data():
    mode = request.args.get("mode", "osu") 
    print(f"Game mode: {mode}")

    if mode in GAME_MODES:
        table_name = TABLES[mode]
    else:
        return jsonify({"error": "Invalid mode"}), 400

    db = get_db()
    cursor = db.cursor()
    data = cursor.execute(f"SELECT * FROM {table_name} AS r").fetchall()
    t_data = [i for i in zip(*data)]
    dict_data = {key: list(t_data[i]) for i, key in enumerate(COUNTRY_RANKINGS_ENTRIES)}
    json_data = jsonify(dict_data)

    return json_data


if __name__  == "__main__":
    init()
    if(can_run_server):
        app.run(debug=True, port=8000)


# @app.template_filter('reverse')
# def reverse_filter(s):
#     return s[::-1]

