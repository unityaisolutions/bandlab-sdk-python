# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PostListParams"]


class PostListParams(TypedDict, total=False):
    after: str

    before: str

    limit: int

    offset: int
