import os
from flask import Flask, request, json
from model import Classifiers

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_iris():

    s_length = request.get_json(force=True)
    s_width = request.get_json(force=True)
    p_length = request.get_json(force=True)
    p_width = request.get_json(force=True)

    prediction, accuracy = Classifiers.Random_Forest([[s_length['s_length'], s_width['s_width'], p_length['p_length'], p_width['p_width']]])
    if prediction == [0]:
       iris_setosa = 'Iris Setosa'
       return json.dumps(iris_setosa)
    if prediction == [1]:
       iris_virginica = 'Iris Virginica'
       return json.dumps(iris_virginica)
    else:
       iris_versicolor = 'Iris Versicolor'
       return json.dumps(iris_versicolor)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)