from flask import Flask, render_template, request, Response
from parser.documentation_parser import generate_documentation

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    generated_docs = ""
    raw_notes = ""
    doc_type = "infrastructure"

    if request.method == "POST":
        raw_notes = request.form.get("raw_notes", "")
        doc_type = request.form.get("doc_type", "infrastructure")
        generated_docs = generate_documentation(raw_notes, doc_type)

    return render_template(
        "index.html",
        raw_notes=raw_notes,
        generated_docs=generated_docs,
        doc_type=doc_type
    )


@app.route("/download", methods=["POST"])
def download():
    raw_notes = request.form.get("raw_notes", "")
    generated_docs = generate_documentation(raw_notes)

    return Response(
        generated_docs,
        mimetype="text/markdown",
        headers={
            "Content-Disposition": "attachment; filename=documentation.md"
        }
    )


if __name__ == "__main__":
    app.run(debug=True)