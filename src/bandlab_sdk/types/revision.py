# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .genre import Genre
from .creator import Creator
from .._models import BaseModel
from .mastering import Mastering
from .audio_sample import AudioSample
from .song_summary import SongSummary
from .revision_counters import RevisionCounters
from .collections.client_id import ClientID

__all__ = ["Revision", "AuxChannel", "AuxChannelEffect"]


class AuxChannelEffect(BaseModel):
    bypass: Optional[bool] = None

    params: Optional[object] = None

    slug: Optional[str] = None


class AuxChannel(BaseModel):
    id: Optional[str] = None

    effects: Optional[List[AuxChannelEffect]] = None

    preset: Optional[str] = None

    return_level: Optional[float] = FieldInfo(alias="returnLevel", default=None)


class Revision(BaseModel):
    id: Optional[str] = None

    aux_channels: Optional[List[AuxChannel]] = FieldInfo(alias="auxChannels", default=None)

    client_id: Optional[ClientID] = FieldInfo(alias="clientId", default=None)

    counters: Optional[RevisionCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    creator: Optional[Creator] = None

    description: Optional[str] = None

    genres: Optional[List[Genre]] = None

    is_fork: Optional[bool] = FieldInfo(alias="isFork", default=None)

    is_public: Optional[bool] = FieldInfo(alias="isPublic", default=None)

    key: Optional[str] = None

    mastering: Optional[Mastering] = None

    mixdown: Optional[AudioSample] = None

    modified_on: Optional[datetime] = FieldInfo(alias="modifiedOn", default=None)

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)

    post_id: Optional[str] = FieldInfo(alias="postId", default=None)

    samples: Optional[List[AudioSample]] = None

    song: Optional[SongSummary] = None

    stamp: Optional[str] = None

    tracks: Optional[List[AudioSample]] = None
