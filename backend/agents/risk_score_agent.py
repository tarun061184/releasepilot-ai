def calculate_risk_score(
        open_critical,
        open_high,
        test_pass_rate,
        failed_tests):

    score = 0

    score += open_critical * 25
    score += open_high * 5
    score += failed_tests * 2

    if test_pass_rate < 95:
        score += int(95 - test_pass_rate)

    score = min(score, 100)

    confidence = max(100 - score, 5)

    return {
        "risk_score": score,
        "confidence": confidence
    }