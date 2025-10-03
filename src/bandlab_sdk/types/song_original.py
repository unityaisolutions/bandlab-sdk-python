# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .picture import Picture
from .._models import BaseModel

__all__ = ["SongOriginal"]


class SongOriginal(BaseModel):
    creator_name: Optional[str] = FieldInfo(alias="creatorName", default=None)

    name: Optional[str] = None

    picture: Optional[Picture] = None

    revision_id: Optional[str] = FieldInfo(alias="revisionId", default=None)

    song_id: Optional[str] = FieldInfo(alias="songId", default=None)
