from data import document
from file_reader import read_contract_file, get_text_files
from input_analyzer import analyze_contract_text
from report_generator import generate_markdown_report, generate_batch_summary_report
from risk_engine import (
    calculate_risk_counts,
    calculate_risk_score,
    get_overall_assessment,
    calculate_category_counts
)
from export import save_markdown_report


def build_output_file_name(input_file_name):
    base_name = input_file_name.replace(".txt", "")
    return f"Outputs/{base_name}_report.md"


def main():
    input_folder = "inputs"
    input_files = get_text_files(input_folder)
    batch_results = []

    print("Legal Risk Report Generator v2.7")
    print("--------------------------------")
    print("Input files found:", len(input_files))
    print("")

    for input_file in input_files:
        input_path = f"{input_folder}/{input_file}"
        output_path = build_output_file_name(input_file)

        contract_text = read_contract_file(input_path)
        risks = analyze_contract_text(contract_text)

        high_count, medium_count, low_count = calculate_risk_counts(risks)
        risk_score = calculate_risk_score(risks)
        overall_assessment = get_overall_assessment(high_count, medium_count)
        category_counts = calculate_category_counts(risks)

        report = generate_markdown_report(document, risks)
        save_markdown_report(report, output_path)

        batch_results.append({
            "file_name": input_file,
            "risk_count": len(risks),
            "high_count": high_count,
            "medium_count": medium_count,
            "low_count": low_count,
            "risk_score": risk_score,
            "overall_assessment": overall_assessment,
            "category_counts": category_counts
        })

        print("Analyzed:", input_file)
        print("Detected risks:", len(risks))
        print("Risk score:", risk_score)
        print("Output file:", output_path)
        print("---")

    batch_summary = generate_batch_summary_report(batch_results)
    batch_summary_path = "Outputs/batch_summary_report.md"
    save_markdown_report(batch_summary, batch_summary_path)

    print("")
    print("Batch summary generated successfully.")
    print("Output file:", batch_summary_path)


if __name__ == "__main__":
    main()