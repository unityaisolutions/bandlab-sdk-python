# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Location", "Coordinates"]


class Coordinates(BaseModel):
    latitude: Optional[float] = None

    longitude: Optional[float] = None


class Location(BaseModel):
    city: Optional[str] = None

    coordinates: Optional[Coordinates] = FieldInfo(alias="Coordinates", default=None)

    country: Optional[str] = None
