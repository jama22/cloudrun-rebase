from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

# assets: https://flask-assets.readthedocs.io/en/latest/
assets = Environment(app)
assets.url = app.static_url_path

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)