# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .collections.status import Status

__all__ = ["AudioSampleParam"]


class AudioSampleParam(TypedDict, total=False):
    id: str

    name: str

    status: Status
