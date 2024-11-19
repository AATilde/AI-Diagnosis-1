import tensorflow as tf
from flask import Flask, request, jsonify
#from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

# Load the saved model
model = tf.keras.models.load_model('skin_cancer_model.keras')
#model = load_model('skin_cancer_model.keras')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img = Image.open(io.BytesIO(file.read()))
        img = img.resize((170, 170))  # Resize to match the input size of the model
        img_array = np.array(img) / 255.0  # Normalize pixel values
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        prediction = model.predict(img_array)[0][0]
        # You can map the prediction to a class label (e.g., cancer or non-cancer)
        # based on a threshold (e.g., 0.5)
        if prediction > 0.5:
            result = "Cancer"
        else:
            result = "Non-Cancer"

        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)