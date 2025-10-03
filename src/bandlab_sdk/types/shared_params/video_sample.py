# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..picture_param import PictureParam
from ..collections.status import Status
from .video_sample_counters import VideoSampleCounters

__all__ = ["VideoSample"]


class VideoSample(TypedDict, total=False):
    id: str

    counters: VideoSampleCounters

    duration: float

    picture: PictureParam

    status: Status
