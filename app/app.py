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

    query = 'SELECT * FROM malignant_data WHERE chrom=%s AND pos=%s AND alt=%s;'
    cursor.execute(query, (chr, pos, alt))

    results = cursor.fetchone()

    with open("data.txt", 'w') as f:
        for row in results:
            f.write("%s\n" % str(row))
    f.close()

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