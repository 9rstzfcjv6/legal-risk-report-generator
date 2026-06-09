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