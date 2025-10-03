# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .confirmations import (
    ConfirmationsResource,
    AsyncConfirmationsResource,
    ConfirmationsResourceWithRawResponse,
    AsyncConfirmationsResourceWithRawResponse,
    ConfirmationsResourceWithStreamingResponse,
    AsyncConfirmationsResourceWithStreamingResponse,
)

__all__ = ["EmailsResource", "AsyncEmailsResource"]


class EmailsResource(SyncAPIResource):
    @cached_property
    def confirmations(self) -> ConfirmationsResource:
        return ConfirmationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return EmailsResourceWithStreamingResponse(self)


class AsyncEmailsResource(AsyncAPIResource):
    @cached_property
    def confirmations(self) -> AsyncConfirmationsResource:
        return AsyncConfirmationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncEmailsResourceWithStreamingResponse(self)


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

    @cached_property
    def confirmations(self) -> ConfirmationsResourceWithRawResponse:
        return ConfirmationsResourceWithRawResponse(self._emails.confirmations)


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

    @cached_property
    def confirmations(self) -> AsyncConfirmationsResourceWithRawResponse:
        return AsyncConfirmationsResourceWithRawResponse(self._emails.confirmations)


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

    @cached_property
    def confirmations(self) -> ConfirmationsResourceWithStreamingResponse:
        return ConfirmationsResourceWithStreamingResponse(self._emails.confirmations)


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

    @cached_property
    def confirmations(self) -> AsyncConfirmationsResourceWithStreamingResponse:
        return AsyncConfirmationsResourceWithStreamingResponse(self._emails.confirmations)
