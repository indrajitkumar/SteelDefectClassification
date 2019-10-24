from flask import Flask, jsonify, request
import numpy as np
import pickle as p
import os

app = Flask(__name__)
port = int(os.getenv("PORT", 9099))


@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"


@app.route('/add', methods=['GET'])
def add():
    return 5


@app.route('/api/', methods=['POST'])
def predictModel():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(results=prediction)


@app.route('/predict/', methods=['POST'])
def predict():
    # all kind of error checking go here
    data = request.get_json(force=True)
    # convert our json to numpy array

    predict_request = np.array(data)
    # np array goes into random forest and prediction comes out
    y_hat = model.predict(predict_request)
    # Return our prediction
    output = [y_hat[0]]
    return jsonify(results=output)


if __name__ == '__main__':
    # model = pickle.load(open("clf.pkl", "rb"))
    model = p.load(open("final_prediction.pickle", 'rb'))
    app.run(debug=True)
