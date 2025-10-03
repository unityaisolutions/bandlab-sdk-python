# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Mastering"]


class Mastering(BaseModel):
    dry_sample_id: Optional[str] = FieldInfo(alias="drySampleId", default=None)

    preset: Optional[str] = None
