# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .lyrics import Lyrics
from ..._utils import PropertyInfo
from ..creator_param import CreatorParam
from ..audio_sample_param import AudioSampleParam
from ..collections.client_id import ClientID
from ..revision_counters_param import RevisionCountersParam

__all__ = ["RevisionSummary"]


class RevisionSummary(TypedDict, total=False):
    id: str

    client_id: Annotated[ClientID, PropertyInfo(alias="clientId")]

    counters: RevisionCountersParam

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    creator: CreatorParam

    description: str

    is_fork: Annotated[bool, PropertyInfo(alias="isFork")]

    is_public: Annotated[bool, PropertyInfo(alias="isPublic")]

    lyrics: Lyrics

    mixdown: AudioSampleParam

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]

    post_id: Annotated[str, PropertyInfo(alias="postId")]

    stamp: str
