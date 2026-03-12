from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract", methods=["POST"])
def extract():
    file = request.files["image"]
    image = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(image)
    return render_template("index.html", result=text)

if __name__ == "__main__":
    app.run(debug=True)
