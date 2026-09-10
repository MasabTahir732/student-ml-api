import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_version():
    if os.path.exists("VERSION"):
        with open("VERSION", "r") as f:
            return f.read().strip()
    return "1.0.0"


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": get_version(),
        "model_version": "model-1"
    }), 200
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    if not data or "value" not in data:
        return jsonify({"error": "Missing 'value' field in JSON body"}), 400

    val = data["value"]
    if not isinstance(val, (int, float)):
        return jsonify({"error": "'value' must be numeric"}), 400

    # Linear transformation placeholder for ML inference
    prediction = val * 2
    return jsonify({
        "input": val,
        "prediction": prediction
    }), 200

if __name__ == "__main__":
    # Must bind to 0.0.0.0 for Docker container networking
    app.run(host="0.0.0.0", port=5000)