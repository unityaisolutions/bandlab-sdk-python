# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RevisionCounters"]


class RevisionCounters(BaseModel):
    comments: Optional[int] = None

    forks: Optional[int] = None

    likes: Optional[int] = None

    plays: Optional[int] = None
