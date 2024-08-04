# EC CAS Validation Service

A Python-based service for validating and cross-referencing EC (European Community) and CAS (Chemical Abstracts Service) numbers, along with retrieving associated information.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Data](#data)
7. [Future Enhancements](#future-enhancements)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgements](#acknowledgements)

## Introduction
The EC CAS Validation Service is designed to help users validate chemical identifiers and retrieve detailed information based on a dataset of over 107,000 entries. This service can identify if a given identifier is valid, determine its type (EC or CAS), and provide associated data such as paired identifiers, material names, and the availability of Material Safety Data Sheets (MSDS).

For detailed documentation, please refer to the [Pager Documentation](https://equinox-cost-01c.notion.site/EC-CAS-Validation-Service-22263ba624694704b269c4c88b3597ab?pvs=4).

## Features
- **Identifier Validation**: Verify if an identifier conforms to EC or CAS number formats.
- **Data Retrieval**: Fetch paired identifiers and additional information from the dataset.
- **RESTful API**: Access the service through a simple API for easy integration with other applications.

## Installation

### Prerequisites
- Python 3.x
- Flask
- Git

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/shireen-t/EC-CAS-validation-service.git
   cd EC-CAS-validation-service

2. **Install Dependencies**
   ```bash
    pip install -r requirements.txt
3. **Run the Application**
    ```bash
    python routes.py
    ```
## Usage
The service can be used to validate identifiers and retrieve associated information.

### Example
To check the validity of an identifier and retrieve information:
    
```python
from ec_cas_validation_service import check_identifier_validity, retrieve_information

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
```

## API Endpoints

### Base URL
`/` - Returns a simple welcome message.

### Get Other Number and Information
`GET /api/get_other_number/<number>` - Checks the validity of a number and retrieves associated information.

#### Example Request
```bash
    GET /api/get_other_number/243-053-7
```

#### Example Response
```json
{
  "status": "success",
  "paired_identifier": "135-37-7",
  "material_name": "Example Material",
  "sources": ["OECD", "REACH"],
  "msds_availability": "Yes"
}
```

## Data
The dataset consists of 107,000 entries with the following fields:
* EC Number
* CAS Number
* Material Name
* Sources: Presence in various databases (OECD, CANDIDATE, REACH, FORD, TSCA)
* MSDS Availability

## Future Enhancements
* **Expanded Database**: Addition of more comprehensive datasets.
* **Enhanced Validation**: Improved validation logic.
* **User Authentication**: Secure access to the API.
* **Advanced Search**: Search by material names or other attributes.
* **Data Analytics**: Insights into chemical data trends.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE]() file for details.

## Acknowledgements
Data sources include public databases and regulatory agencies.
