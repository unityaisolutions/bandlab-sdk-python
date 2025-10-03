# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VideoSampleCounters"]


class VideoSampleCounters(BaseModel):
    likes: Optional[int] = None

    views: Optional[int] = None
