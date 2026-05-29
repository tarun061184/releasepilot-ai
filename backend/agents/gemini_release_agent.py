import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_release_summary(
        defect_result,
        test_result,
        release_result):

    prompt = f"""
You are a Senior Release Governance Manager.

Analyze the following release readiness data.

Provide:

1. Executive Summary
2. Key Risks
3. Deployment Recommendation
4. Next Actions

IMPORTANT:
- Return plain text only
- No markdown
- No asterisks (*)
- No hashtags (#)
- No bullet formatting
- Keep response concise and professional

Defect Analysis:
{defect_result}

Test Analysis:
{test_result}

Release Decision:
{release_result}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text