import re

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

# Example usage
number = input("Enter a number: ")

result = validate_number(number)

if result == "CAS":
    print(f"{number} is a valid CAS number.")
elif result == "EC":
    print(f"{number} is a valid EC number.")
else:
    print(f"{number} is not a valid CAS or EC number.")

"""
CAS:
Starts with 2 to 7 digits.
A hyphen.
Followed by 2 digits.
Another hyphen.
Ends with a single digit.

"""

"""
EC:
Starts with a digit between 2 and 9.
Followed by two digits.
A hyphen.
Followed by three digits.
Another hyphen.
Ends with a single digit.

"""