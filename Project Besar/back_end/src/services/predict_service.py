import pickle
import os
import pandas as pd
import xgboost as xgb

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '../models/model.pkl')
    with open(model_path, 'rb') as file:
        model_data = pickle.load(file)

    if isinstance(model_data, tuple) and len(model_data) == 4:
        model, scaler, pca, original_columns = model_data
    else:
        raise ValueError("File pickle tidak berisi format yang diharapkan (model, scaler, pca, original_columns).")
    
    return model, scaler, pca, original_columns

def preprocess_data(data, scaler, pca, original_columns):
    input_df = pd.DataFrame([data])
    print("Input DataFrame sebelum encoding:\n", input_df)  # Debugging output

    # Map categorical values to numerical
    input_df['keamanan (ada/tidak)'] = input_df['keamanan (ada/tidak)'].map({'ada': 1, 'tidak': 0})
    input_df['taman (ada/tidak)'] = input_df['taman (ada/tidak)'].map({'ada': 1, 'tidak': 0})
    input_df['lokasi'] = pd.Categorical(input_df['Kabupaten/Kota'], categories=['Jakarta Pusat', 'Jakarta Barat', 'Jakarta Selatan', 'Jakarta Timur', 'Jakarta Utara'])
    input_df = input_df.drop(columns=['Kabupaten/Kota'])

    print("Input DataFrame setelah mapping:\n", input_df)  # Debugging output

    # Encoding categorical features
    input_df = pd.get_dummies(input_df, columns=['keamanan (ada/tidak)', 'taman (ada/tidak)', 'lokasi'], drop_first=True)
    
    print("Input DataFrame setelah get_dummies:\n", input_df)  # Debugging output

    # Ensure all necessary features are present
    for feature in original_columns:
        if feature not in input_df.columns:
            input_df[feature] = 0

    # Reorder columns to match the training data
    input_df = input_df.reindex(columns=original_columns, fill_value=0)

    print("Input DataFrame setelah reindexing:\n", input_df)  # Debugging output

    # Scaling and PCA transformation
    input_scaled = scaler.transform(input_df)
    input_reduced = pca.transform(input_scaled)

    return input_reduced

def predict(data):
    model, scaler, pca, original_columns = load_model()
    preprocessed_data = preprocess_data(data, scaler, pca, original_columns)
    prediction = model.predict(preprocessed_data)
    return round(prediction[0])
