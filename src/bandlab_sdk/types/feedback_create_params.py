# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FeedbackCreateParams"]


class FeedbackCreateParams(TypedDict, total=False):
    description: str

    report_type: Annotated[str, PropertyInfo(alias="reportType")]
