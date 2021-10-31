from flask import Flask, render_template, request, session, Response

import modules.time_log as time_log

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import wikipedia

import io

app = Flask(__name__)

app.secret_key = open("secret_key.txt", "r").read()

#Returns wiki page either as a string or a disambiguation list
def wikitxt(string):
    try:
        bigstring = wikipedia.page(string).content
        return bigstring
    except Exception as e: return str(e).split("\n")[1:-2]
        
#Generates cloud image
def wikigen(string, bg='white', cmap='viridis'):
        bigstring = wikipedia.page(string).content
        stopwords_session = STOPWORDS
        stopwords_session.update(['b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        plt.figure(figsize=(12,12))
        wordcloud = WordCloud(stopwords = stopwords_session,
                              background_color=bg,
                              colormap = cmap,
                              collocations=False,
                              width =1200,
                              height =1000
                             ).generate(bigstring)
        plt.axis('off')
        return wordcloud



@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/log/530AE6")
def log():
    return time_log.run()


@app.route("/projects")
def about():
    return render_template('projects.html', title='Projects')

@app.route("/wordcloud", methods=['GET', 'POST'])
def wordcloud():
    if request.method == "POST":
        title = request.form['title']
        try:
            newtitle = request.form['ambig']
        except Exception:
            newtitle = False
        print(newtitle)
        session['bg'] = request.form['bg']
        session['cmap']  = request.form['cmap']
        if isinstance(wikitxt(title), list):
          txt = wikitxt(title)
        if newtitle:
            return render_template('wordcloud.html', title=newtitle, bg=session['bg'], cmap=session['cmap'], wikivalid=True)
        elif isinstance(wikitxt(title), str):
            return render_template('wordcloud.html', title=title, bg=session['bg'], cmap=session['cmap'], wikivalid=True)
        elif isinstance(wikitxt(title), list):
            if wikitxt(title) == []:
              return render_template('wordcloud.html', title=title, bg=session['bg'], cmap=session['cmap'], error=True)
            else:
              return render_template('wordcloud.html', title=title, bg=session['bg'], cmap=session['cmap'], ambig=txt)               
    else:
        return render_template('wordcloud.html')


@app.route('/generatecloud/<name>.png', methods=['GET', 'POST'])
def plot_png(name):
    fig = wikigen(name, session['bg'], session['cmap'])
    output = fig.to_image()
    buf = io.BytesIO()
    output.save(buf, format='PNG')
    byte_im = buf.getvalue()
    plt.close('all')
    return Response(byte_im, mimetype='image/png')
    
    
if __name__ == '__main__':
    app.run(debug=False)
