# Legal Risk Report Generator v2.0

## Overview

Legal Risk Report Generator v2.0 is a modular Python prototype designed to generate structured legal risk reports for technology, R&D and IP-related contracts.

The project focuses on risks commonly found in R&D collaboration agreements, including intellectual property ownership, confidentiality, AI training use, and publication approval.

This tool is part of a broader Legal AI Builder learning path focused on legal automation, AI governance, IP risk management and Legal Operations.

## Strategic Purpose

The purpose of this project is to demonstrate how legal reasoning can be translated into a structured and semi-automated workflow.

The tool transforms legal risk analysis into:

- structured data
- risk classification
- risk scoring
- recommendations
- ownership allocation
- deadline tracking
- status monitoring
- Markdown report generation

## Strategic LegalTech Value

This project is designed to demonstrate how legal, IP and AI governance workflows can be translated into structured software logic.

For legal and IP teams, the value of this type of tool is not only document review, but also workflow standardization. A structured risk report can help teams:

- identify recurring contractual risks
- prioritize high-risk issues before signature
- allocate ownership to the right legal, IP, data governance or R&D team
- create a repeatable review framework
- improve communication with business and technical stakeholders
- support early-stage Legal Operations automation

In a technology or MedTech environment, this type of workflow can be particularly useful for R&D collaboration agreements, supplier contracts, NDA review and AI-related data use restrictions.

## Features

- Structured contract information
- Legal risk database
- Risk classification by category
- Risk level assessment
- Weighted risk scoring
- Automatic overall assessment
- Recommended action per risk
- Owner, deadline, priority and status tracking
- Markdown report generation
- Modular Python architecture

## Project Structure

```text
02_legal_risk_report_generator/
├── main.py
├── data.py
├── risk_engine.py
├── report_generator.py
├── export.py
└── outputs/
    └── legal_risk_report.md
```

## File Roles

### `main.py`

Orchestrates the project. It imports the data, generates the report and exports the final Markdown file.

### `data.py`

Contains the structured contract data and legal risk items.

### `risk_engine.py`

Contains the legal decision logic, including risk counting, scoring, action generation and overall assessment.

### `report_generator.py`

Generates the Markdown legal risk report.

### `export.py`

Saves the generated report into the `outputs` folder.

### `outputs/`

Stores generated reports.

## How to Run

From the project folder, run:

```bash
python3 main.py
```

The generated report will be saved as:

```text
outputs/legal_risk_report.md
```

## Example Use Case

This prototype can support legal and IP teams reviewing R&D collaboration agreements by identifying and structuring key contractual risks before signature.

Example risks include:

- unclear ownership of foreground intellectual property
- missing confidentiality survival period
- unrestricted AI training use of confidential or technical data
- missing publication approval clause

## Current Version

Version: `v2.0`

Status: Prototype

## Future Improvements

Planned improvements include:

- Streamlit web interface
- user input form
- contract upload
- AI-assisted clause extraction
- automated risk detection
- DOCX and PDF export
- clause library
- risk dashboard
- integration with AI agent workflows

## Legal Disclaimer

This project is for educational and internal workflow prototyping purposes only. It does not constitute formal legal advice and should not be used as a substitute for review by a qualified legal professional.