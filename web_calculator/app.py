# web_calculator/app.py
from flask import Flask, render_template, request
from mpmath import zeta

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sigma = float(request.form["sigma"])
        t = float(request.form["t"])
        s = complex(sigma, t)
        zeta_val = zeta(s)
        return render_template("result.html", sigma=sigma, t=t, zeta_val=zeta_val)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
