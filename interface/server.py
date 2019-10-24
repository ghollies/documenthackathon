#!/usr/bin/env python3

from flask import Flask, jsonify, request
from os import environ
from datetime import datetime, timedelta
import subprocess
import requests


app = Flask(__name__)

VAULT_ADDR = 'https://vault.eng.appianci.net'

def refresh_aws_session_credentials():
    # Get a token for an application role via get-vault-token
    completed_process = subprocess.run(['get-vault-token', '--application', 'rekognition-detect-text'], stdout=subprocess.PIPE, check=True)
    application_token = completed_process.stdout.decode().strip()

    # Use the token to read a secret from Vault via Vault's REST API. Access the
    # JSON from the response as a Python object
    url = f'{VAULT_ADDR}/v1/prod.aws/creds/rekognition-detect-text'
    response = requests.get(url, headers={'X-Vault-Token': application_token})
    response.raise_for_status()
    r = response.json()

    return {
        'last_updated': datetime.now(),
        'aws_access_key_id': r['data']['access_key'],
        'aws_secret_access_key': r['data']['secret_key'],
        'aws_session_token': r['data']['security_token']
    }


@app.route('/api/interface/dummy')
def dummy():
    return jsonify({
        "success": True,
        "data": {}
    })

@app.route('/api/interface/generate')
def interface_generate():
    data = refresh_aws_session_credentials()



    # data = '''
    # {
    #     a!textField(
    #         label: "Label"
    #     )
    # }
    # '''

    return jsonify({
        "success": True,
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True)
