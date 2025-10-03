# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .badge import Badge
from .genre import Genre
from .skill import Skill
from .._models import BaseModel

__all__ = ["LabelListResponse", "LabelListResponseItem"]


class LabelListResponseItem(BaseModel):
    badges: Optional[List[Badge]] = None

    genres: Optional[List[Genre]] = None

    skills: Optional[List[Skill]] = None


LabelListResponse: TypeAlias = List[LabelListResponseItem]
