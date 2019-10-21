from waitress import serve

import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from python.functions import  result_f1scr, result_table

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""

    restaurants = ["amelie_nyc", "lovemama_nyc", "upstate_nyc"]

    return render_template("index.html", restaurants=restaurants)

@app.route("/get_results", methods=["POST"])
def get_results():
    data = request.form
    print(data)

    restaurant_a = data["restaurant"]
    table = result_table(restaurant_a).to_html()
    f1 = result_f1scr(restaurant_a)

    return render_template('results.html', restaurant = restaurant_a, table=table, f1=f1)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)

