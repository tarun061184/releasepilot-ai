def analyze_defects(open_critical, open_high):

    if open_critical > 0:
        return {
            "risk": "HIGH",
            "score": 90,
            "reason": f"{open_critical} critical defects remain open."
        }

    if open_high > 5:
        return {
            "risk": "MEDIUM",
            "score": 60,
            "reason": f"{open_high} high-priority defects remain open."
        }

    return {
        "risk": "LOW",
        "score": 20,
        "reason": "No critical defects and acceptable high-priority defect count."
    }