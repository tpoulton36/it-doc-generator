from flask import Flask, render_template, request, Response
from parser.documentation_parser import generate_documentation
from database.db import init_db, save_project, get_projects, get_project

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    generated_docs = ""
    raw_notes = ""
    doc_type = "infrastructure"
    projects = get_projects()
    message = ""

    if request.method == "POST":
        raw_notes = request.form.get("raw_notes", "")
        doc_type = request.form.get("doc_type", "infrastructure")
        generated_docs = generate_documentation(raw_notes, doc_type)

        if request.form.get("action") == "save":
            project_name = request.form.get("project_name", "").strip()

            if project_name:
                save_project(project_name, doc_type, raw_notes, generated_docs)
                message = "Project saved successfully."
                projects = get_projects()
            else:
                message = "Project name is required to save."

    return render_template(
        "index.html",
        raw_notes=raw_notes,
        generated_docs=generated_docs,
        doc_type=doc_type,
        projects=projects,
        message=message
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

@app.route("/load/<int:project_id>")
def load_project(project_id):
    project = get_project(project_id)

    if not project:
        return "Project not found", 404

    return render_template(
        "index.html",
        project_name=project["project_name"],
        raw_notes=project["raw_notes"],
        generated_docs=project["generated_docs"],
        doc_type=project["doc_type"],
        projects=get_projects(),
        message=f"Loaded project: {project['project_name']}"
    )


if __name__ == "__main__":
    app.run(debug=True)