from flask import Flask, render_template, request, redirect, url_for
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Remove the existing QR code image if it exists
    qr_image_path = 'static/image.jpg'
    if os.path.exists(qr_image_path):
        os.remove(qr_image_path)
    return render_template('index.html')

@app.route('/makeQr', methods=['POST'])
def make():
    try:
        data = request.form['data']
        if data:
            qr = qrcode.make(data)
            qr.save('static/image.jpg')
        else:
            return render_template('index.html', error="No data provided.")
    except Exception as e:
        return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
