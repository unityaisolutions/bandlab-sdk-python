# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .geo_coordinate import GeoCoordinate

__all__ = ["Location"]


class Location(BaseModel):
    city: Optional[str] = None

    coordinates: Optional[GeoCoordinate] = FieldInfo(alias="Coordinates", default=None)

    country: Optional[str] = None
