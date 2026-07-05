from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

# إنشاء مجلد static لحفظ الصور إذا لم يكن موجوداً
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/', methods=['GET', 'POST'])
def home():
    qr_generated = False
    text_input = ""
    
    if request.method == 'POST':
        text_input = request.form.get('text_data')
        if text_input:
            # توليد كود الـ QR
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(text_input)
            qr.make(fit=True)
            
            # حفظ الكود كصورة داخل مجلد static
            img = qr.make_image(fill_color="black", back_color="white")
            img.save("static/qr.png")
            qr_generated = True

    return render_template('index.html', qr_generated=qr_generated, text_input=text_input)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

