# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PictureParam"]


class PictureParam(TypedDict, total=False):
    is_default: Annotated[bool, PropertyInfo(alias="isDefault")]

    l: str

    m: str

    s: str

    url: str
