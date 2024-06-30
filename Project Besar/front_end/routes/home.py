from flask import Blueprint, render_template, request, redirect, url_for
import requests

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home/index.html')

@home.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    response = requests.post('http://localhost:5000/predict', data=data)
    prediction = response.json().get('prediction')

    return render_template('home/hasil.html', prediction=prediction)
