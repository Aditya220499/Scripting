import json
import os
from jinja2 import Environment, FileSystemLoader

INPUT_FILE = "input/ip_description.json"
TEMPLATE_DIR = "templates"
OUTPUT_FILE = "output/top_generated.sv"

def load_metadata():
    with open(INPUT_FILE) as f:
        return json.load(f)

def collect_nets(ips):
    nets = []
    for ip in ips:
        for port in ip["ports"]:
            nets.append({
                "name": f"{ip['instance']}__{port['name']}",
                "width": port["width"]
            })
    return nets

def main():
    data = load_metadata()
    ips = data["ips"]
    nets = collect_nets(ips)

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("top_template.sv.j2")

    output = template.render(ips=ips, nets=nets)

    os.makedirs("output", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write(output)

    print("Top module generated successfully.")

if __name__ == "__main__":
    main()
