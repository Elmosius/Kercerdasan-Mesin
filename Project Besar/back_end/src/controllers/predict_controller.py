from flask import Blueprint, request, jsonify
from services.predict_service import predict

predict_bp = Blueprint('predict_bp', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict_route():
    data = {
        'jumlah kamar tidur': [int(request.form.get('kamar_tidur'))],
        'jumlah kamar mandi': [int(request.form.get('kamar_mandi'))],
        'luas tanah (m2)': [float(request.form.get('luas_tanah'))],
        'luas bangunan (m2)': [float(request.form.get('luas_bangunan'))],
        'carport (mobil)': [int(request.form.get('carport'))],
        'pasokan listrik (watt)': [int(request.form.get('listrik'))],
        'Kabupaten/Kota': [request.form.get('kota')],
        'keamanan (ada/tidak)': [request.form.get('keamanan')],
        'taman (ada/tidak)': [request.form.get('taman')],
        'jarak dengan rumah sakit terdekat (km)': [float(request.form.get('jarak_rs'))],
        'jarak dengan sekolah terdekat (km)': [float(request.form.get('jarak_sekolah'))],
        'jarak dengan tol terdekat (km)': [float(request.form.get('jarak_tol'))]
    }

    prediction = predict(data)
    return jsonify({'prediction': prediction})
