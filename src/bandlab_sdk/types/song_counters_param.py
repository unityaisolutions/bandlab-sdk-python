# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SongCountersParam"]


class SongCountersParam(TypedDict, total=False):
    collaborators: int

    comments: int

    forks: int

    likes: int

    plays: int

    public_revisions: Annotated[int, PropertyInfo(alias="publicRevisions")]
