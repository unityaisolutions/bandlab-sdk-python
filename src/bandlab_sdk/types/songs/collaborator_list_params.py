# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CollaboratorListParams"]


class CollaboratorListParams(TypedDict, total=False):
    community_id: Required[Annotated[str, PropertyInfo(alias="communityId")]]

    after: str

    before: str

    limit: int

    offset: int
