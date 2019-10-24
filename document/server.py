#!/usr/bin/env python3

from flask import Flask, jsonify, request, send_file
from PyPDF2 import PdfFileReader, PdfFileWriter
from io import BytesIO


app = Flask(__name__)


@app.route('/api/dummy')
def dummy():
    return jsonify({
        "success": True,
        "data": {}
    })

@app.route('/api/document/merge', methods=['POST'])
def document_merge():
    writer = PdfFileWriter()    
    for key in sorted(request.files.keys()):
        reader = PdfFileReader(request.files[key])
        for p in range(reader.getNumPages()):
            writer.addPage(reader.getPage(p))

    tmp = BytesIO()
    writer.write(tmp)
    tmp.seek(0)

    return send_file(
        tmp,
        as_attachment=True,
        attachment_filename='merged.pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)
