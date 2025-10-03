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
from ...types.songs import collaborator_list_params
from ..._base_client import make_request_options
from ...types.songs.collaborator_list_response import CollaboratorListResponse

__all__ = ["CollaboratorsResource", "AsyncCollaboratorsResource"]


class CollaboratorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollaboratorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CollaboratorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollaboratorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return CollaboratorsResourceWithStreamingResponse(self)

    def list(
        self,
        song_id: str,
        *,
        community_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollaboratorListResponse:
        """
        Returns members of a band

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        return self._get(
            f"/songs/{song_id}/collaborators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "community_id": community_id,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    collaborator_list_params.CollaboratorListParams,
                ),
            ),
            cast_to=CollaboratorListResponse,
        )

    def remove(
        self,
        user_id: str,
        *,
        song_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a collaborator

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/songs/{song_id}/collaborators/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCollaboratorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollaboratorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollaboratorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollaboratorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return AsyncCollaboratorsResourceWithStreamingResponse(self)

    async def list(
        self,
        song_id: str,
        *,
        community_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollaboratorListResponse:
        """
        Returns members of a band

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        return await self._get(
            f"/songs/{song_id}/collaborators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "community_id": community_id,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    collaborator_list_params.CollaboratorListParams,
                ),
            ),
            cast_to=CollaboratorListResponse,
        )

    async def remove(
        self,
        user_id: str,
        *,
        song_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a collaborator

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/songs/{song_id}/collaborators/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CollaboratorsResourceWithRawResponse:
    def __init__(self, collaborators: CollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = to_raw_response_wrapper(
            collaborators.list,
        )
        self.remove = to_raw_response_wrapper(
            collaborators.remove,
        )


class AsyncCollaboratorsResourceWithRawResponse:
    def __init__(self, collaborators: AsyncCollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = async_to_raw_response_wrapper(
            collaborators.list,
        )
        self.remove = async_to_raw_response_wrapper(
            collaborators.remove,
        )


class CollaboratorsResourceWithStreamingResponse:
    def __init__(self, collaborators: CollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = to_streamed_response_wrapper(
            collaborators.list,
        )
        self.remove = to_streamed_response_wrapper(
            collaborators.remove,
        )


class AsyncCollaboratorsResourceWithStreamingResponse:
    def __init__(self, collaborators: AsyncCollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = async_to_streamed_response_wrapper(
            collaborators.list,
        )
        self.remove = async_to_streamed_response_wrapper(
            collaborators.remove,
        )
