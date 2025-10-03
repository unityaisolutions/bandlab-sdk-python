# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .lyrics import Lyrics
from ..creator import Creator
from ..._models import BaseModel
from ..audio_sample import AudioSample
from ..revision_counters import RevisionCounters
from ..collections.client_id import ClientID

__all__ = ["RevisionSummary"]


class RevisionSummary(BaseModel):
    id: Optional[str] = None

    client_id: Optional[ClientID] = FieldInfo(alias="clientId", default=None)

    counters: Optional[RevisionCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    creator: Optional[Creator] = None

    description: Optional[str] = None

    is_fork: Optional[bool] = FieldInfo(alias="isFork", default=None)

    is_public: Optional[bool] = FieldInfo(alias="isPublic", default=None)

    lyrics: Optional[Lyrics] = None

    mixdown: Optional[AudioSample] = None

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)

    post_id: Optional[str] = FieldInfo(alias="postId", default=None)

    stamp: Optional[str] = None
