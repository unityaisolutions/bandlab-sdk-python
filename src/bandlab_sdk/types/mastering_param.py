# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MasteringParam"]


class MasteringParam(TypedDict, total=False):
    dry_sample_id: Annotated[str, PropertyInfo(alias="drySampleId")]

    preset: str
