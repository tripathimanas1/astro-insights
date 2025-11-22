from pydantic import BaseModel, Field, validator
from datetime import date, time
from typing import Optional, Literal


class InsightRequest(BaseModel):
    name: str = Field(..., example="Ritika")
    birth_date: date = Field(..., example="1995-08-20")
    birth_time: Optional[time] = Field(None, example="14:30")
    birth_place: Optional[str] = Field(None, example="Jaipur, India")
    language: Literal["en", "hi"] = Field("en", description="Preferred language of response")
    date_for: Optional[date] = Field(
        None,
        description="Date for which the daily insight is requested. Defaults to today on server."
    )


class InsightResponse(BaseModel):
    zodiac: str
    insight: str
    language: str
    date_for: date
    personalization_score: float


class ErrorResponse(BaseModel):
    detail: str
