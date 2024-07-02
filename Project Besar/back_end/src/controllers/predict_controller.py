from flask import Blueprint, request, jsonify
from src.services.predict_service import predict

predict_bp = Blueprint('predict_bp', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict_route():
    try:
        data = {
            'jumlah kamar tidur': int(request.form.get('kamar_tidur', 0)),
            'jumlah kamar mandi': int(request.form.get('kamar_mandi', 0)),
            'luas tanah (m2)': float(request.form.get('luas_tanah', 0.0)),
            'luas bangunan (m2)': float(request.form.get('luas_bangunan', 0.0)),
            'carport (mobil)': int(request.form.get('carport', 0)),
            'pasokan listrik (watt)': int(request.form.get('listrik', 0)),
            'Kabupaten/Kota': request.form.get('kota', ''),
            'keamanan (ada/tidak)': request.form.get('keamanan', 'tidak'),
            'taman (ada/tidak)': request.form.get('taman', 'tidak'),
            'jarak dengan rumah sakit terdekat (km)': float(request.form.get('jarak_rs', 0.0)),
            'jarak dengan sekolah terdekat (km)': float(request.form.get('jarak_sekolah', 0.0)),
            'jarak dengan tol terdekat (km)': float(request.form.get('jarak_tol', 0.0))
        }

        print("Data yang diterima:", data)
        prediction = predict(data)
        return jsonify({'prediction': prediction})

    except ValueError as e:
        print("Error:", e)
        return jsonify({'error': 'Input tidak valid atau prediksi gagal'}), 400
