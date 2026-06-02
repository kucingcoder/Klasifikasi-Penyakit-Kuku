import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template, jsonify
from PIL import Image

app = Flask(__name__)

# 1. Muat model yang sudah disimpan
MODEL_PATH = 'nail_disease_model.keras'
model = tf.keras.models.load_model(MODEL_PATH)

# Urutannya harus sama persis dengan yang dihasilkan
CLASS_NAMES = ['healthy', 'onychomycosis', 'psoriasis'] 

IMG_HEIGHT = 224
IMG_WIDTH = 224

def preprocess_image(image_file):
    # Membaca gambar, memastikan format RGB, dan mengubah ukuran ke 224x224
    img = Image.open(image_file).convert('RGB')
    img = img.resize((IMG_WIDTH, IMG_HEIGHT))
    
    # Konversi ke array NumPy
    img_array = tf.keras.utils.img_to_array(img)
    
    # Tambahkan dimensi batch (karena model menerima input batch: [batch_size, height, width, channels])
    img_array = tf.expand_dims(img_array, 0)
    return img_array

@app.route('/')
def index():
    # Menampilkan halaman web HTML
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Tidak ada file yang diunggah'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'File tidak valid'})

    try:
        # Preprocessing gambar
        img_array = preprocess_image(file)
        
        # Lakukan prediksi (menghasilkan logits)
        predictions = model.predict(img_array)
        
        # Konversi logits menjadi probabilitas menggunakan Softmax
        score = tf.nn.softmax(predictions[0])
        
        # Cari kelas dengan probabilitas tertinggi
        predicted_class = CLASS_NAMES[np.argmax(score)]
        confidence = 100 * np.max(score)

        return jsonify({
            'class': predicted_class,
            'confidence': float(confidence)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Jalankan server lokal
    app.run(debug=True, port=5000)