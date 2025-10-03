# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UserCounters"]


class UserCounters(BaseModel):
    bands: Optional[int] = None

    collections: Optional[int] = None

    followers: Optional[int] = None

    following: Optional[int] = None
