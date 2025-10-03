# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .type import Type
from .._utils import PropertyInfo
from .creator_param import CreatorParam
from .picture_param import PictureParam
from .community_counters_param import CommunityCountersParam
from .group_member_summary_param import GroupMemberSummaryParam

__all__ = ["CommunityCreateParams"]


class CommunityCreateParams(TypedDict, total=False):
    name: Required[str]

    id: str

    about: str

    counters: CommunityCountersParam

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    creator: CreatorParam

    is_comments_enabled: Annotated[bool, PropertyInfo(alias="isCommentsEnabled")]

    members: Iterable[GroupMemberSummaryParam]

    picture: PictureParam

    type: Type

    username: str
