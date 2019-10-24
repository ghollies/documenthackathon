#!/usr/bin/env python3

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/api/interface/dummy')
def dummy():
    return jsonify({
        "success": True,
        "data": {}
    })

if __name__ == '__main__':
    app.run(debug=True)
