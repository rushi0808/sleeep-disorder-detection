from flask import Flask, redirect, render_template, request, send_from_directory

from sleep_disorder.pipeline.stage_05_prediction import UserPredictionPipeline

app = Flask(__name__)


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


@app.route("/")
def index():
    return redirect("/home")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/detect", methods=["GET", "POST"])
def detect():
    if request.method == "POST":
        user_input = request.form.items()
        user_prediction_pipe = UserPredictionPipeline()
        user_prediction = user_prediction_pipe.main(user_input=list(user_input))
        return render_template("detect.html", user_prediction=user_prediction)
    elif request.method == "GET":
        return render_template("detect.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
