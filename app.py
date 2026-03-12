from flask import Flask, request, render_template
from PIL import Image
import easyocr
import io
import numpy as np

app = Flask(__name__)
reader = easyocr.Reader(['en'])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract", methods=["POST"])
def extract():
    file = request.files["image"]
    image = Image.open(io.BytesIO(file.read()))
    image_np = np.array(image)
    result = reader.readtext(image_np, detail=0)
    text = "\n".join(result)
    return render_template("index.html", result=text)

if __name__ == "__main__":
    app.run(debug=True)
