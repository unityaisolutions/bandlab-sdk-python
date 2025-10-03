# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ValidationValidateResponse"]


class ValidationValidateResponse(BaseModel):
    is_available: Optional[bool] = FieldInfo(alias="isAvailable", default=None)

    is_valid: Optional[bool] = FieldInfo(alias="isValid", default=None)
