import mysql.connector # type: ignore
import csv

def insert_data_into_db(csv_file):
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="root",
            database="chemical_db"
        )
        if connection.is_connected():
            print("Connection to MySQL database successful")
        
        cursor = connection.cursor()

        with open(csv_file, mode='r', encoding='utf-8', errors='replace') as infile:
            reader = csv.reader(infile)
            row_count = 0
            for row in reader:
                cas_number, ec_number, name = row
                cursor.execute(
                    "INSERT INTO chemicals (cas_number, ec_number, name) VALUES (%s, %s, %s)",
                    (cas_number, ec_number, name)
                )
                row_count += 1
                print(f"Successfully inserted row {row_count}: CAS number {cas_number}, EC number {ec_number}, Name {name}")

        connection.commit()
        print(f"Total {row_count} rows inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

# Example usage
insert_data_into_db('new_ECCAS.csv')