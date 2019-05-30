from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)


def retrieve_data(inf):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'vcfData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    if 'chr' in inf.keys() and 'pos' in inf.keys() and 'alt' in inf.keys():
        query = 'SELECT TOP 1 * FROM malignant_data WHERE chrom=' + str(inf.get('chr') + ' AND pos=' + str(inf.get('pos')) + ' AND alt=' + str(inf.get('alt')))
        cursor.execute(query)
        print("1 BOEJAAA")
    else:
        cursor.execute('SELECT * FROM malignant_data')
        print("2 BAMMMMM")
    results = cursor.fetchone()
    print(results)
    cursor.close()
    connection.close()

    return results


@app.route('/api', methods=['GET'])
def api() -> str:
    inf = request.args.to_dict()
    results = retrieve_data(inf)
    return str(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0')