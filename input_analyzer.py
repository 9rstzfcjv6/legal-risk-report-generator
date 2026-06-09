def analyze_contract_text(contract_text):
    detected_risks = []

    text = contract_text.lower()

    if "foreground ip" in text or "jointly owned" in text or "ownership" in text:
        detected_risks.append({
            "name": "Potential ambiguity in foreground IP ownership",
            "category": "Intellectual Property",
            "level": "High",
            "recommendation": "Clarify ownership of foreground IP, background IP and jointly developed results.",
            "owner": "IP / Legal Team",
            "deadline": "Before signature",
            "priority": "Urgent",
            "status": "To review"
        })

    if "confidential" in text and "termination" not in text:
        detected_risks.append({
            "name": "Potential missing confidentiality survival period",
            "category": "Confidentiality",
            "level": "Medium",
            "recommendation": "Add a survival clause specifying that confidentiality obligations continue after termination.",
            "owner": "Legal Team",
            "deadline": "Before negotiation closing",
            "priority": "Important",
            "status": "To clarify"
        })

    if "ai training" in text or "model training" in text or "machine learning" in text:
        detected_risks.append({
            "name": "Potential unrestricted AI training use",
            "category": "AI / Data Governance",
            "level": "High",
            "recommendation": "Prohibit use of confidential information, technical data or R&D outputs for AI model training without prior written consent.",
            "owner": "Legal / Data Governance Team",
            "deadline": "Before sharing technical data",
            "priority": "Urgent",
            "status": "To review"
        })

    if ("publication" in text or "publish" in text or "disclose" in text or "disclosure" in text) and "approval" not in text:
        detected_risks.append({
            "name": "Potential missing publication approval clause",
            "category": "R&D Governance",
            "level": "Medium",
            "recommendation": "Require prior written approval before publication or disclosure of research results.",
            "owner": "R&D / Legal Team",
            "deadline": "Before project launch",
            "priority": "Important",
            "status": "To clarify"
        })

    return detected_risks