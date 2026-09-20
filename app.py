from flask import Flask, render_template
from products import products

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)