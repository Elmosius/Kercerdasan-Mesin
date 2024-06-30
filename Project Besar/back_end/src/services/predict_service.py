import pickle
import os
import pandas as pd

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '../models/model.pkl')
    with open(model_path, 'rb') as file:
        model_data = pickle.load(file)

    if isinstance(model_data, tuple) and len(model_data) == 3:
        model, scaler, pca = model_data
    else:
        raise ValueError("File pickle tidak berisi format yang diharapkan (model, scaler, pca).")
    
    return model, scaler, pca

def preprocess_data(data, scaler, pca):
    input_df = pd.DataFrame([data])

    # Map categorical values to numerical
    input_df['keamanan (ada/tidak)'] = input_df['keamanan (ada/tidak)'].map({'ada': 1, 'tidak': 0})
    input_df['taman (ada/tidak)'] = input_df['taman (ada/tidak)'].map({'ada': 1, 'tidak': 0})
    input_df['lokasi'] = input_df['Kabupaten/Kota'].map({'Jakarta Pusat': 0, 'Jakarta Barat': 1, 'Jakarta Selatan': 2, 'Jakarta Timur': 3})  # Tambahkan semua kemungkinan lokasi
    input_df = input_df.drop(columns=['Kabupaten/Kota'])

    input_scaled = scaler.transform(input_df)
    input_reduced = pca.transform(input_scaled)

    return input_reduced

def predict(data):
    model, scaler, pca = load_model()
    preprocessed_data = preprocess_data(data, scaler, pca)
    prediction = model.predict(preprocessed_data)
    return round(prediction[0])
