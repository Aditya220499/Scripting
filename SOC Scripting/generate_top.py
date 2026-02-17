import json
import os
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE = os.path.join(BASE_DIR, "input", "ip_description.json")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
OUTPUT_FILE = os.path.join(BASE_DIR, "output", "top_generated.sv")

COMMON_SIGNALS = ["clk", "rst_n"]


def load_metadata():
    with open(INPUT_FILE) as f:
        return json.load(f)


def collect_nets(ips):
    """
    Generate nets.
    - Shared nets for common signals (clk, rst_n)
    - Unique nets for other ports
    """
    nets = {}

    for ip in ips:
        for port in ip["ports"]:
            name = port["name"]
            width = port["width"]

            if name in COMMON_SIGNALS:
                # Shared net
                if name not in nets:
                    nets[name] = width
                else:
                    if nets[name] != width:
                        raise ValueError(f"Width mismatch on shared signal '{name}'")
            else:
                # Unique per instance
                net_name = f"{ip['instance']}__{name}"
                nets[net_name] = width

    return [{"name": k, "width": v} for k, v in nets.items()]


def validate_drivers(ips):
    """
    Ensure no multiple outputs drive same shared signal.
    """
    signal_map = {}

    for ip in ips:
        for port in ip["ports"]:
            name = port["name"]
            direction = port["dir"]

            if name in COMMON_SIGNALS:
                if name not in signal_map:
                    signal_map[name] = []

                signal_map[name].append(direction)

    for signal, directions in signal_map.items():
        if directions.count("output") > 1:
            raise ValueError(f"Multiple drivers detected on shared signal '{signal}'")


def validate_widths(ips):
    """
    Ensure shared signals have matching widths.
    """
    signal_widths = {}

    for ip in ips:
        for port in ip["ports"]:
            name = port["name"]
            width = port["width"]

            if name in COMMON_SIGNALS:
                if name not in signal_widths:
                    signal_widths[name] = width
                else:
                    if signal_widths[name] != width:
                        raise ValueError(f"Width mismatch on shared signal '{name}'")


def main():
    data = load_metadata()
    ips = data["ips"]

    validate_drivers(ips)
    validate_widths(ips)

    nets = collect_nets(ips)

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("top_template.sv.j2")

    output = template.render(
        ips=ips,
        nets=nets,
        common_signals=COMMON_SIGNALS
    )

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w") as f:
        f.write(output)

    print("Top module generated successfully.")


if __name__ == "__main__":
    main()
