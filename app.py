from flask import Flask, render_template
from database_connection import connect_to_data, connect_to_data2

app = Flask(__name__)


@app.route('/')
def hello():
    
    return render_template('index.html', data = connect_to_data())

@app.route('/dish')
def dish():
    
    return render_template('dish.html', data = connect_to_data2())

app.run(debug=True)