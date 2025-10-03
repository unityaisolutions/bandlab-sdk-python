# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .author_param import AuthorParam
from .creator_param import CreatorParam
from .picture_param import PictureParam
from .song_counters_param import SongCountersParam
from .song_original_param import SongOriginalParam
from .user_counters_param import UserCountersParam

__all__ = ["SongUpdateParams", "Collaborator"]


class SongUpdateParams(TypedDict, total=False):
    name: Required[str]

    id: str

    author: AuthorParam

    collaborators: Iterable[Collaborator]

    counters: SongCountersParam

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    creator: CreatorParam

    description: str

    is_fork: Annotated[bool, PropertyInfo(alias="isFork")]

    is_forkable: Annotated[bool, PropertyInfo(alias="isForkable")]

    is_public: Annotated[bool, PropertyInfo(alias="isPublic")]

    modified_on: Annotated[Union[str, datetime], PropertyInfo(alias="modifiedOn", format="iso8601")]

    original: SongOriginalParam

    picture: PictureParam

    slug: str


class Collaborator(TypedDict, total=False):
    id: str

    counters: UserCountersParam

    name: str

    picture: PictureParam

    username: str
