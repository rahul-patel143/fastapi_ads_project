from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class MetricsFilter(BaseModel):
    start_date: Optional[date] = Field(None, description="Start date for filtering (YYYY-MM-DD)")
    end_date: Optional[date] = Field(None, description="End date for filtering (YYYY-MM-DD)")
    region: Optional[str] = None
    platform: Optional[str] = None

class AdMetricsResponse(BaseModel):
    date: date
    region: str
    platform: str
    age_group: str
    gender: str
    placement: str
    device_type: str
    impressions: int
    clicks: int
    cost: float
    conversions: int
    likes: int
