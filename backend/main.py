from fastapi import FastAPI

from models.release_data import ReleaseData

from agents.defect_agent import analyze_defects
from agents.test_agent import analyze_tests
from agents.release_agent import release_decision
from agents.executive_summary_agent import generate_summary
from agents.gemini_release_agent import generate_ai_release_summary
from agents.risk_score_agent import calculate_risk_score

app = FastAPI(
    title="ReleasePilot AI",
    description="AI-Powered Release Governance Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "ReleasePilot AI Running"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.post("/analyze")
def analyze_release(data: ReleaseData):

    # Defect Analysis Agent
    defect_result = analyze_defects(
        data.open_critical,
        data.open_high
    )

    # Test Analysis Agent
    test_result = analyze_tests(
        data.test_pass_rate,
        data.failed_tests
    )

    # Release Decision Agent
    final_result = release_decision(
        defect_result,
        test_result
    )

    # Executive Summary Agent
    executive_summary = generate_summary(
        defect_result,
        test_result,
        final_result
    )

    # Gemini AI Agent
    ai_release_assessment = generate_ai_release_summary(
        defect_result,
        test_result,
        final_result
    )

    risk_metrics = calculate_risk_score(
        data.open_critical,
        data.open_high,
        data.test_pass_rate,
        data.failed_tests
    )

    return {
        "defect_analysis": defect_result,
        "test_analysis": test_result,
        "release_decision": final_result,
        "executive_summary": executive_summary,
        "risk_metrics": risk_metrics,
        "ai_release_assessment": ai_release_assessment
    }