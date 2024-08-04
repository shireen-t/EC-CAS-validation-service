import mysql.connector # type: ignore

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

cas_number = "162221-28-5"
ec_number = get_ec_number(cas_number)
print(f"CAS Number: {cas_number}, EC Number: {ec_number}")
