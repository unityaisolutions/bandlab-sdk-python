# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Picture"]


class Picture(BaseModel):
    is_default: Optional[bool] = FieldInfo(alias="isDefault", default=None)

    l: Optional[str] = None

    m: Optional[str] = None

    s: Optional[str] = None

    url: Optional[str] = None
