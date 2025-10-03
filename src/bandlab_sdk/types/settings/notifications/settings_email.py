# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SettingsEmail"]


class SettingsEmail(BaseModel):
    invitation_to_band: Optional[bool] = FieldInfo(alias="invitationToBand", default=None)

    invitation_to_song: Optional[bool] = FieldInfo(alias="invitationToSong", default=None)

    join_to_band_request: Optional[bool] = FieldInfo(alias="joinToBandRequest", default=None)

    new_band_member: Optional[bool] = FieldInfo(alias="newBandMember", default=None)

    new_revision: Optional[bool] = FieldInfo(alias="newRevision", default=None)

    new_song_collaborator: Optional[bool] = FieldInfo(alias="newSongCollaborator", default=None)

    new_song_in_band: Optional[bool] = FieldInfo(alias="newSongInBand", default=None)

    request_to_join_approved: Optional[bool] = FieldInfo(alias="requestToJoinApproved", default=None)
