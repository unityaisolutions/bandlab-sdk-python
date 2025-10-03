# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VersionRetrieveResponse"]


class VersionRetrieveResponse(BaseModel):
    last: Optional[str] = None

    message: Optional[str] = None

    min: Optional[str] = None

    url: Optional[str] = None
