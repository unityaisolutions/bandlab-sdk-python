# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .picture_param import PictureParam

__all__ = ["SongOriginalParam"]


class SongOriginalParam(TypedDict, total=False):
    creator_name: Annotated[str, PropertyInfo(alias="creatorName")]

    name: str

    picture: PictureParam

    revision_id: Annotated[str, PropertyInfo(alias="revisionId")]

    song_id: Annotated[str, PropertyInfo(alias="songId")]
