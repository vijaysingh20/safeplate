from pydantic import BaseModel, ConfigDict, Field
from datetime import date


class RestaurantRecord(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    restaurant_id: str = Field(pattern=r"^RST-[0-9]{3}$")
    name: str = Field(min_length=1)
    city: str = Field(min_length=1)
    address: str = Field(min_length=1)
    cuisine: str = Field(min_length=1)


class InspectionRecord(BaseModel):
    inspection_id: str = Field(pattern=r"^INS-[0-9]{3}$")
    restaurant_id: str = Field(pattern=r"^RST-[0-9]{3}$")
    inspection_date: date
    score: int = Field(ge=0, le=100)
    critical_violations: int = Field(ge=0)