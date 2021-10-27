from flask import Flask, render_template, url_for, request, redirect, session


import requests

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import wikipedia

from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import io


app = Flask(__name__)


def wikigen(string):
    bigstring = wikipedia.page(string).content

    plt.figure(figsize=(12,12))
    wordcloud = WordCloud(stopwords = STOPWORDS,
                          background_color='white',
                          #background_color='black',
                          #colormap = 'Reds',
                          collocations=False,
                          width =1200,
                          height =1000
                         ).generate(bigstring)
    plt.axis('off')
    return wordcloud
    
    
@app.route('/plot/<name>.png', methods=['GET', 'POST'])
def plot_png(name):
    fig = wikigen(name)
    output = fig.to_image()
    buf = io.BytesIO()
    output.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return Response(byte_im, mimetype='image/png')

   



@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')

@app.route("/projects")
def about():
    return render_template('projects.html', title='Projects')

@app.route("/wordcloud", methods=['GET', 'POST'])
def wordcloud():
    if request.method == "POST":
        title = request.form['title']
        return render_template('wordcloud.html', title=title)
        
    else:
        return render_template('wordcloud.html')


if __name__ == '__main__':
    app.run(debug=False)
