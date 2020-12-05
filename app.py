from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dnhs")
def dnhs():
    return render_template("dnhs.html")

@app.route("/videos")
def videos():
    return render_template("ytvids.html")


if __name__ == "__main__":
    app.run(debug=True)