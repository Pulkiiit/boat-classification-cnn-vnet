from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from utils import preprocess_image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load model at startup
model = load_model("model/boat_classifier.keras")

# Labels
class_names = ["buoy", "cruise ship", "ferry boat", "freight boat", "gondola", "inflatable boat", "kayak", "paper boat", "sailboat"]

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    img = preprocess_image(file)

    preds = model.predict(np.expand_dims(img, axis=0))
    class_id = int(tf.argmax(preds[0]))
    confidence = float(tf.nn.softmax(preds[0])[class_id])

    return jsonify({
        "prediction": class_names[class_id],
        "confidence": round(confidence, 4)
    })

if __name__ == "__main__":
    app.run(debug=True)
