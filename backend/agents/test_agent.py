def analyze_tests(test_pass_rate, failed_tests):

    if test_pass_rate < 80:
        return {
            "risk": "HIGH",
            "score": 90,
            "reason": f"Test pass rate is only {test_pass_rate}%."
        }

    if failed_tests > 10:
        return {
            "risk": "MEDIUM",
            "score": 60,
            "reason": f"{failed_tests} tests are failing."
        }

    return {
        "risk": "LOW",
        "score": 20,
        "reason": "Test execution results are healthy."
    }