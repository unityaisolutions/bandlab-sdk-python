# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VersionValidateParams"]


class VersionValidateParams(TypedDict, total=False):
    client_id: Required[Annotated[str, PropertyInfo(alias="clientId")]]

    client_version: Required[Annotated[str, PropertyInfo(alias="clientVersion")]]
