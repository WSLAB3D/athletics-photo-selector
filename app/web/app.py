from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def gallery():
    df = pd.read_csv("../output/tagged_images.csv")
    images = df.sort_values("score", ascending=False).head(40).to_dict(orient="records")
    return render_template("gallery.html", images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
