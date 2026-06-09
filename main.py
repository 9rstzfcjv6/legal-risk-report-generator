from data import document
from input_analyzer import analyze_contract_text
from report_generator import generate_markdown_report
from export import save_markdown_report


def main():
    contract_text = """
    The parties agree to collaborate on the development of medical AI technology.
    Any foreground IP developed during the project may be jointly owned by the parties.
    Confidential technical data may be used for machine learning model improvement.
    The research partner may publish project results after completion.
    """

    risks = analyze_contract_text(contract_text)

    report = generate_markdown_report(document, risks)

    output_path = "Outputs/legal_risk_report.md"
    save_markdown_report(report, output_path)

    print("Legal Risk Report Generator v2.1")
    print("--------------------------------")
    print("Contract text analyzed successfully.")
    print("Detected risks:", len(risks))
    print("Output file:", output_path)


if __name__ == "__main__":
    main()