from flask import Blueprint, request, jsonify
from services.predict_service import predict

predict_bp = Blueprint('predict_bp', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    prediction = predict(data)
    return jsonify({'prediction': prediction})
