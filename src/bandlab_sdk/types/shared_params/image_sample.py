# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..picture_param import PictureParam
from .image_sample_counters import ImageSampleCounters

__all__ = ["ImageSample"]


class ImageSample(TypedDict, total=False):
    id: str

    counters: ImageSampleCounters

    picture: PictureParam
