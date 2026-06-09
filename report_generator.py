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


def generate_batch_summary_report(batch_results):
    total_contracts = len(batch_results)
    total_risks = 0
    escalation_contracts = []
    highest_risk_contract = None
    highest_risk_score = -1

    report = ""

    report += "# Batch Summary Report\n\n"
    report += "## Executive Summary\n\n"
    report += f"- **Total contracts reviewed:** {total_contracts}\n"

    for result in batch_results:
        total_risks += result["risk_count"]

        if result["risk_score"] > highest_risk_score:
            highest_risk_score = result["risk_score"]
            highest_risk_contract = result["file_name"]

        if result["high_count"] > 0:
            escalation_contracts.append(result["file_name"])

    report += f"- **Total risks detected:** {total_risks}\n"
    report += f"- **Highest-risk contract:** {highest_risk_contract}\n"
    report += f"- **Highest risk score:** {highest_risk_score}\n"
    report += f"- **Contracts requiring legal escalation:** {len(escalation_contracts)}\n\n"

    report += "## Priority Recommendation\n\n"

    if highest_risk_contract:
        report += (
            f"Priority should be given to **{highest_risk_contract}** because it has "
            f"the highest risk score in the reviewed contract batch "
            f"(**{highest_risk_score}** points). This contract should be reviewed first "
            f"by the legal or IP team before lower-risk contracts.\n\n"
        )
    else:
        report += "No priority recommendation available because no contract was analyzed.\n\n"

    report += "## Ranking Logic\n\n"
    report += (
        "Contracts are ranked based on their total risk score. "
        "High risks count for 3 points, medium risks count for 2 points, "
        "and low risks count for 1 point. Contracts with at least one high-risk issue "
        "should generally be escalated for legal review before signature.\n\n"
    )

    report += "## Contract Risk Overview\n\n"
    report += "| Contract | High | Medium | Low | Total Risks | Risk Score | Overall Assessment |\n"
    report += "|---|---:|---:|---:|---:|---:|---|\n"

    for result in batch_results:
        report += (
            f"| {result['file_name']} "
            f"| {result['high_count']} "
            f"| {result['medium_count']} "
            f"| {result['low_count']} "
            f"| {result['risk_count']} "
            f"| {result['risk_score']} "
            f"| {result['overall_assessment']} |\n"
        )

    report += "\n## Contracts Requiring Legal Escalation\n\n"

    if escalation_contracts:
        for contract in escalation_contracts:
            report += f"- {contract}\n"
    else:
        report += "No contracts require legal escalation.\n"

    report += "\n## Strategic Use\n\n"
    report += (
        "This batch summary helps legal, IP and R&D teams prioritize contract review workload, "
        "identify high-risk agreements and allocate review resources more efficiently.\n"
    )

    return report