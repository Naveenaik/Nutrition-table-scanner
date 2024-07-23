from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import base64
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
CORS(app)

def process_image(image):
    # Example processing: Convert to grayscale and create a histogram
    gray_image = image.convert('L')
    
    # Create a histogram
    histogram = gray_image.histogram()
    
    # Plot the histogram
    plt.figure()
    plt.plot(histogram)
    plt.title("Grayscale Histogram")
    
    # Save plot to a PNG in-memory
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    
    return plot_url

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    image = Image.open(file.stream)
    plot_url = process_image(image)
    return jsonify({"plot_url": plot_url})

if __name__ == '__main__':
    app.run(debug=True)
