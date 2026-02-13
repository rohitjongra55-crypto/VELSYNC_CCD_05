from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Home route
@app.route("/")
def home():
    return "ML App is running"

# Test route for browser
@app.route("/test")
def test():
    sample = [5.1, 3.5, 1.4, 0.2]
    prediction = model.predict([sample])
    return {"sample": sample, "prediction": int(prediction[0])}

# Predict route (POST JSON)
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["features"]
        prediction = model.predict([data])
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # Fixed host and port for Windows, debug=True for auto-reload
    app.run(host="127.0.0.1", port=5000, debug=True)
