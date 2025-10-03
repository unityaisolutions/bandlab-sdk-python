# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .picture_param import PictureParam

__all__ = ["CreatorParam"]


class CreatorParam(TypedDict, total=False):
    id: str

    is_verified: Annotated[bool, PropertyInfo(alias="isVerified")]

    name: str

    picture: PictureParam

    username: str
