# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .geo_coordinate_param import GeoCoordinateParam

__all__ = ["LocationParam"]


class LocationParam(TypedDict, total=False):
    city: str

    coordinates: Annotated[GeoCoordinateParam, PropertyInfo(alias="Coordinates")]

    country: str
