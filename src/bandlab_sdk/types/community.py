# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .type import Type
from .creator import Creator
from .picture import Picture
from .._models import BaseModel
from .community_counters import CommunityCounters
from .group_member_summary import GroupMemberSummary

__all__ = ["Community"]


class Community(BaseModel):
    name: str

    id: Optional[str] = None

    about: Optional[str] = None

    counters: Optional[CommunityCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    creator: Optional[Creator] = None

    is_comments_enabled: Optional[bool] = FieldInfo(alias="isCommentsEnabled", default=None)

    members: Optional[List[GroupMemberSummary]] = None

    picture: Optional[Picture] = None

    type: Optional[Type] = None

    username: Optional[str] = None
