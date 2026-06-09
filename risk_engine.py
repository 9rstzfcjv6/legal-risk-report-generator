def calculate_risk_counts(risks):
    high_count = 0
    medium_count = 0
    low_count = 0

    for risk in risks:
        if risk["level"] == "High":
            high_count = high_count + 1
        elif risk["level"] == "Medium":
            medium_count = medium_count + 1
        else:
            low_count = low_count + 1

    return high_count, medium_count, low_count


def calculate_risk_score(risks):
    risk_score = 0

    for risk in risks:
        if risk["level"] == "High":
            risk_score = risk_score + 3
        elif risk["level"] == "Medium":
            risk_score = risk_score + 2
        else:
            risk_score = risk_score + 1

    return risk_score


def get_action_for_risk(risk):
    if risk["level"] == "High":
        return "Escalate to legal team before signature."
    elif risk["level"] == "Medium":
        return "Negotiate clause clarification."
    else:
        return "Standard monitoring."


def get_overall_assessment(high_count, medium_count):
    if high_count > 0:
        return "High-risk contract. Legal escalation required."
    elif medium_count > 0:
        return "Medium-risk contract. Negotiation recommended."
    else:
        return "Low-risk contract. Standard review sufficient."
def calculate_category_counts(risks):
    category_counts = {}

    for risk in risks:
        category = risk["category"]

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] = category_counts[category] + 1

    return category_counts

def generate_category_insights(category_counts):
    insights = []

    if category_counts.get("Intellectual Property", 0) > 0:
        insights.append(
            "Intellectual Property risks appear in the reviewed contract batch. "
            "This suggests that ownership of foreground IP, background IP and jointly developed results should be clarified and standardized in R&D agreements."
        )

    if category_counts.get("Confidentiality", 0) > 0:
        insights.append(
            "Confidentiality risks appear in the reviewed contract batch. "
            "This suggests that confidentiality survival periods and post-termination obligations should be reviewed systematically."
        )

    if category_counts.get("AI / Data Governance", 0) > 0:
        insights.append(
            "AI / Data Governance risks appear in the reviewed contract batch. "
            "This suggests that restrictions on AI training use, model improvement and secondary use of technical data should be added to the contract review playbook."
        )

    if category_counts.get("R&D Governance", 0) > 0:
        insights.append(
            "R&D Governance risks appear in the reviewed contract batch. "
            "This suggests that publication approval, research disclosure and project governance clauses should be standardized before project launch."
        )

    if not insights:
        insights.append(
            "No recurring strategic risk category was identified in the reviewed contract batch."
        )

    return insights

def generate_portfolio_action_plan(batch_results):
    action_plan = {}

    for result in batch_results:
        file_name = result["file_name"]

        for risk in result["risks"]:
            owner = risk["owner"]

            if owner not in action_plan:
                action_plan[owner] = []

            action_plan[owner].append({
                "contract": file_name,
                "risk": risk["name"],
                "priority": risk["priority"],
                "deadline": risk["deadline"],
                "status": risk["status"]
            })
    for owner in action_plan:
        action_plan[owner] = sort_actions_by_priority(action_plan[owner])

    return action_plan

def sort_actions_by_priority(actions):
    priority_order = {
        "Urgent": 1,
        "Important": 2,
        "Standard": 3
    }

    return sorted(
        actions,
        key=lambda action: priority_order.get(action["priority"], 99)
    )

def generate_contract_playbook_recommendations(category_counts):
    recommendations = []

    if category_counts.get("Intellectual Property", 0) > 0:
        recommendations.append(
            "Add a standard foreground IP ownership clause to R&D collaboration agreements, clearly distinguishing background IP, foreground IP and jointly developed results."
        )

    if category_counts.get("Confidentiality", 0) > 0:
        recommendations.append(
            "Add a standard confidentiality survival clause specifying that confidentiality obligations continue after termination or expiration of the agreement."
        )

    if category_counts.get("AI / Data Governance", 0) > 0:
        recommendations.append(
            "Add a standard AI training-use restriction clause prohibiting the use of confidential information, technical data or R&D outputs for model training without prior written consent."
        )

    if category_counts.get("R&D Governance", 0) > 0:
        recommendations.append(
            "Add a standard publication approval clause requiring prior written approval before publication or disclosure of research results."
        )

    if not recommendations:
        recommendations.append(
            "No contract playbook recommendation was generated because no recurring risk category was detected."
        )

    return recommendations