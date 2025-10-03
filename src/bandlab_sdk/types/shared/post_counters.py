# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PostCounters"]


class PostCounters(BaseModel):
    comments: Optional[int] = None

    likes: Optional[int] = None

    reposts: Optional[int] = None
