# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .genre_param import GenreParam
from .skill_param import SkillParam
from .picture_param import PictureParam
from .location_param import LocationParam
from .user_counters_param import UserCountersParam

__all__ = ["MeUpdateParams", "Ftue"]


class MeUpdateParams(TypedDict, total=False):
    id: str

    about: str

    badges: SequenceNotStr[str]

    birthday: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    counters: UserCountersParam

    created_on: Annotated[Union[str, datetime], PropertyInfo(alias="createdOn", format="iso8601")]

    email: str

    ftue: Ftue

    gender: Literal["Male", "Female", "Other"]

    genres: Iterable[GenreParam]

    has_password: Annotated[bool, PropertyInfo(alias="hasPassword")]

    is_beta_user: Annotated[bool, PropertyInfo(alias="isBetaUser")]

    is_email_confirmed: Annotated[bool, PropertyInfo(alias="isEmailConfirmed")]

    is_newbie: Annotated[bool, PropertyInfo(alias="isNewbie")]

    is_social: Annotated[bool, PropertyInfo(alias="isSocial")]

    is_tippable: Annotated[bool, PropertyInfo(alias="isTippable")]

    is_verified: Annotated[bool, PropertyInfo(alias="isVerified")]

    location: LocationParam

    name: str

    picture: PictureParam

    skills: Iterable[SkillParam]

    username: str


class Ftue(TypedDict, total=False):
    confirmed_email: Annotated[bool, PropertyInfo(alias="confirmedEmail")]

    created_band: Annotated[bool, PropertyInfo(alias="createdBand")]

    created_song: Annotated[bool, PropertyInfo(alias="createdSong")]

    set_custom_username: Annotated[bool, PropertyInfo(alias="setCustomUsername")]

    set_genres: Annotated[bool, PropertyInfo(alias="setGenres")]

    set_picture: Annotated[bool, PropertyInfo(alias="setPicture")]

    set_skills: Annotated[bool, PropertyInfo(alias="setSkills")]
