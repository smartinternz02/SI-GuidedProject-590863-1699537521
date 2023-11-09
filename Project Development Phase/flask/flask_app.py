from flask import Flask, render_template, request
#from tensorflow.keras.models import load_model
#import numpy as np
#from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load the model
#modeln = load_model("vgg_16_tea_leaf_disease.h5")

@app.route('/')
def index():
    return render_template('index.html')

'''
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the image file from the request
        f = request.files['image']

        # Save the file
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'uploads', f.filename)
        f.save(filepath)

        # Load and preprocess the image
        img = image.load_img(filepath, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)  # You may need to define the preprocess_input function

        # Get the prediction
        prediction = np.argmax(modeln.predict(img_data))
        index = ['Antracnose', 'algal leaf', 'bird eye spot', 'brown light', 'gray light', 'healthy', 'red leaf spot', 'white spot']
        nresult = str(index[prediction])

        return nresult  # Return the result to update the HTML
'''        


if __name__ == '__main__':
    app.run(debug=True)

