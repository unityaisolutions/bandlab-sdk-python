# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .creator_param import CreatorParam
from .posts.comment_param import CommentParam
from .collections.client_id import ClientID
from .shared_params.image_sample import ImageSample
from .shared_params.video_sample import VideoSample
from .shared_params.post_counters import PostCounters
from .shared_params.revision_summary import RevisionSummary

__all__ = ["VideoCreatePostParams"]


class VideoCreatePostParams(TypedDict, total=False):
    id: str

    caption: str

    client_id: Annotated[ClientID, PropertyInfo(alias="clientId")]

    comments: Iterable[CommentParam]

    counters: PostCounters

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    creator: CreatorParam

    image: ImageSample

    message: str

    revision: RevisionSummary

    type: Literal["Revision", "Image", "Video", "Text"]

    video: VideoSample
