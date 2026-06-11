import streamlit as st
import pandas as pd
from docx import Document
from export import convert_markdown_to_docx_bytes

from data import document
from file_reader import read_contract_file, get_text_files, read_docx_file
from input_analyzer import analyze_contract_text
from report_generator import generate_markdown_report, generate_batch_summary_report
from risk_engine import (
    calculate_risk_counts,
    calculate_risk_score,
    get_overall_assessment,
    calculate_category_counts
)


st.set_page_config(
    page_title="Legal Risk Report Generator",
    layout="wide"
)


def analyze_selected_contracts(selected_files, input_folder):
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

    return batch_results

def analyze_uploaded_contract(file_name, contract_text):
    risks = analyze_contract_text(contract_text)

    high_count, medium_count, low_count = calculate_risk_counts(risks)
    risk_score = calculate_risk_score(risks)
    overall_assessment = get_overall_assessment(high_count, medium_count)
    category_counts = calculate_category_counts(risks)

    report = generate_markdown_report(document, risks)

    return {
        "file_name": file_name,
        "risk_count": len(risks),
        "high_count": high_count,
        "medium_count": medium_count,
        "low_count": low_count,
        "risk_score": risk_score,
        "overall_assessment": overall_assessment,
        "category_counts": category_counts,
        "risks": risks,
        "report": report
    }

def read_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    if uploaded_file.name.endswith(".docx"):
        document = Document(uploaded_file)
        paragraphs = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                paragraphs.append(paragraph.text)

        return "\n".join(paragraphs)

    return ""

def build_overview_table(batch_results):
    rows = []

    for result in batch_results:
        rows.append({
            "Contract": result["file_name"],
            "Risk Score": result["risk_score"],
            "Risk Level": get_risk_level(result["risk_score"]),
            "Total Risks": result["risk_count"],
            "High": result["high_count"],
            "Medium": result["medium_count"],
            "Low": result["low_count"],
            "Assessment": result["overall_assessment"]
        })

    overview_df = pd.DataFrame(rows)

    if overview_df.empty:
        return overview_df

    return overview_df.sort_values(
        by="Risk Score",
        ascending=False
    ).reset_index(drop=True)


def get_highest_risk_contract(batch_results):
    if not batch_results:
        return "N/A"

    highest = max(batch_results, key=lambda result: result["risk_score"])
    return highest["file_name"]

def get_risk_level(risk_score):
    if risk_score >= 7:
        return "High"

    if risk_score >= 4:
        return "Medium"

    return "Low"

def get_base_file_name(file_name):
    return (
        file_name
        .replace(".txt", "")
        .replace(".docx", "")
        .replace(" ", "_")
    )
st.sidebar.title("Legal Risk Report Generator")
st.sidebar.markdown(
    """
    **Prototype type:** LegalTech / Legal Ops  
    **Focus:** IP, confidentiality, AI/data governance and R&D risk review  
    **Version:** v3.4 + DOCX Export Support
    """
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    **Strategic value**

    This prototype helps legal and innovation teams move from contract review
    to portfolio-level risk prioritization and contract playbook improvement.
    """
)

st.title("Legal Risk Report Generator")
st.caption("Rule-based LegalTech prototype for contract risk analysis, IP governance and AI/data risk review.")

st.markdown(
    """
    Analyze contract files, identify recurring legal risks, generate individual reports,
    produce a batch summary and convert recurring issues into contract playbook recommendations.
    """
)

input_folder = "inputs"
input_files = get_text_files(input_folder)

st.subheader("1. Choose Input Mode")

input_mode = st.radio(
    "How do you want to provide contracts?",
    ["Use existing files from inputs/", "Upload .txt or .docx contract files"]
)

batch_results = []

if input_mode == "Use existing files from inputs/":
    input_folder = "inputs"
    input_files = get_text_files(input_folder)

    st.markdown("### Existing Contract Files")
    st.write(f"Detected files in `inputs/`: **{len(input_files)}**")

    if input_files:
        selected_files = st.multiselect(
            "Select contracts to analyze:",
            input_files,
            default=input_files
        )

        analyze_button = st.button("Analyze selected existing contracts")

        if analyze_button:
            if not selected_files:
                st.warning("Please select at least one contract.")
            else:
                batch_results = analyze_selected_contracts(selected_files, input_folder)
                st.success("Analysis completed.")

    else:
        st.warning("No .txt files found in the inputs folder.")

else:
    uploaded_files = st.file_uploader(
        "Upload one or more .txt or .docx contract files:",
        type=["txt", "docx"],
        accept_multiple_files=True
)

    analyze_button = st.button("Analyze uploaded contracts")

    if analyze_button:
        if not uploaded_files:
            st.warning("Please upload at least one .txt contract.")
        else:
            for uploaded_file in uploaded_files:
                contract_text = read_uploaded_file(uploaded_file)
                result = analyze_uploaded_contract(uploaded_file.name, contract_text)
                batch_results.append(result)

            st.success("Uploaded contract analysis completed.")

if batch_results:
    total_contracts = len(batch_results)
    total_risks = sum(result["risk_count"] for result in batch_results)
    total_high_risks = sum(result["high_count"] for result in batch_results)
    highest_risk_contract = get_highest_risk_contract(batch_results)
    highest_risk_score = max(result["risk_score"] for result in batch_results)

    st.subheader("2. Portfolio Risk Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Contracts analyzed", total_contracts)
    col2.metric("Total risks detected", total_risks)
    col3.metric("High-risk issues", total_high_risks)
    col4.metric("Highest risk score", highest_risk_score)

    st.caption(f"Highest-risk contract: {highest_risk_contract}")

    overview_df = build_overview_table(batch_results)

    st.markdown("### Contract Overview Table")
    st.dataframe(overview_df, use_container_width=True)

    st.subheader("3. Individual Contract Reports")

    for result in batch_results:
        with st.expander(f"{result['file_name']} — Score: {result['risk_score']}"):
            st.write(f"Detected risks: **{result['risk_count']}**")
            st.write(f"High risks: **{result['high_count']}**")
            st.write(f"Medium risks: **{result['medium_count']}**")
            st.write(f"Low risks: **{result['low_count']}**")
            st.write(f"Overall assessment: **{result['overall_assessment']}**")

            st.markdown("### Individual Report")
            st.markdown(result["report"])

            base_file_name = get_base_file_name(result["file_name"])

            base_file_name = get_base_file_name(result["file_name"])

            st.download_button(
                label=f"Download {result['file_name']} report as Markdown",
                data=result["report"],
                file_name=f"{base_file_name}_report.md",
                mime="text/markdown"
            )

            docx_report = convert_markdown_to_docx_bytes(result["report"])

            docx_report = convert_markdown_to_docx_bytes(result["report"])

            st.download_button(
                label=f"Download {result['file_name']} report as DOCX",
                data=docx_report,
                file_name=f"{base_file_name}_report.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

    st.subheader("4. Portfolio Summary")

    batch_summary = generate_batch_summary_report(batch_results)

    st.markdown(batch_summary)

    st.download_button(
        label="Download batch summary report as Markdown",
        data=batch_summary,
        file_name="batch_summary_report.md",
        mime="text/markdown"
    )

    batch_docx_report = convert_markdown_to_docx_bytes(batch_summary)

    st.download_button(
        label="Download batch summary report as DOCX",
        data=batch_docx_report,
        file_name="batch_summary_report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )