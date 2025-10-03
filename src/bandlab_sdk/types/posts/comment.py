# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..creator import Creator
from ..._models import BaseModel

__all__ = ["Comment"]


class Comment(BaseModel):
    id: Optional[int] = None

    content: Optional[str] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    creator: Optional[Creator] = None

    timestamp: Optional[float] = None
