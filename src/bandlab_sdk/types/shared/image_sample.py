# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..picture import Picture
from ..._models import BaseModel
from .image_sample_counters import ImageSampleCounters

__all__ = ["ImageSample"]


class ImageSample(BaseModel):
    id: Optional[str] = None

    counters: Optional[ImageSampleCounters] = None

    picture: Optional[Picture] = None
