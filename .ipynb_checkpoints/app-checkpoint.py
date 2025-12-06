from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
linreg = pickle.load(open('linreg.pkl','rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    input = [float(x) for x in request.form.values()]

    input_array = np.array(input).reshape(1, -1)

    output = linreg.predict(input_array)[0]

    return render_template('home.html', prediction_test=output)
# def main():
#     print("Hello from higher-education-consulting-analytics!")


if __name__ == "__main__":
    app.run(debug=True)
