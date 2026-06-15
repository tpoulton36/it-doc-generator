from flask import Flask, render_template, request

app = Flask(__name__)


def generate_documentation(raw_notes):
    if not raw_notes.strip():
        return ""

    lines = raw_notes.splitlines()
    output = ["# Infrastructure Documentation", ""]

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.lower().startswith("server:"):
            server_name = line.split(":", 1)[1].strip()
            output.append(f"## Server: {server_name}")
            output.append("")

        elif line.lower().startswith("ip:"):
            ip_address = line.split(":", 1)[1].strip()
            output.append(f"IP Address: {ip_address}")
            output.append("")

        elif line.lower().startswith("os:"):
            operating_system = line.split(":", 1)[1].strip()
            output.append(f"Operating System: {operating_system}")
            output.append("")

        else:
            output.append(line)
            output.append("")

    return "\n".join(output)


@app.route("/", methods=["GET", "POST"])
def home():
    generated_docs = ""
    raw_notes = ""

    if request.method == "POST":
        raw_notes = request.form.get("raw_notes", "")
        generated_docs = generate_documentation(raw_notes)

    return render_template(
        "index.html",
        raw_notes=raw_notes,
        generated_docs=generated_docs
    )


if __name__ == "__main__":
    app.run(debug=True)