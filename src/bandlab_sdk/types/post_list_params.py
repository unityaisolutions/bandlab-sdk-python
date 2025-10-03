# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PostListParams"]


class PostListParams(TypedDict, total=False):
    after: str

    before: str

    forkable: bool

    genres: str

    limit: int

    offset: int

    sort: Literal["recent", "popular", "inspiring"]

    spotlights: str

    tag: str

    types: str
