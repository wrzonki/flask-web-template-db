from flask import Flask, render_template, url_for
from flask_sqlalechmy import SQLAlchemy

app = Flask(__name__)
app.config

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)