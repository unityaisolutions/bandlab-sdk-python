# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..creator import Creator
from ..._models import BaseModel
from .client_id import ClientID
from ..posts.comment import Comment
from ..shared.image_sample import ImageSample
from ..shared.video_sample import VideoSample
from ..shared.post_counters import PostCounters
from ..shared.revision_summary import RevisionSummary

__all__ = ["Post"]


class Post(BaseModel):
    id: Optional[str] = None

    caption: Optional[str] = None

    client_id: Optional[ClientID] = FieldInfo(alias="clientId", default=None)

    comments: Optional[List[Comment]] = None

    counters: Optional[PostCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    creator: Optional[Creator] = None

    image: Optional[ImageSample] = None

    message: Optional[str] = None

    revision: Optional[RevisionSummary] = None

    type: Optional[Literal["Revision", "Image", "Video", "Text"]] = None

    video: Optional[VideoSample] = None
