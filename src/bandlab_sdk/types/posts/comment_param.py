# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..creator_param import CreatorParam

__all__ = ["CommentParam"]


class CommentParam(TypedDict, total=False):
    id: int

    content: str

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    creator: CreatorParam

    timestamp: float
