from flask import Flask, render_template, request, url_for
import pickle
import pandas as pd
import numpy as np
import sklearn

app = Flask(__name__)
d_model = pickle.load(open("../deb_model.pkl", "rb"))
d_car = pd.read_csv("../diabetes.csv")
c_model = pickle.load(open("../covid_model.pkl", "rb"))
c_car = pd.read_csv("../COVID-19.csv")
b_model = pickle.load(open("../model.pkl", "rb"))
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
names = [
    "id",
    "clump_thickness",
    "uniform_cell_size",
    "uniform_cell_shape",
    "marginal_adhesion",
    "single_epithelial_size",
    "bare_nuclei",
    "bland_chromatin",
    "normal_nucleoli",
    "mitoses",
    "class",
]
b_car = pd.read_csv(url, names=names)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        Pregnancies = request.form["pregnancies"]
        glucose = request.form["glucose"]
        BP = request.form["blood_pressure"]
        Skin = request.form["skin_thickness"]
        Insulin = request.form["insulin"]
        bmi = request.form["bmi"]
        dpf = request.form["dpf"]
        Age = request.form["age"]

        prediction = d_model.predict(
            pd.DataFrame(
                [[Pregnancies, glucose, BP, Skin, Insulin, bmi, dpf, Age]],
                columns=[
                    "Pregnancies",
                    "Glucose",
                    "BloodPressure",
                    "SkinThickness",
                    "Insulin",
                    "BMI",
                    "DiabetesPedigreeFunction",
                    "Age",
                ],
            )
        )
        if prediction == 1:
            predict = "Positive"
        else:
            predict = "Negative"
        # Process the text_value (e.g., store in database, perform calculations)
        return render_template("index.html", predict=predict)
    else:
        return render_template("index.html")

@app.route("/BreastCancer", methods=["GET", "POST"])
def BreastCancer():
    if request.method == "POST":
        clump = request.form["ClumpThickness"]
        unisize = request.form["UniformCellSize"]
        unishape = request.form["UniformCellShape"]
        ma = request.form["MarginalAdhesion"]
        ses = request.form["SingleEpithelialSize"]
        bareN = request.form["BareNuclei"]
        BlandC = request.form["BlandChromatin"]
        normalN = request.form["BlandChromatin"]
        mitoses = request.form["mitoses"]

        b_prediction = b_model.predict(
            pd.DataFrame(
                [[clump, unisize, unishape, ma, ses, bareN, BlandC, normalN, mitoses]],
                columns=[
                    "clump_thickness",
                    "uniform_cell_size",
                    "uniform_cell_shape",
                    "marginal_adhesion",
                    "single_epithelial_size",
                    "bare_nuclei",
                    "bland_chromatin",
                    "normal_nucleoli",
                    "mitoses",
                ],
            )
        )
        # Process the text_value (e.g., store in database, perform calculations)
        if b_prediction == 1:
            predict = "Positive"
        else:
            predict = "Negative"
        return render_template("BreastCancer.html", predict=predict)
    else:
        return render_template("BreastCancer.html")


@app.route("/Covid", methods=["GET", "POST"])
def Covid19():
    if request.method == "POST":
        age = request.form["Age"]
        bodytemp = request.form["bodytemperature"]
        drycough = request.form["DryCough"]
        sourt = request.form["sourthroat"]
        weak = request.form["Weakness"]
        breath = request.form["breathingproblem"]
        drows = request.form["drowsiness"]
        painc = request.form["paininchest"]
        travel = request.form["travelhistorytoinfectedcountries"]
        stroke = request.form["strokeorreducedimmunity"]
        highbp = request.form["highbloodpressue"]
        change = request.form["changeinappetide"]
        losssmell = request.form["Lossofsenseofsmell"]

        c_prediction = c_model.predict(
            pd.DataFrame(
                [
                    [
                        age,
                        bodytemp,
                        drycough,
                        sourt,
                        weak,
                        breath,
                        drows,
                        painc,
                        travel,
                        stroke,
                        highbp,
                        change,
                        losssmell,
                    ]
                ],
                columns=[
                    "age",
                    "body temperature",
                    "Dry Cough",
                    "sour throat",
                    "weakness",
                    "breathing problem",
                    "drowsiness",
                    "pain in chest",
                    "travel history to infected countries",
                    "stroke or reduced immunity",
                    "high blood pressue",
                    "change in appetide",
                    "Loss of sense of smell",
                ],
            )
        )
        # Process the text_value (e.g., store in database, perform calculations)
        if c_prediction == 1:
            predict = "Positive"
        else:
            predict = "Negative"
        return render_template("Covid19.html", predict=predict)
    else:
        return render_template("Covid19.html")


if __name__ == "__main__":
    app.run(debug=True)
