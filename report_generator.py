from risk_engine import (
    calculate_risk_counts,
    calculate_risk_score,
    get_action_for_risk,
    get_overall_assessment
)


def generate_markdown_report(document, risks):
    high_count, medium_count, low_count = calculate_risk_counts(risks)
    risk_score = calculate_risk_score(risks)
    overall_assessment = get_overall_assessment(high_count, medium_count)

    report = ""

    report += f"# {document['version']}\n\n"
    report += "## Document Information\n\n"
    report += f"- **Title:** {document['title']}\n"
    report += f"- **Type:** {document['type']}\n\n"

    report += "## Executive Summary\n\n"
    report += f"- **High risks:** {high_count}\n"
    report += f"- **Medium risks:** {medium_count}\n"
    report += f"- **Low risks:** {low_count}\n"
    report += f"- **Total risk score:** {risk_score}\n"
    report += f"- **Overall assessment:** {overall_assessment}\n\n"

    report += "## Risk Matrix\n\n"
    report += "| Risk | Category | Level | Owner | Deadline | Priority | Status |\n"
    report += "|---|---|---|---|---|---|---|\n"

    for risk in risks:
        report += (
            f"| {risk['name']} "
            f"| {risk['category']} "
            f"| {risk['level']} "
            f"| {risk['owner']} "
            f"| {risk['deadline']} "
            f"| {risk['priority']} "
            f"| {risk['status']} |\n"
        )

    report += "\n## Detailed Recommendations\n\n"

    for risk in risks:
        action = get_action_for_risk(risk)

        report += f"### {risk['name']}\n\n"
        report += f"- **Category:** {risk['category']}\n"
        report += f"- **Level:** {risk['level']}\n"
        report += f"- **Recommendation:** {risk['recommendation']}\n"
        report += f"- **Action:** {action}\n"
        report += f"- **Owner:** {risk['owner']}\n"
        report += f"- **Deadline:** {risk['deadline']}\n"
        report += f"- **Priority:** {risk['priority']}\n"
        report += f"- **Status:** {risk['status']}\n\n"

    report += "## Legal Disclaimer\n\n"
    report += (
        "This report is generated for internal legal workflow support only. "
        "It does not constitute formal legal advice and should be reviewed by a qualified legal professional before use.\n"
    )

    return report
