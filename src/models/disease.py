from typing import List, Optional, Union
from pydantic import BaseModel, Field

class Symptom(BaseModel):
    """A model representing a symptom of a disease with its metrics and thresholds."""
    name: str = Field(..., description="The name of the symptom")
    description: str = Field(..., description="A detailed description of the symptom")
    metric: str = Field(..., description="The objective metric used to measure the symptom (e.g., temperature, heart rate, skill level)")
    normal_min: float = Field(..., description="The minimum value considered normal for this metric")
    normal_max: float = Field(..., description="The maximum value considered normal for this metric")
    symptomatic_min: float = Field(..., description="The minimum value at which the symptom is considered present")
    symptomatic_max: float = Field(..., description="The maximum value at which the symptom is considered present")
    emergency_min: Optional[float] = Field(None, description="The minimum value at which immediate medical attention is required")
    emergency_max: Optional[float] = Field(None, description="The maximum value at which immediate medical attention is required")
    duration_min: Optional[float] = Field(None, description="Minimum typical duration of the symptom in hours")
    duration_max: Optional[float] = Field(None, description="Maximum typical duration of the symptom in hours")

class Disease(BaseModel):
    """A model representing a disease with its associated symptoms."""
    name: str = Field(..., description="The name of the disease")
    description: str = Field(..., description="A detailed description of the disease")
    symptoms: List[Symptom] = Field(..., description="List of symptoms associated with the disease")
    sources: List[str] = Field(default_factory=list, description="List of source URLs for the disease information") 