from data import document, risks
from report_generator import generate_markdown_report
from export import save_markdown_report


def main():
    report = generate_markdown_report(document, risks)

    output_path = "outputs/legal_risk_report.md"
    save_markdown_report(report, output_path)

    print("Legal Risk Report Generator v2.0")
    print("--------------------------------")
    print("Report generated successfully.")
    print("Output file:", output_path)


if __name__ == "__main__":
    main()
