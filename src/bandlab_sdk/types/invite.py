# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .type import Type
from .picture import Picture
from .._models import BaseModel
from .song_summary import SongSummary
from .user_summary import UserSummary
from .band_counters import BandCounters
from .community_counters import CommunityCounters

__all__ = ["Invite", "Band", "Community"]


class Band(BaseModel):
    id: Optional[str] = None

    counters: Optional[BandCounters] = None

    name: Optional[str] = None

    picture: Optional[Picture] = None

    username: Optional[str] = None


class Community(BaseModel):
    id: Optional[str] = None

    about: Optional[str] = None

    counters: Optional[CommunityCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    name: Optional[str] = None

    picture: Optional[Picture] = None

    type: Optional[Type] = None

    username: Optional[str] = None


class Invite(BaseModel):
    message: str

    id: Optional[str] = None

    band: Optional[Band] = None

    community: Optional[Community] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    email: Optional[str] = None

    is_user_request: Optional[bool] = FieldInfo(alias="isUserRequest", default=None)

    sender: Optional[UserSummary] = None

    song: Optional[SongSummary] = None

    text: Optional[str] = None

    type: Optional[
        Literal[
            "RequestToBand",
            "RequestToSong",
            "RequestToCommunity",
            "InviteToBand",
            "InviteToSong",
            "InviteToCommunity",
            "ExternalInviteToBand",
            "ExternalInviteToSong",
            "ExternalInviteToBandLab",
        ]
    ] = None

    user: Optional[UserSummary] = None
