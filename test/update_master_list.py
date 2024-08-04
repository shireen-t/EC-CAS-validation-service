import pandas as pd # type: ignore
import mysql.connector # type: ignore
import time

# Define a function to get the EC number from the database
def get_ec_number(cas_number, db_connection):
    cursor = db_connection.cursor()
    start_time = time.time()
    cursor.execute("SELECT ec_number FROM chemicals WHERE cas_number = %s", (cas_number,))
    result = cursor.fetchone()
    cursor.fetchall()  # Consume any unread results to avoid InternalError
    end_time = time.time()
    cursor.close()
    retrieval_time = end_time - start_time
    return (result[0] if result else "EC number not found", retrieval_time)

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="chemical_db"
)

# Load the Excel file, ensuring all columns are read as strings
file_path = 'EDITED.xlsx'  # Update the file path if necessary
df = pd.read_excel(file_path, dtype=str)

# Start the overall timer
overall_start_time = time.time()

# Iterate over the rows and update the EC numbers
for index, row in df.iterrows():
    if pd.isna(row['ECNumber']) and not pd.isna(row['CASNumber']):
        cas_number = row['CASNumber']
        ec_number, retrieval_time = get_ec_number(cas_number, db_connection)
        if ec_number != "EC number not found":
            df.at[index, 'ECNumber'] = ec_number
            print(f"Updated CAS Number: {cas_number} with EC Number: {ec_number} (Retrieved in {retrieval_time:.4f} seconds)")
        else:
            print(f"EC number for CAS Number: {cas_number} not found in the database")

# Save the updated Excel file
output_file_path = 'Master_List_PFASAGE_EC_edit.xlsx'
df.to_excel(output_file_path, index=False)

# Close the database connection
db_connection.close()

# End the overall timer
overall_end_time = time.time()
overall_time = overall_end_time - overall_start_time

print(f"\nProcess completed in {overall_time:.4f} seconds")
print(f"Updated file saved at: {output_file_path}")
