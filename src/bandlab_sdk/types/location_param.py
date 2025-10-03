# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LocationParam", "Coordinates"]


class Coordinates(TypedDict, total=False):
    latitude: float

    longitude: float


class LocationParam(TypedDict, total=False):
    city: str

    coordinates: Annotated[Coordinates, PropertyInfo(alias="Coordinates")]

    country: str
