from flask import Flask, render_template
from database_connection import connect_to_data

app = Flask(__name__)


@app.route('/')
def hello():
    
    return render_template('index.html', data = connect_to_data())

app.run(debug=True)