# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .creator import Creator
from .picture import Picture
from .._models import BaseModel
from .collections.post import Post
from .collection_counters import CollectionCounters

__all__ = ["Collection"]


class Collection(BaseModel):
    name: str

    id: Optional[str] = None

    counters: Optional[CollectionCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    creator: Optional[Creator] = None

    description: Optional[str] = None

    is_public: Optional[bool] = FieldInfo(alias="isPublic", default=None)

    last_updated_on: Optional[datetime] = FieldInfo(alias="lastUpdatedOn", default=None)

    picture: Optional[Picture] = None

    posts: Optional[List[Post]] = None

    type: Optional[Literal["Playlist", "Album"]] = None
