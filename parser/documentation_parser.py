def generate_documentation(raw_notes, doc_type="infrastructure"):
    if not raw_notes.strip():
        return ""

    titles = {
        "infrastructure": "# Infrastructure Documentation",
        "server": "# Server Documentation",
        "network": "# Network Device Documentation",
        "workstation": "# Workstation Documentation",
    }

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
        "firewall": "## Firewall",
        "switch": "## Switch",
        "router": "## Router",
        "printer": "## Printer",
        "workstation": "## Workstation",
        "user": "Assigned User",
        "department": "Department",
        "serial": "Serial Number",
    }

    lines = raw_notes.splitlines()
    output = [titles.get(doc_type, "# Infrastructure Documentation"), ""]

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
                output.append(f"{label}: {value}")
                output.append("")
            else:
                output.append(line)
                output.append("")
        else:
            output.append(line)
            output.append("")

    return "\n".join(output)