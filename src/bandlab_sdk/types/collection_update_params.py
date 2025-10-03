# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .creator_param import CreatorParam
from .picture_param import PictureParam
from .collections.post_param import PostParam
from .collection_counters_param import CollectionCountersParam

__all__ = ["CollectionUpdateParams"]


class CollectionUpdateParams(TypedDict, total=False):
    name: Required[str]

    id: str

    counters: CollectionCountersParam

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    creator: CreatorParam

    description: str

    is_public: Annotated[bool, PropertyInfo(alias="isPublic")]

    last_updated_on: Annotated[Union[str, datetime], PropertyInfo(alias="lastUpdatedOn", format="iso8601")]

    picture: PictureParam

    posts: Iterable[PostParam]

    type: Literal["Playlist", "Album"]
