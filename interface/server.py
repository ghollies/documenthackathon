#!/usr/bin/env python3

from flask import Flask, jsonify, request
import analyzeShapes

app = Flask(__name__)


@app.route('/api/interface/dummy')
def dummy():
    return jsonify({
        "success": True,
        "data": {}
    })

@app.route('/api/interface/generate', methods=['POST'])
def interface_generate():
    data = analyzeShapes.main(request.data)

    return jsonify({
        "success": True,
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True)
