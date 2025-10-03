# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Login"]


class Login(BaseModel):
    access_token: Optional[str] = FieldInfo(alias="accessToken", default=None)

    provider: Optional[Literal["Google", "Facebook"]] = None
