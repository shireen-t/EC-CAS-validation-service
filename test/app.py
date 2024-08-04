from flask import Flask, request, jsonify
import re
import mysql.connector

app = Flask(__name__)


def validate_number(number):
    cas_pattern = r'^\d{2,7}-\d{2}-\d$'
    ec_pattern = r'^[2-9]\d{2}-\d{3}-\d$'

    if re.match(cas_pattern, number):
        return "CAS"
    elif re.match(ec_pattern, number):
        return "EC"
    else:
        return "Invalid"


def get_ec_number(cas_number):
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="chemical_db"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT ec_number FROM chemicals WHERE cas_number = %s", (cas_number,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0] if result else "EC number not found"


def get_cas_number(ec_number):
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="chemical_db"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT cas_number FROM chemicals WHERE ec_number = %s", (ec_number,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0] if result else "CAS number not found"


@app.route('/validate', methods=['GET'])
def validate():
    number = request.args.get('number')
    result = validate_number(number)
    response = {"input_number": number, "validation_result": result}

    if result == "CAS":
        ec_number = get_ec_number(number)
        response["ec_number"] = ec_number
    elif result == "EC":
        cas_number = get_cas_number(number)
        response["cas_number"] = cas_number

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
