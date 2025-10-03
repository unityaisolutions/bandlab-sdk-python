# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .users.paging import Paging

__all__ = ["SearchSearchBandsResponse"]


class SearchSearchBandsResponse(BaseModel):
    data: Optional[List[object]] = None

    paging: Optional[Paging] = None
