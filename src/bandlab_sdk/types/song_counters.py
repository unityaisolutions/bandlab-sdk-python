# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SongCounters"]


class SongCounters(BaseModel):
    collaborators: Optional[int] = None

    comments: Optional[int] = None

    forks: Optional[int] = None

    likes: Optional[int] = None

    plays: Optional[int] = None

    public_revisions: Optional[int] = FieldInfo(alias="publicRevisions", default=None)
