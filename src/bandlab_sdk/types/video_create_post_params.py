# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .creator_param import CreatorParam
from .picture_param import PictureParam
from .audio_sample_param import AudioSampleParam
from .collections.status import Status
from .posts.comment_param import CommentParam
from .collections.client_id import ClientID
from .revision_counters_param import RevisionCountersParam

__all__ = [
    "VideoCreatePostParams",
    "Counters",
    "Image",
    "ImageCounters",
    "Revision",
    "RevisionLyrics",
    "Video",
    "VideoCounters",
]


class VideoCreatePostParams(TypedDict, total=False):
    id: str

    caption: str

    client_id: Annotated[ClientID, PropertyInfo(alias="clientId")]

    comments: Iterable[CommentParam]

    counters: Counters

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    creator: CreatorParam

    image: Image

    message: str

    revision: Revision

    type: Literal["Revision", "Image", "Video", "Text"]

    video: Video


class Counters(TypedDict, total=False):
    comments: int

    likes: int

    reposts: int


class ImageCounters(TypedDict, total=False):
    likes: int


class Image(TypedDict, total=False):
    id: str

    counters: ImageCounters

    picture: PictureParam


class RevisionLyrics(TypedDict, total=False):
    content: str


class Revision(TypedDict, total=False):
    id: str

    client_id: Annotated[ClientID, PropertyInfo(alias="clientId")]

    counters: RevisionCountersParam

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    creator: CreatorParam

    description: str

    is_fork: Annotated[bool, PropertyInfo(alias="isFork")]

    is_public: Annotated[bool, PropertyInfo(alias="isPublic")]

    lyrics: RevisionLyrics

    mixdown: AudioSampleParam

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]

    post_id: Annotated[str, PropertyInfo(alias="postId")]

    stamp: str


class VideoCounters(TypedDict, total=False):
    likes: int

    views: int


class Video(TypedDict, total=False):
    id: str

    counters: VideoCounters

    duration: float

    picture: PictureParam

    status: Status
