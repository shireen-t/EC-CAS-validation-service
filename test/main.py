import re
import mysql.connector # type: ignore

def validate_number(number):
    """
    Validate whether the given number is a CAS number, an EC number, or not a valid number.

    Parameters:
        number (str): The number to validate.

    Returns:
        str: "CAS" if it's a valid CAS number,
             "EC" if it's a valid EC number,
             "Invalid" if it's not a valid number.
    """
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

number = input("Enter a number: ")
result = validate_number(number)

if result == "CAS":
    ec_number = get_ec_number(number)
    print(f"CAS Number: {number}, EC Number: {ec_number}")
elif result == "EC":
    cas_number = get_cas_number(number)
    print(f"EC Number: {number}, CAS Number: {cas_number}")
else:
    print(f"{number} is not a valid CAS or EC number.")