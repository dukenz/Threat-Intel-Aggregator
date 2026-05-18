import json
from collections import defaultdict
from pathlib import Path


DATA_FILE = Path("data/sample_iocs.json")
REPORT_FILE = Path("reports/sample_report.md")


def load_iocs(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def categorize_iocs(iocs):
    categorized = defaultdict(set)

    for item in iocs["indicators"]:
        indicator_type = item.get("type", "unknown")
        indicator_value = item.get("value", "")

        if indicator_value:
            categorized[indicator_type].add(indicator_value)

    return categorized


def generate_report(categorized_iocs):
    total_count = sum(len(values) for values in categorized_iocs.values())

    report = []
    report.append("# Threat Intelligence Report\n")
    report.append(f"Total Unique Indicators: {total_count}\n")

    for indicator_type, values in categorized_iocs.items():
        report.append(f"\n## {indicator_type.upper()} Indicators\n")

        for value in sorted(values):
            report.append(f"- {value}")

    report.append("\n\n## Analyst Notes\n")
    report.append("- Review IP reputation before blocking.")
    report.append("- Validate domains against threat intelligence sources.")
    report.append("- Escalate confirmed malicious indicators to incident response.")

    return "\n".join(report)


def save_report(report):
    REPORT_FILE.parent.mkdir(exist_ok=True)

    with open(REPORT_FILE, "w") as file:
        file.write(report)


def main():
    iocs = load_iocs(DATA_FILE)
    categorized_iocs = categorize_iocs(iocs)
    report = generate_report(categorized_iocs)
    save_report(report)

    print("Threat intelligence report generated successfully.")
    print(f"Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
