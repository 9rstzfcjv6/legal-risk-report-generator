def find_evidence_snippet(contract_text, keywords):
    paragraphs = contract_text.split("\n")

    for keyword in keywords:
        for paragraph in paragraphs:
            clean_paragraph = paragraph.strip()

            if not clean_paragraph:
                continue

            if keyword.lower() in clean_paragraph.lower():
                return clean_paragraph

    return "No specific evidence snippet identified."

def check_clause_presence(contract_text):
    lower_text = contract_text.lower()

    checklist = {
        "Foreground IP ownership": any(
            keyword in lower_text
            for keyword in ["foreground ip", "project-generated ip", "jointly developed", "derivative works"]
        ),
        "Background IP reservation": any(
            keyword in lower_text
            for keyword in ["background ip", "pre-existing intellectual property", "pre-existing ip"]
        ),
        "Confidentiality survival": any(
            keyword in lower_text
            for keyword in ["survive termination", "survive expiration", "confidentiality obligations shall survive", "post-termination"]
        ),
        "AI / data use restriction": any(
            keyword in lower_text
            for keyword in ["ai training", "model training", "machine learning", "secondary use", "fine-tuning", "training corpus"]
        ),
        "Publication approval": any(
            keyword in lower_text
            for keyword in ["publication approval", "prior written approval", "publish", "case study", "public disclosure"]
        ),
        "Audit / records": any(
            keyword in lower_text
            for keyword in ["audit", "records", "development notes", "version history"]
        ),
        "Third-party IP warranty": any(
            keyword in lower_text
            for keyword in ["third-party rights", "third party rights", "infringe", "infringement"]
        )
    }

    return checklist

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
            "status": "To review",
            "evidence": find_evidence_snippet(
                contract_text,
                ["foreground IP", "jointly developed", "derivative works", "improvements"]
            ),
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
            "status": "To clarify",
            "evidence": find_evidence_snippet(
                contract_text,
                ["confidentiality", "termination", "expiration", "survive"]
            ),
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
            "status": "To review",
            "evidence": find_evidence_snippet(
                contract_text,
                ["software logs", "datasets", "AI training", "model training", "secondary use", "machine learning"]
            ),
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
            "status": "To clarify",
            "evidence": find_evidence_snippet(
                contract_text,
                ["publication", "case studies", "disclosure", "research results", "public"]
            ),
        })

    return detected_risks