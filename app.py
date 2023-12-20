import math
import pickle

import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="staticFiles")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.items()
    data = list(data)
    for key, value in data:
        print(f"{key}: {value}")
    return render_template("index.html", prediction_text=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
