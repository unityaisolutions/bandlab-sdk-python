# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import password_reset_params, password_change_params, password_send_restore_email_params
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
from .._base_client import make_request_options

__all__ = ["PasswordsResource", "AsyncPasswordsResource"]


class PasswordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PasswordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PasswordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PasswordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return PasswordsResourceWithStreamingResponse(self)

    def change(
        self,
        *,
        new_password: str | Omit = omit,
        old_password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Changes password

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/passwords",
            body=maybe_transform(
                {
                    "new_password": new_password,
                    "old_password": old_password,
                },
                password_change_params.PasswordChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def reset(
        self,
        *,
        code: str | Omit = omit,
        new_password: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Resets password

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/passwords",
            body=maybe_transform(
                {
                    "code": code,
                    "new_password": new_password,
                    "user_id": user_id,
                },
                password_reset_params.PasswordResetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_restore_email(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Sends restore password email

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/passwords",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"email": email}, password_send_restore_email_params.PasswordSendRestoreEmailParams
                ),
            ),
            cast_to=NoneType,
        )


class AsyncPasswordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPasswordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPasswordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPasswordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncPasswordsResourceWithStreamingResponse(self)

    async def change(
        self,
        *,
        new_password: str | Omit = omit,
        old_password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Changes password

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/passwords",
            body=await async_maybe_transform(
                {
                    "new_password": new_password,
                    "old_password": old_password,
                },
                password_change_params.PasswordChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def reset(
        self,
        *,
        code: str | Omit = omit,
        new_password: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Resets password

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/passwords",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "new_password": new_password,
                    "user_id": user_id,
                },
                password_reset_params.PasswordResetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_restore_email(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Sends restore password email

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/passwords",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"email": email}, password_send_restore_email_params.PasswordSendRestoreEmailParams
                ),
            ),
            cast_to=NoneType,
        )


class PasswordsResourceWithRawResponse:
    def __init__(self, passwords: PasswordsResource) -> None:
        self._passwords = passwords

        self.change = to_raw_response_wrapper(
            passwords.change,
        )
        self.reset = to_raw_response_wrapper(
            passwords.reset,
        )
        self.send_restore_email = to_raw_response_wrapper(
            passwords.send_restore_email,
        )


class AsyncPasswordsResourceWithRawResponse:
    def __init__(self, passwords: AsyncPasswordsResource) -> None:
        self._passwords = passwords

        self.change = async_to_raw_response_wrapper(
            passwords.change,
        )
        self.reset = async_to_raw_response_wrapper(
            passwords.reset,
        )
        self.send_restore_email = async_to_raw_response_wrapper(
            passwords.send_restore_email,
        )


class PasswordsResourceWithStreamingResponse:
    def __init__(self, passwords: PasswordsResource) -> None:
        self._passwords = passwords

        self.change = to_streamed_response_wrapper(
            passwords.change,
        )
        self.reset = to_streamed_response_wrapper(
            passwords.reset,
        )
        self.send_restore_email = to_streamed_response_wrapper(
            passwords.send_restore_email,
        )


class AsyncPasswordsResourceWithStreamingResponse:
    def __init__(self, passwords: AsyncPasswordsResource) -> None:
        self._passwords = passwords

        self.change = async_to_streamed_response_wrapper(
            passwords.change,
        )
        self.reset = async_to_streamed_response_wrapper(
            passwords.reset,
        )
        self.send_restore_email = async_to_streamed_response_wrapper(
            passwords.send_restore_email,
        )
