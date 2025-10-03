# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthorParam"]


class AuthorParam(TypedDict, total=False):
    id: str

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]

    name: str

    type: Literal["User", "Band"]

    username: str
