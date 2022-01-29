from typing import List, Dict
from flask import Flask,jsonify
import mysql.connector
import json

app = Flask(__name__)


def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()
    print(jsonify(results), type(jsonify(results)))
    return jsonify(results)


@app.route('/')
def index():
    print("hi")
    return favorite_colors()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
