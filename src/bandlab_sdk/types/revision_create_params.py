# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .genre_param import GenreParam
from .creator_param import CreatorParam
from .audio_sample_param import AudioSampleParam
from .song_summary_param import SongSummaryParam
from .collections.client_id import ClientID
from .revision_counters_param import RevisionCountersParam

__all__ = ["RevisionCreateParams", "AuxChannel", "AuxChannelEffect", "Mastering"]


class RevisionCreateParams(TypedDict, total=False):
    id: str

    aux_channels: Annotated[Iterable[AuxChannel], PropertyInfo(alias="auxChannels")]

    client_id: Annotated[ClientID, PropertyInfo(alias="clientId")]

    counters: RevisionCountersParam

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    creator: CreatorParam

    description: str

    genres: Iterable[GenreParam]

    is_fork: Annotated[bool, PropertyInfo(alias="isFork")]

    is_public: Annotated[bool, PropertyInfo(alias="isPublic")]

    key: str

    mastering: Mastering

    mixdown: AudioSampleParam

    modified_on: Annotated[Union[str, datetime], PropertyInfo(alias="modifiedOn", format="iso8601")]

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]

    post_id: Annotated[str, PropertyInfo(alias="postId")]

    samples: Iterable[AudioSampleParam]

    song: SongSummaryParam

    stamp: str

    tracks: Iterable[AudioSampleParam]


class AuxChannelEffect(TypedDict, total=False):
    bypass: bool

    params: object

    slug: str


class AuxChannel(TypedDict, total=False):
    id: str

    effects: Iterable[AuxChannelEffect]

    preset: str

    return_level: Annotated[float, PropertyInfo(alias="returnLevel")]


class Mastering(TypedDict, total=False):
    dry_sample_id: Annotated[str, PropertyInfo(alias="drySampleId")]

    preset: str
