# cas_to_ec.py
import argparse
from data import CAS_EC_MAPPING

def get_ec_number(cas_number):
    return CAS_EC_MAPPING.get(cas_number, "EC number not found")

def main():
    parser = argparse.ArgumentParser(description="Get EC number for a given CAS number.")
    parser.add_argument("cas_number", type=str, help="The CAS number to look up.")
    args = parser.parse_args()

    cas_number = args.cas_number
    ec_number = get_ec_number(cas_number)

    print(f"CAS Number: {cas_number}")
    print(f"EC Number: {ec_number}")

if __name__ == "__main__":
    main()
