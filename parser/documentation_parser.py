def generate_documentation(raw_notes):
    if not raw_notes.strip():
        return ""

    field_map = {
        "server": "## Server",
        "hostname": "Hostname",
        "ip": "IP Address",
        "subnet": "Subnet",
        "gateway": "Default Gateway",
        "dns": "DNS Server",
        "os": "Operating System",
        "vendor": "Vendor",
        "model": "Model",
        "location": "Location",
    }

    lines = raw_notes.splitlines()
    output = ["# Infrastructure Documentation", ""]

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip().lower()
            value = value.strip()

            if key in field_map:
                label = field_map[key]

                if key == "server":
                    output.append(f"{label}: {value}")
                else:
                    output.append(f"{label}: {value}")

                output.append("")
            else:
                output.append(line)
                output.append("")
        else:
            output.append(line)
            output.append("")

    return "\n".join(output)