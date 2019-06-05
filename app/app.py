#########################################################################################################################
# Authors:  Awan Al Koerdi & Melanie Opperman                                                                           #
# Version:  1.0                                                                                                         #
# Date:     20-05-2019                                                                                                  #
# Finished: 06-06-2019                                                                                                  #
#                                                                                                                       #
# Function: Parameters chr, pos and alt can be passed through a URL. When variant is present in database, additional    #
#           information is retrieved.                                                                                   #
##########################################################################################################################

# required imports
from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)

# Retrieves data from local database based on given parameters chr, pos and alt. Which represents chromosome, position and
# alternative allele
def retrieve_malignant_data(chr, pos, alt):
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

    cursor.close()
    connection.close()

    return results


# Retrieves data from local database based on given parameters chr, pos and alt. Which represents chromosome, position and
# alternative allele
def retrieve_benign_data(chr, pos, alt):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'vcfData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    query = 'SELECT * FROM benign_data WHERE chrom=%s AND pos=%s AND alt=%s;'
    cursor.execute(query, (chr, pos, alt))
    results = cursor.fetchone()

    cursor.close()
    #connection.close()

    return results

# api function can be called from URL and initiate the chr, pos and alt parameters/variable.
@app.route('/api', methods=['GET'])
def api():
    chr = request.args.get('chr')
    pos = request.args.get('pos')
    alt = request.args.get('alt')
    results = retrieve_malignant_data(chr, pos, alt)
    if results != None:
        return(str(results).strip("()"))
    else:
        results = retrieve_benign_data(chr, pos, alt)
        return(str(results))
#        if results != None:
#            return("Benign")


    
    #return str(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
