# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .author import Author
from .picture import Picture
from .._models import BaseModel
from .song_counters import SongCounters
from .song_original import SongOriginal

__all__ = ["SongSummary"]


class SongSummary(BaseModel):
    id: Optional[str] = None

    author: Optional[Author] = None

    counters: Optional[SongCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    description: Optional[str] = None

    is_fork: Optional[bool] = FieldInfo(alias="isFork", default=None)

    is_forkable: Optional[bool] = FieldInfo(alias="isForkable", default=None)

    is_public: Optional[bool] = FieldInfo(alias="isPublic", default=None)

    name: Optional[str] = None

    original: Optional[SongOriginal] = None

    picture: Optional[Picture] = None

    slug: Optional[str] = None
