from pydantic import BaseModel
from typing import List


class EvaluationResult(BaseModel):
    applies: bool
    score: int
    verdict: str
    strengths: List[str]
    gaps: List[str]
    recommendation: str