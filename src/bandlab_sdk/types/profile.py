# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .genre import Genre
from .skill import Skill
from .picture import Picture
from .._models import BaseModel
from .location import Location
from .user_counters import UserCounters

__all__ = ["Profile", "Ftue"]


class Ftue(BaseModel):
    confirmed_email: Optional[bool] = FieldInfo(alias="confirmedEmail", default=None)

    created_band: Optional[bool] = FieldInfo(alias="createdBand", default=None)

    created_song: Optional[bool] = FieldInfo(alias="createdSong", default=None)

    set_custom_username: Optional[bool] = FieldInfo(alias="setCustomUsername", default=None)

    set_genres: Optional[bool] = FieldInfo(alias="setGenres", default=None)

    set_picture: Optional[bool] = FieldInfo(alias="setPicture", default=None)

    set_skills: Optional[bool] = FieldInfo(alias="setSkills", default=None)


class Profile(BaseModel):
    id: Optional[str] = None

    about: Optional[str] = None

    badges: Optional[List[str]] = None

    birthday: Optional[date] = None

    counters: Optional[UserCounters] = None

    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    email: Optional[str] = None

    ftue: Optional[Ftue] = None

    gender: Optional[Literal["Male", "Female", "Other"]] = None

    genres: Optional[List[Genre]] = None

    has_password: Optional[bool] = FieldInfo(alias="hasPassword", default=None)

    is_beta_user: Optional[bool] = FieldInfo(alias="isBetaUser", default=None)

    is_email_confirmed: Optional[bool] = FieldInfo(alias="isEmailConfirmed", default=None)

    is_newbie: Optional[bool] = FieldInfo(alias="isNewbie", default=None)

    is_social: Optional[bool] = FieldInfo(alias="isSocial", default=None)

    is_tippable: Optional[bool] = FieldInfo(alias="isTippable", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    location: Optional[Location] = None

    name: Optional[str] = None

    picture: Optional[Picture] = None

    skills: Optional[List[Skill]] = None

    username: Optional[str] = None
