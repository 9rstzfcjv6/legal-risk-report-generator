import streamlit as st

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


def build_output_file_name(input_file_name):
    base_name = input_file_name.replace(".txt", "")
    return f"Outputs/{base_name}_report.md"


st.set_page_config(
    page_title="Legal Risk Report Generator",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Legal Risk Report Generator")
st.caption("Rule-based LegalTech prototype for contract risk analysis, IP governance and AI/data risk review.")

st.markdown(
    """
    This tool analyzes contract text files and generates legal risk reports,
    including risk scoring, category insights, action plans and contract playbook recommendations.
    """
)

input_folder = "inputs"
input_files = get_text_files(input_folder)

st.subheader("Available Contract Files")
st.write(f"Detected files: **{len(input_files)}**")

if input_files:
    selected_files = st.multiselect(
        "Select contracts to analyze:",
        input_files,
        default=input_files
    )

    if st.button("Analyze selected contracts"):
        batch_results = []

        for input_file in selected_files:
            input_path = f"{input_folder}/{input_file}"

            contract_text = read_contract_file(input_path)
            risks = analyze_contract_text(contract_text)

            high_count, medium_count, low_count = calculate_risk_counts(risks)
            risk_score = calculate_risk_score(risks)
            overall_assessment = get_overall_assessment(high_count, medium_count)
            category_counts = calculate_category_counts(risks)

            report = generate_markdown_report(document, risks)

            batch_results.append({
                "file_name": input_file,
                "risk_count": len(risks),
                "high_count": high_count,
                "medium_count": medium_count,
                "low_count": low_count,
                "risk_score": risk_score,
                "overall_assessment": overall_assessment,
                "category_counts": category_counts,
                "risks": risks,
                "report": report
            })

        st.success("Analysis completed.")

        st.subheader("Contract Risk Overview")

        for result in batch_results:
            with st.expander(f"{result['file_name']} — Score: {result['risk_score']}"):
                st.write(f"Detected risks: **{result['risk_count']}**")
                st.write(f"High risks: **{result['high_count']}**")
                st.write(f"Medium risks: **{result['medium_count']}**")
                st.write(f"Low risks: **{result['low_count']}**")
                st.write(f"Overall assessment: **{result['overall_assessment']}**")

                st.markdown("### Individual Report")
                st.markdown(result["report"])

                st.download_button(
                    label=f"Download {result['file_name']} report",
                    data=result["report"],
                    file_name=f"{result['file_name'].replace('.txt', '')}_report.md",
                    mime="text/markdown"
                )

        if batch_results:
            batch_summary = generate_batch_summary_report(batch_results)

            st.subheader("Batch Summary Report")
            st.markdown(batch_summary)

            st.download_button(
                label="Download batch summary report",
                data=batch_summary,
                file_name="batch_summary_report.md",
                mime="text/markdown"
            )

else:
    st.warning("No .txt files found in the inputs folder.")