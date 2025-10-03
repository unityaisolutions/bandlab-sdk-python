# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["NotificationUpdateAllParams"]


class NotificationUpdateAllParams(TypedDict, total=False):
    ids: SequenceNotStr[str]

    last_read_on: Annotated[Union[str, datetime], PropertyInfo(alias="lastReadOn", format="iso8601")]

    unread: bool
