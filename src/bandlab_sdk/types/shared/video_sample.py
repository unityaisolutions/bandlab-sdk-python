# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..picture import Picture
from ..._models import BaseModel
from ..collections.status import Status
from .video_sample_counters import VideoSampleCounters

__all__ = ["VideoSample"]


class VideoSample(BaseModel):
    id: Optional[str] = None

    counters: Optional[VideoSampleCounters] = None

    duration: Optional[float] = None

    picture: Optional[Picture] = None

    status: Optional[Status] = None
