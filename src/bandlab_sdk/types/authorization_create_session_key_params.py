# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .provider import Provider

__all__ = ["AuthorizationCreateSessionKeyParams"]


class AuthorizationCreateSessionKeyParams(TypedDict, total=False):
    access_token: Annotated[str, PropertyInfo(alias="accessToken")]

    email: str

    key: str

    login: str

    name: str

    password: str

    provider: Provider

    referral: str

    refresh_token: Annotated[str, PropertyInfo(alias="refreshToken")]

    register: bool

    remember_me: Annotated[bool, PropertyInfo(alias="rememberMe")]

    username: str
