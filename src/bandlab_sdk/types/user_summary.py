# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .picture import Picture
from .._models import BaseModel
from .user_counters import UserCounters

__all__ = ["UserSummary"]


class UserSummary(BaseModel):
    id: Optional[str] = None

    counters: Optional[UserCounters] = None

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    name: Optional[str] = None

    picture: Optional[Picture] = None

    username: Optional[str] = None
