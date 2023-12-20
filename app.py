import math
import pickle

import numpy as np
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="staticFiles")
model = pickle.load(open(r"./model/model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    int_features = [[int(x) for x in request.form.values()]]
    final_features = np.array(int_features)
    prediction = model.predict(final_features)
    print(final_features)
    print(prediction)
    if prediction == 0:
        return render_template(
            "index.html",
            prediction_text="You have no sleep disorder!".format(prediction),
        )
    elif prediction == 1:
        return render_template(
            "index.html",
            prediction_text="You have sleep Apnea Please Visit a doctor!".format(prediction),
        )
    else:
        return render_template(
            "index.html",
            prediction_text="You have Insomnia Please Visit a doctor!".format(prediction),
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
