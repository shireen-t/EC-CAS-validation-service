import csv
import re

# Validate EC or CAS number format
def validate_identifier(identifier):
    cas_pattern = r'^\d{2,7}-\d{2}-\d$'
    ec_pattern = r'^[2-9]\d{2}-\d{3}-\d$'

    if re.match(cas_pattern, identifier):
        return "CAS"
    elif re.match(ec_pattern, identifier):
        return "EC"
    else:
        return "Invalid"

# Load CSV data into dictionary
identifier_data = {}

with open('data.csv', mode='r', encoding='cp1252', errors='ignore') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # skip header row
    for row in reader:
        ec_number = row[0]
        cas_number = row[1]
        material_name = row[2]
        sources = {
            "OECD": row[3],
            "CANDIDATE": row[4],
            "REACH": row[5],
            "FORD": row[6],
            "TSCA": row[7]
        }
        msds_availability = row[8]
        entry = {
            'ECNumber': ec_number,
            'CASNumber': cas_number,
            'MaterialName': material_name,
            'Sources': [key for key, value in sources.items() if value == "YES"],
            'MSDSAvailability': msds_availability
        }
        if ec_number:
            identifier_data[ec_number] = entry
        if cas_number:
            identifier_data[cas_number] = entry

# Function to retrieve paired identifier and additional information
def retrieve_information(identifier, identifier_type):
    entry = identifier_data.get(identifier)
    if entry:
        paired_identifier = entry['CASNumber'] if identifier_type == 'EC' else entry['ECNumber']
        return {
            'PairedIdentifier': paired_identifier,
            'MaterialName': entry['MaterialName'],
            'Sources': entry['Sources'],
            'MSDSAvailability': entry['MSDSAvailability']
        }
    return None

# Function to check validity of identifier
def check_identifier_validity(identifier):
    identifier_type = validate_identifier(identifier)
    if identifier_type in ["CAS", "EC"]:
        return {'valid': True, 'type': identifier_type}
    return {'valid': False, 'type': None}

# Example usage
identifier = '243-053-7'  # Example EC number
validity_check = check_identifier_validity(identifier)
if validity_check['valid']:
    info = retrieve_information(identifier, validity_check['type'])
    if info:
        print(f"Paired Identifier: {info['PairedIdentifier']}")
        print(f"Material Name: {info['MaterialName']}")
        print(f"Sources: {', '.join(info['Sources'])}")
        print(f"MSDS Availability: {info['MSDSAvailability']}")
    else:
        print("Identifier not found in the data.")
else:
    print("Invalid identifier.")
