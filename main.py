from data import document
from file_reader import read_contract_file
from input_analyzer import analyze_contract_text
from report_generator import generate_markdown_report
from export import save_markdown_report


def main():
    input_path = "inputs/sample_contract.txt"
    output_path = "Outputs/legal_risk_report.md"

    contract_text = read_contract_file(input_path)

    risks = analyze_contract_text(contract_text)

    report = generate_markdown_report(document, risks)

    save_markdown_report(report, output_path)

    print("Legal Risk Report Generator v2.3")
    print("--------------------------------")
    print("Contract file analyzed successfully.")
    print("Input file:", input_path)
    print("Detected risks:", len(risks))
    print("Output file:", output_path)


if __name__ == "__main__":
    main()