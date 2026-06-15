function copyDocumentation() {
    const generatedDocs = document.getElementById("generated-docs").innerText;

    navigator.clipboard.writeText(generatedDocs)
        .then(() => {
            alert("Documentation copied to clipboard.");
        })
        .catch(() => {
            alert("Unable to copy documentation.");
        });
}