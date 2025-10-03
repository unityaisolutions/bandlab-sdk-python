# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["NotificationUpdateParams"]


class NotificationUpdateParams(TypedDict, total=False):
    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]

    ids: SequenceNotStr[str]

    last_read_on: Annotated[Union[str, datetime], PropertyInfo(alias="lastReadOn", format="iso8601")]

    unread: bool
