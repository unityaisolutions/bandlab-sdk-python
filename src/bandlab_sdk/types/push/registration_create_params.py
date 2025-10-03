# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RegistrationCreateParams"]


class RegistrationCreateParams(TypedDict, total=False):
    device_id: Annotated[str, PropertyInfo(alias="deviceId")]

    platfrom: Literal["Gcm", "Apns"]

    pns_id: Annotated[str, PropertyInfo(alias="pnsId")]
