from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)



model = load_model('vgg_16_tea_leaf_disease.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        img = Image.open(io.BytesIO(file.read()))
        img = img.resize((224, 224))

        img_array = np.asarray(img)

        img_array = img_array / 255.0

        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)

        predicted_index = np.argmax(prediction)

        return jsonify({'health_index': predicted_index})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
