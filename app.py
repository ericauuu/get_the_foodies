from waitress import serve

import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from python.functions import  get_pos_neg_words_df, f1_ind, full_df, get_f1scr, show_aud

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""
    return render_template("index.html")

@app.route("/get_results", methods=["POST"])
def get_results():
    data = request.form
    print(data)
    # user_number = int(data["number"])
    # user_number_doubled = user_number * 2

    url = data["yelp_url"] 
    df = full_df(url)
    words = show_aud(df)
    table = words.to_html()
    f1 = get_f1scr(df)

    #show_plot(url)
    #f1_score = f1_ind(url)
    #text = force_text_ind(url)
    #force_plot = force_plot_ind(url)

    #return render_template("results.html", url=url, path='/static/images/shap_plot.png')
    return render_template('results.html', table=table, f1=f1)

#@app.route('/test')
# def show_plot(url):
    #draw=force_plot_ind(url)
    # plt.plot(draw)
    #draw.savefig('static/images/shap_plot1.png')
    # return render_template('results.html', name = 'review example', url ='static/images/shap_plot1.png')

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)

