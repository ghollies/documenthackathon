from StringIO import StringIO
from docxtpl import DocxTemplate
import os.path
import json

def from_template(template,jsonFile):
    target_file = StringIO()

    template = DocxTemplate(template)
    with open(jsonFile, 'r') as f:
        context = json.load(f) # gets the context used to render the document

    target_file = StringIO()
    template.render(context)
    newDoc = template
    newDoc.save("NewDoc1.docx")

    return target_file

if __name__ == "__main__":
    from_template("InvoiceTpl.docx","myData.json")
