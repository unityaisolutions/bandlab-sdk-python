# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .author_param import AuthorParam
from .picture_param import PictureParam
from .song_counters_param import SongCountersParam
from .song_original_param import SongOriginalParam

__all__ = ["SongSummaryParam"]


class SongSummaryParam(TypedDict, total=False):
    id: str

    author: AuthorParam

    counters: SongCountersParam

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    description: str

    is_fork: Annotated[bool, PropertyInfo(alias="isFork")]

    is_forkable: Annotated[bool, PropertyInfo(alias="isForkable")]

    is_public: Annotated[bool, PropertyInfo(alias="isPublic")]

    name: str

    original: SongOriginalParam

    picture: PictureParam

    slug: str
