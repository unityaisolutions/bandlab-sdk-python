# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Paging", "Cursors"]


class Cursors(BaseModel):
    after: Optional[str] = None

    before: Optional[str] = None


class Paging(BaseModel):
    cursors: Optional[Cursors] = None

    items_count: Optional[int] = FieldInfo(alias="itemsCount", default=None)

    limit: Optional[int] = None

    offset: Optional[int] = None
