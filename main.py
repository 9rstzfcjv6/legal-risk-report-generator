from data import document
from file_reader import read_contract_file, get_text_files
from input_analyzer import analyze_contract_text
from report_generator import generate_markdown_report
from export import save_markdown_report


def build_output_file_name(input_file_name):
    base_name = input_file_name.replace(".txt", "")
    return f"Outputs/{base_name}_report.md"


def main():
    input_folder = "inputs"

    input_files = get_text_files(input_folder)

    print("Legal Risk Report Generator v2.4")
    print("--------------------------------")
    print("Input files found:", len(input_files))
    print("")

    for input_file in input_files:
        input_path = f"{input_folder}/{input_file}"
        output_path = build_output_file_name(input_file)

        contract_text = read_contract_file(input_path)

        risks = analyze_contract_text(contract_text)

        report = generate_markdown_report(document, risks)

        save_markdown_report(report, output_path)

        print("Analyzed:", input_file)
        print("Detected risks:", len(risks))
        print("Output file:", output_path)
        print("---")


if __name__ == "__main__":
    main()