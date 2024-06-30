import pickle

def load_model():
    with open('models/model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def predict(data):
    model = load_model()
    prediction = model.predict([data])
    return prediction[0]
