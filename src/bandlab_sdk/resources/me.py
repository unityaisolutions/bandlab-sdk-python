# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ..types import me_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.profile import Profile
from ..types.genre_param import GenreParam
from ..types.skill_param import SkillParam
from ..types.picture_param import PictureParam
from ..types.location_param import LocationParam
from ..types.user_counters_param import UserCountersParam

__all__ = ["MeResource", "AsyncMeResource"]


class MeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return MeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Profile:
        """Returns a profile of current user"""
        return self._get(
            "/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Profile,
        )

    def update(
        self,
        *,
        id: str | Omit = omit,
        about: str | Omit = omit,
        badges: SequenceNotStr[str] | Omit = omit,
        birthday: Union[str, date] | Omit = omit,
        counters: UserCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        email: str | Omit = omit,
        ftue: me_update_params.Ftue | Omit = omit,
        gender: Literal["Male", "Female", "Other"] | Omit = omit,
        genres: Iterable[GenreParam] | Omit = omit,
        has_password: bool | Omit = omit,
        is_beta_user: bool | Omit = omit,
        is_email_confirmed: bool | Omit = omit,
        is_newbie: bool | Omit = omit,
        is_social: bool | Omit = omit,
        is_tippable: bool | Omit = omit,
        is_verified: bool | Omit = omit,
        location: LocationParam | Omit = omit,
        name: str | Omit = omit,
        picture: PictureParam | Omit = omit,
        skills: Iterable[SkillParam] | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Profile:
        """
        Updates a profile of current user

        Args:
          badges

          genres

          skills

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/me",
            body=maybe_transform(
                {
                    "id": id,
                    "about": about,
                    "badges": badges,
                    "birthday": birthday,
                    "counters": counters,
                    "created_on": created_on,
                    "email": email,
                    "ftue": ftue,
                    "gender": gender,
                    "genres": genres,
                    "has_password": has_password,
                    "is_beta_user": is_beta_user,
                    "is_email_confirmed": is_email_confirmed,
                    "is_newbie": is_newbie,
                    "is_social": is_social,
                    "is_tippable": is_tippable,
                    "is_verified": is_verified,
                    "location": location,
                    "name": name,
                    "picture": picture,
                    "skills": skills,
                    "username": username,
                },
                me_update_params.MeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Profile,
        )


class AsyncMeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncMeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Profile:
        """Returns a profile of current user"""
        return await self._get(
            "/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Profile,
        )

    async def update(
        self,
        *,
        id: str | Omit = omit,
        about: str | Omit = omit,
        badges: SequenceNotStr[str] | Omit = omit,
        birthday: Union[str, date] | Omit = omit,
        counters: UserCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        email: str | Omit = omit,
        ftue: me_update_params.Ftue | Omit = omit,
        gender: Literal["Male", "Female", "Other"] | Omit = omit,
        genres: Iterable[GenreParam] | Omit = omit,
        has_password: bool | Omit = omit,
        is_beta_user: bool | Omit = omit,
        is_email_confirmed: bool | Omit = omit,
        is_newbie: bool | Omit = omit,
        is_social: bool | Omit = omit,
        is_tippable: bool | Omit = omit,
        is_verified: bool | Omit = omit,
        location: LocationParam | Omit = omit,
        name: str | Omit = omit,
        picture: PictureParam | Omit = omit,
        skills: Iterable[SkillParam] | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Profile:
        """
        Updates a profile of current user

        Args:
          badges

          genres

          skills

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/me",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "about": about,
                    "badges": badges,
                    "birthday": birthday,
                    "counters": counters,
                    "created_on": created_on,
                    "email": email,
                    "ftue": ftue,
                    "gender": gender,
                    "genres": genres,
                    "has_password": has_password,
                    "is_beta_user": is_beta_user,
                    "is_email_confirmed": is_email_confirmed,
                    "is_newbie": is_newbie,
                    "is_social": is_social,
                    "is_tippable": is_tippable,
                    "is_verified": is_verified,
                    "location": location,
                    "name": name,
                    "picture": picture,
                    "skills": skills,
                    "username": username,
                },
                me_update_params.MeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Profile,
        )


class MeResourceWithRawResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.retrieve = to_raw_response_wrapper(
            me.retrieve,
        )
        self.update = to_raw_response_wrapper(
            me.update,
        )


class AsyncMeResourceWithRawResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.retrieve = async_to_raw_response_wrapper(
            me.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            me.update,
        )


class MeResourceWithStreamingResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.retrieve = to_streamed_response_wrapper(
            me.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            me.update,
        )


class AsyncMeResourceWithStreamingResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.retrieve = async_to_streamed_response_wrapper(
            me.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            me.update,
        )
