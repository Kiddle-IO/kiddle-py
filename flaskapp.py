from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')

@app.route("/projects")
def about():
    return render_template('projects.html', title='Projects')

if __name__ == '__main__':
    app.run(debug=False)
