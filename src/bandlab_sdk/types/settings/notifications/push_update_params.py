# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PushUpdateParams"]


class PushUpdateParams(TypedDict, total=False):
    invitation_to_band: Annotated[bool, PropertyInfo(alias="invitationToBand")]

    invitation_to_song: Annotated[bool, PropertyInfo(alias="invitationToSong")]

    join_to_band_request: Annotated[bool, PropertyInfo(alias="joinToBandRequest")]

    new_band_member: Annotated[bool, PropertyInfo(alias="newBandMember")]

    new_revision: Annotated[bool, PropertyInfo(alias="newRevision")]

    new_song_collaborator: Annotated[bool, PropertyInfo(alias="newSongCollaborator")]

    new_song_in_band: Annotated[bool, PropertyInfo(alias="newSongInBand")]

    request_to_join_approved: Annotated[bool, PropertyInfo(alias="requestToJoinApproved")]
