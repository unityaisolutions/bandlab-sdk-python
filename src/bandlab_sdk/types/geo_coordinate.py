# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GeoCoordinate"]


class GeoCoordinate(BaseModel):
    latitude: Optional[float] = None

    longitude: Optional[float] = None
