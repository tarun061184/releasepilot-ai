def generate_summary(
        defect_result,
        test_result,
        release_result):

    return f"""
Release Readiness Summary

Decision: {release_result['decision']}

Defect Risk:
{defect_result['reason']}

Testing Risk:
{test_result['reason']}

Overall Risk Score:
{release_result['overall_risk_score']}

Recommendation:
The release team should review the identified risks before deployment.
"""