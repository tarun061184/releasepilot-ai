from agents.gemini_release_agent import generate_ai_release_summary

result = generate_ai_release_summary(
    {
        "risk": "HIGH",
        "score": 90,
        "reason": "2 critical defects remain open."
    },
    {
        "risk": "LOW",
        "score": 20,
        "reason": "Test execution results are healthy."
    },
    {
        "decision": "NO-GO",
        "overall_risk_score": 90
    }
)

print(result)