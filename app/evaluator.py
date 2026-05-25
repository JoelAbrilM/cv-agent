import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

from app.schemas import EvaluationResult

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def evaluate_cv(
    cv_text: str,
    job_requirements: str
) -> EvaluationResult:

    prompt = f"""
You are an expert technical recruiter.

Compare the candidate CV against the job requirements.

Rules:
- Be strict but fair.
- Do not invent experience.
- If requirements are missing, mark them as gaps.
- Return whether the candidate applies or does not apply.
- Score from 0 to 100.
- A candidate applies only if score is 70 or higher and there are no critical missing requirements.

You MUST respond ONLY in valid JSON.

JSON FORMAT:
{{
    "applies": true,
    "score": 85,
    "verdict": "Candidate meets most requirements.",
    "strengths": [
        "Python experience",
        "API development"
    ],
    "gaps": [
        "No AWS experience"
    ],
    "recommendation": "Proceed to technical interview."
}}

CV:
{cv_text}

JOB REQUIREMENTS:
{job_requirements}
"""

    response = model.generate_content(prompt)

    raw_response = response.text.strip()

    # Limpia markdown si Gemini devuelve ```json
    raw_response = raw_response.replace(
        "```json", ""
    ).replace(
        "```", ""
    ).strip()

    data = json.loads(raw_response)

    return EvaluationResult(**data)