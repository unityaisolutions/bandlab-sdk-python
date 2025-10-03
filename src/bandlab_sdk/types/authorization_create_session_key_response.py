# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .provider import Provider

__all__ = ["AuthorizationCreateSessionKeyResponse"]


class AuthorizationCreateSessionKeyResponse(BaseModel):
    expire_date: Optional[datetime] = FieldInfo(alias="expireDate", default=None)

    provider: Optional[Provider] = None

    refresh_token: Optional[str] = FieldInfo(alias="refreshToken", default=None)

    session_key: Optional[str] = FieldInfo(alias="sessionKey", default=None)

    was_registered: Optional[bool] = FieldInfo(alias="wasRegistered", default=None)
