# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.emails import confirmation_confirm_params

__all__ = ["ConfirmationsResource", "AsyncConfirmationsResource"]


class ConfirmationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfirmationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConfirmationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfirmationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return ConfirmationsResourceWithStreamingResponse(self)

    def confirm(
        self,
        *,
        code: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Confirms an email

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/emails/confirmations",
            body=maybe_transform(
                {
                    "code": code,
                    "user_id": user_id,
                },
                confirmation_confirm_params.ConfirmationConfirmParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def resend(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Resends the email confirmation"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/emails/confirmations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncConfirmationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfirmationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfirmationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfirmationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return AsyncConfirmationsResourceWithStreamingResponse(self)

    async def confirm(
        self,
        *,
        code: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Confirms an email

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/emails/confirmations",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "user_id": user_id,
                },
                confirmation_confirm_params.ConfirmationConfirmParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def resend(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Resends the email confirmation"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/emails/confirmations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ConfirmationsResourceWithRawResponse:
    def __init__(self, confirmations: ConfirmationsResource) -> None:
        self._confirmations = confirmations

        self.confirm = to_raw_response_wrapper(
            confirmations.confirm,
        )
        self.resend = to_raw_response_wrapper(
            confirmations.resend,
        )


class AsyncConfirmationsResourceWithRawResponse:
    def __init__(self, confirmations: AsyncConfirmationsResource) -> None:
        self._confirmations = confirmations

        self.confirm = async_to_raw_response_wrapper(
            confirmations.confirm,
        )
        self.resend = async_to_raw_response_wrapper(
            confirmations.resend,
        )


class ConfirmationsResourceWithStreamingResponse:
    def __init__(self, confirmations: ConfirmationsResource) -> None:
        self._confirmations = confirmations

        self.confirm = to_streamed_response_wrapper(
            confirmations.confirm,
        )
        self.resend = to_streamed_response_wrapper(
            confirmations.resend,
        )


class AsyncConfirmationsResourceWithStreamingResponse:
    def __init__(self, confirmations: AsyncConfirmationsResource) -> None:
        self._confirmations = confirmations

        self.confirm = async_to_streamed_response_wrapper(
            confirmations.confirm,
        )
        self.resend = async_to_streamed_response_wrapper(
            confirmations.resend,
        )
