# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..genre import Genre
from ..skill import Skill
from ..picture import Picture
from ..._models import BaseModel
from ..location import Location
from ..user_counters import UserCounters

__all__ = ["GroupMember"]


class GroupMember(BaseModel):
    id: Optional[str] = None

    about: Optional[str] = None

    badges: Optional[List[str]] = None

    counters: Optional[UserCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    genres: Optional[List[Genre]] = None

    is_tippable: Optional[bool] = FieldInfo(alias="isTippable", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    location: Optional[Location] = None

    name: Optional[str] = None

    picture: Optional[Picture] = None

    role: Optional[Literal["None", "Member", "Admin", "Owner"]] = None

    skills: Optional[List[Skill]] = None

    username: Optional[str] = None
