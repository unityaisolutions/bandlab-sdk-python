# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .paging import Paging
from ..._models import BaseModel

__all__ = ["ContactListBandsResponse"]


class ContactListBandsResponse(BaseModel):
    data: Optional[List[object]] = None

    paging: Optional[Paging] = None
