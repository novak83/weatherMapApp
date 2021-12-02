import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    city = "Honolulu"
    apiKey = "apiKey"
    unit = "metric"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units={unit}"

    data = requests.get(url=url)

    return render_template("index.html", data=data.json())

if __name__=="__main__":
    app.run(use_reloader=True, debug=True)
