# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .registrations import (
    RegistrationsResource,
    AsyncRegistrationsResource,
    RegistrationsResourceWithRawResponse,
    AsyncRegistrationsResourceWithRawResponse,
    RegistrationsResourceWithStreamingResponse,
    AsyncRegistrationsResourceWithStreamingResponse,
)

__all__ = ["PushResource", "AsyncPushResource"]


class PushResource(SyncAPIResource):
    @cached_property
    def registrations(self) -> RegistrationsResource:
        return RegistrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PushResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PushResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PushResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return PushResourceWithStreamingResponse(self)


class AsyncPushResource(AsyncAPIResource):
    @cached_property
    def registrations(self) -> AsyncRegistrationsResource:
        return AsyncRegistrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPushResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPushResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPushResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return AsyncPushResourceWithStreamingResponse(self)


class PushResourceWithRawResponse:
    def __init__(self, push: PushResource) -> None:
        self._push = push

    @cached_property
    def registrations(self) -> RegistrationsResourceWithRawResponse:
        return RegistrationsResourceWithRawResponse(self._push.registrations)


class AsyncPushResourceWithRawResponse:
    def __init__(self, push: AsyncPushResource) -> None:
        self._push = push

    @cached_property
    def registrations(self) -> AsyncRegistrationsResourceWithRawResponse:
        return AsyncRegistrationsResourceWithRawResponse(self._push.registrations)


class PushResourceWithStreamingResponse:
    def __init__(self, push: PushResource) -> None:
        self._push = push

    @cached_property
    def registrations(self) -> RegistrationsResourceWithStreamingResponse:
        return RegistrationsResourceWithStreamingResponse(self._push.registrations)


class AsyncPushResourceWithStreamingResponse:
    def __init__(self, push: AsyncPushResource) -> None:
        self._push = push

    @cached_property
    def registrations(self) -> AsyncRegistrationsResourceWithStreamingResponse:
        return AsyncRegistrationsResourceWithStreamingResponse(self._push.registrations)
