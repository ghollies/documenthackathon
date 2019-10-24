#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/dummy')
def dummy():
    return jsonify({
        "success": True,
        "data": {}
    })

if __name__ == '__main__':
    app.run()
