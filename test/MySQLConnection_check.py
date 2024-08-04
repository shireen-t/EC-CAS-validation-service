import mysql.connector # type: ignore

# Establishing connection
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
        
        # You can perform further operations here
        
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")
finally:
    # Close the connection when done
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
