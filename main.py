import os
import sqlite3
import json
import sys
import re
from config import * 

from flask import Flask, render_template, jsonify, request
from flask import g

app = Flask(__name__, static_url_path='/static')

DATABASE = "osu.db"
reset_db = False
can_run_server = True
is_debug_mode = False

# Table schema
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
        for schema in SCHEMA_LIST:
            with app.open_resource(schema, mode='r') as f:
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
    return render_template("index.html", data=get_country_rankings_json_data('osu', 500),
                           **locals(),
                           **CONSTANT_OBJ
                           )

@app.route("/chart")
def chart():
    return render_template("chart.html")

@app.route("/<mode>/")
def table_pages(mode):
    return render_template(f"base_table.html",
                           data=get_country_rankings_json_data(mode, 500),
                           **locals(),
                           **CONSTANT_OBJ
                           )

# Bar chart
@app.route("/<mode>/<entry>")
def chart_pages(mode, entry, p_length = ""):
    length = request.args.get("length", p_length if p_length else "50")
    return render_template(f"base_chart.html", 
                           data=get_country_rankings_json_data(mode, 500),
                           **locals(),
                           **CONSTANT_OBJ
                           )


# Scatter chart
@app.route("/<mode>/scatter")
def scatter_pages(mode, p_x = "", p_y = "", p_length = ""):

    x = request.args.get("x", p_x if p_x else "play_count")
    y = request.args.get("y", p_y if p_y else "avg_performance")
    length = request.args.get("length", p_length if p_length else "100")

    print(f"x: {x}")
    print(f"y: {y}")
    print(f"Locals: {locals()}")

    return render_template(f"base_chart_scatter.html",
                           data=get_country_rankings_json_data(mode, 500),
                           **locals(),
                           **CONSTANT_OBJ
                           )
                           



@app.route("/api/country_rankings", methods = ["GET"])
def get_country_rankings_data(p_mode = "", p_length = ""):

    mode = request.args.get("mode", p_mode if p_mode else "osu")
    length = request.args.get("length", p_length if p_length else "50")

    print(f"Game mode: {mode}")
    print(f"Length : {length}")

    try:
        print(type(int(length)))
        length = int(length)
    except ValueError:
        return jsonify({"error": "Invalid length parameter"}), 400

    if mode in GAME_MODES:
        table_name = TABLES[mode]
    else:
        return jsonify({"error": "Invalid mode"}), 400

    db = get_db()
    cursor = db.cursor()
    data = cursor.execute(f"SELECT * FROM {table_name} AS r").fetchall()
    t_data = [i for i in zip(*data)]
    dict_data = {key: list(t_data[i])[:length] for i, key in enumerate(COUNTRY_RANKINGS_ENTRIES)}
    json_data = jsonify(dict_data)

    return (json_data, 200)

def get_country_rankings_json_data(p_mode = "", p_length = ""):
    res, status = get_country_rankings_data(p_mode, p_length)
    data = res.get_json()
    return data

# Filters
@app.template_filter('pascal_case')
def to_pascal_case(snake_str):
    return f"{' ' if len(snake_str.split('_')) > 1 else '' }".join(word.capitalize() for word in snake_str.split('_'))


@app.template_filter('pascal_to_spaces')
def pascal_to_spaces(pascal_str):
    # Use regular expression to add space before each capital letter, except the first one
    spaced_str = re.sub(r'(?<!^)(?=[A-Z])', ' ', pascal_str)
    return spaced_str


@app.template_filter('format_number')
def format_number_with_comma(number):
    return f"{number:,}"


if __name__  == "__main__":
    init()


    for arg in sys.argv:
        if arg == '--debug':
            is_debug_mode = True

    if(can_run_server):
        if(is_debug_mode):
            app.run(debug=True, port=8000)
        else:
            app.run(host='0.0.0.0',port=8000)
        


