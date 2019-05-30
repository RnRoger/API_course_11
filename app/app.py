from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def retrieve_data() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'vcfData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM malignant_data')
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'data': retrieve_data()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')