# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .genre_param import GenreParam
from .creator_param import CreatorParam
from .picture_param import PictureParam
from .band_counters_param import BandCountersParam
from .group_member_summary_param import GroupMemberSummaryParam

__all__ = ["BandCreateParams"]


class BandCreateParams(TypedDict, total=False):
    name: Required[str]

    id: str

    about: str

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]

    counters: BandCountersParam

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    creator: CreatorParam

    genres: Iterable[GenreParam]

    is_open: Annotated[bool, PropertyInfo(alias="isOpen")]

    members: Iterable[GroupMemberSummaryParam]

    picture: PictureParam

    username: str
