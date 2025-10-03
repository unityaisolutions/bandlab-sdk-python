# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import ProviderType139, login_create_params, login_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.login import Login
from .._base_client import make_request_options
from ..types.provider_type_139 import ProviderType139
from ..types.login_list_response import LoginListResponse

__all__ = ["LoginsResource", "AsyncLoginsResource"]


class LoginsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LoginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return LoginsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        access_token: str | Omit = omit,
        provider: Literal["Google", "Facebook"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Login:
        """
        Add external login

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/logins",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "provider": provider,
                },
                login_create_params.LoginCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Login,
        )

    def update(
        self,
        provider_type: ProviderType139,
        *,
        access_token: str | Omit = omit,
        provider: Literal["Google", "Facebook"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Login:
        """
        Updates an external login

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_type:
            raise ValueError(f"Expected a non-empty value for `provider_type` but received {provider_type!r}")
        return self._put(
            f"/logins/{provider_type}",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "provider": provider,
                },
                login_update_params.LoginUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Login,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginListResponse:
        """Returns external logins"""
        return self._get(
            "/logins",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginListResponse,
        )

    def delete(
        self,
        provider_type: ProviderType139,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes an external login

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_type:
            raise ValueError(f"Expected a non-empty value for `provider_type` but received {provider_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/logins/{provider_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLoginsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncLoginsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        access_token: str | Omit = omit,
        provider: Literal["Google", "Facebook"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Login:
        """
        Add external login

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/logins",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "provider": provider,
                },
                login_create_params.LoginCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Login,
        )

    async def update(
        self,
        provider_type: ProviderType139,
        *,
        access_token: str | Omit = omit,
        provider: Literal["Google", "Facebook"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Login:
        """
        Updates an external login

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_type:
            raise ValueError(f"Expected a non-empty value for `provider_type` but received {provider_type!r}")
        return await self._put(
            f"/logins/{provider_type}",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "provider": provider,
                },
                login_update_params.LoginUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Login,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginListResponse:
        """Returns external logins"""
        return await self._get(
            "/logins",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginListResponse,
        )

    async def delete(
        self,
        provider_type: ProviderType139,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes an external login

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_type:
            raise ValueError(f"Expected a non-empty value for `provider_type` but received {provider_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/logins/{provider_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LoginsResourceWithRawResponse:
    def __init__(self, logins: LoginsResource) -> None:
        self._logins = logins

        self.create = to_raw_response_wrapper(
            logins.create,
        )
        self.update = to_raw_response_wrapper(
            logins.update,
        )
        self.list = to_raw_response_wrapper(
            logins.list,
        )
        self.delete = to_raw_response_wrapper(
            logins.delete,
        )


class AsyncLoginsResourceWithRawResponse:
    def __init__(self, logins: AsyncLoginsResource) -> None:
        self._logins = logins

        self.create = async_to_raw_response_wrapper(
            logins.create,
        )
        self.update = async_to_raw_response_wrapper(
            logins.update,
        )
        self.list = async_to_raw_response_wrapper(
            logins.list,
        )
        self.delete = async_to_raw_response_wrapper(
            logins.delete,
        )


class LoginsResourceWithStreamingResponse:
    def __init__(self, logins: LoginsResource) -> None:
        self._logins = logins

        self.create = to_streamed_response_wrapper(
            logins.create,
        )
        self.update = to_streamed_response_wrapper(
            logins.update,
        )
        self.list = to_streamed_response_wrapper(
            logins.list,
        )
        self.delete = to_streamed_response_wrapper(
            logins.delete,
        )


class AsyncLoginsResourceWithStreamingResponse:
    def __init__(self, logins: AsyncLoginsResource) -> None:
        self._logins = logins

        self.create = async_to_streamed_response_wrapper(
            logins.create,
        )
        self.update = async_to_streamed_response_wrapper(
            logins.update,
        )
        self.list = async_to_streamed_response_wrapper(
            logins.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            logins.delete,
        )
