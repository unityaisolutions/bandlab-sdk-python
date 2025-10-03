# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import Provider, authorization_create_session_key_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.provider import Provider
from ..types.authorization_create_session_key_response import AuthorizationCreateSessionKeyResponse

__all__ = ["AuthorizationsResource", "AsyncAuthorizationsResource"]


class AuthorizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthorizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AuthorizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthorizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AuthorizationsResourceWithStreamingResponse(self)

    def create_session_key(
        self,
        *,
        access_token: str | Omit = omit,
        email: str | Omit = omit,
        key: str | Omit = omit,
        login: str | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        provider: Provider | Omit = omit,
        referral: str | Omit = omit,
        refresh_token: str | Omit = omit,
        register: bool | Omit = omit,
        remember_me: bool | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthorizationCreateSessionKeyResponse:
        """
        Generates a session key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/authorizations",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "email": email,
                    "key": key,
                    "login": login,
                    "name": name,
                    "password": password,
                    "provider": provider,
                    "referral": referral,
                    "refresh_token": refresh_token,
                    "register": register,
                    "remember_me": remember_me,
                    "username": username,
                },
                authorization_create_session_key_params.AuthorizationCreateSessionKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizationCreateSessionKeyResponse,
        )


class AsyncAuthorizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthorizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthorizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthorizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncAuthorizationsResourceWithStreamingResponse(self)

    async def create_session_key(
        self,
        *,
        access_token: str | Omit = omit,
        email: str | Omit = omit,
        key: str | Omit = omit,
        login: str | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        provider: Provider | Omit = omit,
        referral: str | Omit = omit,
        refresh_token: str | Omit = omit,
        register: bool | Omit = omit,
        remember_me: bool | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthorizationCreateSessionKeyResponse:
        """
        Generates a session key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/authorizations",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "email": email,
                    "key": key,
                    "login": login,
                    "name": name,
                    "password": password,
                    "provider": provider,
                    "referral": referral,
                    "refresh_token": refresh_token,
                    "register": register,
                    "remember_me": remember_me,
                    "username": username,
                },
                authorization_create_session_key_params.AuthorizationCreateSessionKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizationCreateSessionKeyResponse,
        )


class AuthorizationsResourceWithRawResponse:
    def __init__(self, authorizations: AuthorizationsResource) -> None:
        self._authorizations = authorizations

        self.create_session_key = to_raw_response_wrapper(
            authorizations.create_session_key,
        )


class AsyncAuthorizationsResourceWithRawResponse:
    def __init__(self, authorizations: AsyncAuthorizationsResource) -> None:
        self._authorizations = authorizations

        self.create_session_key = async_to_raw_response_wrapper(
            authorizations.create_session_key,
        )


class AuthorizationsResourceWithStreamingResponse:
    def __init__(self, authorizations: AuthorizationsResource) -> None:
        self._authorizations = authorizations

        self.create_session_key = to_streamed_response_wrapper(
            authorizations.create_session_key,
        )


class AsyncAuthorizationsResourceWithStreamingResponse:
    def __init__(self, authorizations: AsyncAuthorizationsResource) -> None:
        self._authorizations = authorizations

        self.create_session_key = async_to_streamed_response_wrapper(
            authorizations.create_session_key,
        )
