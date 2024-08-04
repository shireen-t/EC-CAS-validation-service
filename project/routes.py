from flask import Flask, jsonify
from ec_cas_validation_service import check_identifier_validity, retrieve_information

app = Flask('ec_cas_api')

# Base URL route
@app.route('/')
def base_url():
    return 'EC CAS API'

# Route to check number validity and retrieve paired identifier along with additional information
@app.route('/api/get_other_number/<number>', methods=['GET'])
def get_other_number(number):
    result = check_identifier_validity(number)
    if result['valid']:
        info = retrieve_information(number, result['type'])
        if info:
            response = {
                'status': 'success',
                'paired_identifier': info['PairedIdentifier'],
                'material_name': info['MaterialName'],
                'sources': info['Sources'],
                'msds_availability': info['MSDSAvailability']
            }
        else:
            response = {
                'status': 'error',
                'message': 'Identifier not found in the data.'
            }
    else:
        response = {
            'status': 'error',
            'message': 'Invalid number'
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
