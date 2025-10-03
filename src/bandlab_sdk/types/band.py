# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .genre import Genre
from .creator import Creator
from .picture import Picture
from .._models import BaseModel
from .band_counters import BandCounters
from .group_member_summary import GroupMemberSummary

__all__ = ["Band"]


class Band(BaseModel):
    name: str

    id: Optional[str] = None

    about: Optional[str] = None

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    counters: Optional[BandCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    creator: Optional[Creator] = None

    genres: Optional[List[Genre]] = None

    is_open: Optional[bool] = FieldInfo(alias="isOpen", default=None)

    members: Optional[List[GroupMemberSummary]] = None

    picture: Optional[Picture] = None

    username: Optional[str] = None
