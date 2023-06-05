from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def about_me():
    return render_template("contact.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio/portfolio.html")


@app.route("/tribute_page")
def tribute_page():
    return render_template("portfolio/tribute_page/index.html")


@app.route("/boogle")
def boogle():
    return render_template("portfolio/boogle/index.html")


@app.route("/hair_salon")
def hair_salon():
    return render_template("portfolio/hair_salon/index.html")


if __name__ == '__main__':
    app.run(use_reloader=True)
