import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.file', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    predictions = model.predict(final_features)

    output = predictions[0][0].round(2)

    return render_template('index.html', prediction_text = 'Employee Salary Should be ₹. {}'. format(output))


if __name__ == '__main__':
    app.run(debug=True)