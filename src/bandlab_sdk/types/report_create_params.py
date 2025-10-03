# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReportCreateParams"]


class ReportCreateParams(TypedDict, total=False):
    description: str

    object_id: Annotated[str, PropertyInfo(alias="objectId")]

    object_type: Annotated[str, PropertyInfo(alias="objectType")]

    report_type: Annotated[str, PropertyInfo(alias="reportType")]
