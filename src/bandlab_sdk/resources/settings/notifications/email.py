# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.settings.notifications import email_update_params
from ....types.settings.notifications.settings_email import SettingsEmail

__all__ = ["EmailResource", "AsyncEmailResource"]


class EmailResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return EmailResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsEmail:
        """Returns email notifications settings"""
        return self._get(
            "/settings/notifications/email",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsEmail,
        )

    def update(
        self,
        *,
        invitation_to_band: bool | Omit = omit,
        invitation_to_song: bool | Omit = omit,
        join_to_band_request: bool | Omit = omit,
        new_band_member: bool | Omit = omit,
        new_revision: bool | Omit = omit,
        new_song_collaborator: bool | Omit = omit,
        new_song_in_band: bool | Omit = omit,
        request_to_join_approved: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsEmail:
        """
        Updates email notifications settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/settings/notifications/email",
            body=maybe_transform(
                {
                    "invitation_to_band": invitation_to_band,
                    "invitation_to_song": invitation_to_song,
                    "join_to_band_request": join_to_band_request,
                    "new_band_member": new_band_member,
                    "new_revision": new_revision,
                    "new_song_collaborator": new_song_collaborator,
                    "new_song_in_band": new_song_in_band,
                    "request_to_join_approved": request_to_join_approved,
                },
                email_update_params.EmailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsEmail,
        )


class AsyncEmailResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncEmailResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsEmail:
        """Returns email notifications settings"""
        return await self._get(
            "/settings/notifications/email",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsEmail,
        )

    async def update(
        self,
        *,
        invitation_to_band: bool | Omit = omit,
        invitation_to_song: bool | Omit = omit,
        join_to_band_request: bool | Omit = omit,
        new_band_member: bool | Omit = omit,
        new_revision: bool | Omit = omit,
        new_song_collaborator: bool | Omit = omit,
        new_song_in_band: bool | Omit = omit,
        request_to_join_approved: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsEmail:
        """
        Updates email notifications settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/settings/notifications/email",
            body=await async_maybe_transform(
                {
                    "invitation_to_band": invitation_to_band,
                    "invitation_to_song": invitation_to_song,
                    "join_to_band_request": join_to_band_request,
                    "new_band_member": new_band_member,
                    "new_revision": new_revision,
                    "new_song_collaborator": new_song_collaborator,
                    "new_song_in_band": new_song_in_band,
                    "request_to_join_approved": request_to_join_approved,
                },
                email_update_params.EmailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsEmail,
        )


class EmailResourceWithRawResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

        self.retrieve = to_raw_response_wrapper(
            email.retrieve,
        )
        self.update = to_raw_response_wrapper(
            email.update,
        )


class AsyncEmailResourceWithRawResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

        self.retrieve = async_to_raw_response_wrapper(
            email.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            email.update,
        )


class EmailResourceWithStreamingResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

        self.retrieve = to_streamed_response_wrapper(
            email.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            email.update,
        )


class AsyncEmailResourceWithStreamingResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

        self.retrieve = async_to_streamed_response_wrapper(
            email.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            email.update,
        )
