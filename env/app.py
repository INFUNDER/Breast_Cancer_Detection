from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Breast Cancer')
def BreastCancer():
    return render_template('BreastCancer.html')

@app.route('/Covid')
def Covid19():
    return render_template('Covid19.html')


if __name__ == '__main__':
    app.run(debug=True)

