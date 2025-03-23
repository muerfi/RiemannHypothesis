# web_calculator/app.py
from flask import Flask, render_template, request
from mpmath import zeta

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        try:
            sigma = float(request.form["sigma"])
            t = float(request.form["t"])
            s = complex(sigma, t)
            zeta_val = zeta(s)
            return render_template("result.html", sigma=sigma, t=t, zeta_val=zeta_val)
        except ValueError:
            error = "Please enter valid numeric values for σ and t."
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    return render_template("index.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
