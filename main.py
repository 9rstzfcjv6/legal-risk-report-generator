from data import document
from input_analyzer import analyze_contract_text
from report_generator import generate_markdown_report
from export import save_markdown_report


def collect_contract_text():
    print("Paste the contract excerpt below.")
    print("When you are done, type END on a new line and press Enter.")
    print("---------------------------------------------------------")

    lines = []

    while True:
        line = input()

        if line == "END":
            break

        lines.append(line)

    return "\n".join(lines)


def main():
    contract_text = collect_contract_text()

    risks = analyze_contract_text(contract_text)

    report = generate_markdown_report(document, risks)

    output_path = "Outputs/legal_risk_report.md"
    save_markdown_report(report, output_path)

    print("")
    print("Legal Risk Report Generator v2.2")
    print("--------------------------------")
    print("Contract text analyzed successfully.")
    print("Detected risks:", len(risks))
    print("Output file:", output_path)


if __name__ == "__main__":
    main()