# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..users.paging import Paging

__all__ = ["RevisionListResponse"]


class RevisionListResponse(BaseModel):
    data: Optional[List[object]] = None

    paging: Optional[Paging] = None
