def release_decision(defect_result, test_result):

    max_score = max(
        defect_result["score"],
        test_result["score"]
    )

    if max_score >= 90:
        decision = "NO-GO"
    elif max_score >= 60:
        decision = "CONDITIONAL GO"
    else:
        decision = "GO"

    return {
        "decision": decision,
        "overall_risk_score": max_score
    }