# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .status import Status
from ..creator import Creator
from ..picture import Picture
from ..._models import BaseModel
from .client_id import ClientID
from ..audio_sample import AudioSample
from ..posts.comment import Comment
from ..revision_counters import RevisionCounters

__all__ = ["Post", "Counters", "Image", "ImageCounters", "Revision", "RevisionLyrics", "Video", "VideoCounters"]


class Counters(BaseModel):
    comments: Optional[int] = None

    likes: Optional[int] = None

    reposts: Optional[int] = None


class ImageCounters(BaseModel):
    likes: Optional[int] = None


class Image(BaseModel):
    id: Optional[str] = None

    counters: Optional[ImageCounters] = None

    picture: Optional[Picture] = None


class RevisionLyrics(BaseModel):
    content: Optional[str] = None


class Revision(BaseModel):
    id: Optional[str] = None

    client_id: Optional[ClientID] = FieldInfo(alias="clientId", default=None)

    counters: Optional[RevisionCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    creator: Optional[Creator] = None

    description: Optional[str] = None

    is_fork: Optional[bool] = FieldInfo(alias="isFork", default=None)

    is_public: Optional[bool] = FieldInfo(alias="isPublic", default=None)

    lyrics: Optional[RevisionLyrics] = None

    mixdown: Optional[AudioSample] = None

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)

    post_id: Optional[str] = FieldInfo(alias="postId", default=None)

    stamp: Optional[str] = None


class VideoCounters(BaseModel):
    likes: Optional[int] = None

    views: Optional[int] = None


class Video(BaseModel):
    id: Optional[str] = None

    counters: Optional[VideoCounters] = None

    duration: Optional[float] = None

    picture: Optional[Picture] = None

    status: Optional[Status] = None


class Post(BaseModel):
    id: Optional[str] = None

    caption: Optional[str] = None

    client_id: Optional[ClientID] = FieldInfo(alias="clientId", default=None)

    comments: Optional[List[Comment]] = None

    counters: Optional[Counters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    creator: Optional[Creator] = None

    image: Optional[Image] = None

    message: Optional[str] = None

    revision: Optional[Revision] = None

    type: Optional[Literal["Revision", "Image", "Video", "Text"]] = None

    video: Optional[Video] = None
