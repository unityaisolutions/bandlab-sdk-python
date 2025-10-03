# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Author"]


class Author(BaseModel):
    id: Optional[str] = None

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    name: Optional[str] = None

    type: Optional[Literal["User", "Band"]] = None

    username: Optional[str] = None
