# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .author import Author
from .creator import Creator
from .picture import Picture
from .._models import BaseModel
from .song_counters import SongCounters
from .song_original import SongOriginal
from .user_counters import UserCounters

__all__ = ["Song", "Collaborator"]


class Collaborator(BaseModel):
    id: Optional[str] = None

    counters: Optional[UserCounters] = None

    name: Optional[str] = None

    picture: Optional[Picture] = None

    username: Optional[str] = None


class Song(BaseModel):
    name: str

    id: Optional[str] = None

    author: Optional[Author] = None

    collaborators: Optional[List[Collaborator]] = None

    counters: Optional[SongCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    creator: Optional[Creator] = None

    description: Optional[str] = None

    is_fork: Optional[bool] = FieldInfo(alias="isFork", default=None)

    is_forkable: Optional[bool] = FieldInfo(alias="isForkable", default=None)

    is_public: Optional[bool] = FieldInfo(alias="isPublic", default=None)

    modified_on: Optional[datetime] = FieldInfo(alias="modifiedOn", default=None)

    original: Optional[SongOriginal] = None

    picture: Optional[Picture] = None

    slug: Optional[str] = None
