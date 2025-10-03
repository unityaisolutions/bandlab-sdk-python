# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..genre_param import GenreParam
from ..skill_param import SkillParam
from ..picture_param import PictureParam
from ..location_param import LocationParam
from ..user_counters_param import UserCountersParam

__all__ = ["MemberUpdateParams"]


class MemberUpdateParams(TypedDict, total=False):
    community_id: Required[Annotated[str, PropertyInfo(alias="communityId")]]

    id: str

    about: str

    badges: SequenceNotStr[str]

    counters: UserCountersParam

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    genres: Iterable[GenreParam]

    is_tippable: Annotated[bool, PropertyInfo(alias="isTippable")]

    is_verified: Annotated[bool, PropertyInfo(alias="isVerified")]

    location: LocationParam

    name: str

    picture: PictureParam

    role: Literal["None", "Member", "Admin", "Owner"]

    skills: Iterable[SkillParam]

    username: str
