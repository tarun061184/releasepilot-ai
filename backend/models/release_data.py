from pydantic import BaseModel

class ReleaseData(BaseModel):
    open_critical: int
    open_high: int
    test_pass_rate: float
    failed_tests: int