from pydantic import BaseModel, Field


class HouseFeatures(BaseModel):
    MedInc: float = Field(
        gt=0,
        description="Median income of the neighbourhood"
    )

    HouseAge: float = Field(
        ge=0,
        description="Average age of the houses"
    )

    AveRooms: float = Field(
        gt=0,
        description="Average number of rooms"
    )

    AveBedrms: float = Field(
        gt=0,
        description="Average number of bedrooms"
    )

    Population: float = Field(
        gt=0,
        description="Population of the block"
    )

    AveOccup: float = Field(
        gt=0,
        description="Average occupants per household"
    )

    Latitude: float = Field(
        ge=32,
        le=42,
        description="Latitude of the location"
    )

    Longitude: float = Field(
        ge=-125,
        le=-14,
        description="Longitude of the location"
    )