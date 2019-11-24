from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlechmy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Columne(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, defoult=datetime.utcnow)

    def __repr__(self_):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)