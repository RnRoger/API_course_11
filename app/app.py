from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)


def retrieve_data(chr, pos, alt):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'vcfData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    query = 'SELECT TOP 1 * FROM malignant_data WHERE chrom=' + str(inf.get(chr) + ' AND pos=' + str(inf.get(pos)) + ' AND alt=' + str(inf.get(alt)))
    cursor.execute(query)
    results = "1 BOEJAAA"

    result = str(cursor.fetchone()[0])
    cursor.close()
    connection.close()

    return results


@app.route('/api', methods=['GET'])
def api():
    chr = request.args.get('chr')
    pos = request.args.get('pos')
    alt = request.args.get('alt')
    results = retrieve_data(chr, pos, alt)
    return str(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0')