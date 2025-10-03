# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserCountersParam"]


class UserCountersParam(TypedDict, total=False):
    bands: int

    collections: int

    followers: int

    following: int
