# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .collections.status import Status

__all__ = ["AudioSample"]


class AudioSample(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    status: Optional[Status] = None
