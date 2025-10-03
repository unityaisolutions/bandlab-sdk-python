# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["InviteSendParams"]


class InviteSendParams(TypedDict, total=False):
    emails: SequenceNotStr[str]

    message: str

    user_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="userIds")]
