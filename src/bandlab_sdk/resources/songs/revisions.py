# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.song import Song
from ...types.songs import revision_list_params, revision_forks_params
from ..._base_client import make_request_options
from ...types.author_param import AuthorParam
from ...types.creator_param import CreatorParam
from ...types.picture_param import PictureParam
from ...types.song_counters_param import SongCountersParam
from ...types.song_original_param import SongOriginalParam
from ...types.songs.revision_list_response import RevisionListResponse

__all__ = ["RevisionsResource", "AsyncRevisionsResource"]


class RevisionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return RevisionsResourceWithStreamingResponse(self)

    def list(
        self,
        song_id: str,
        *,
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
    ) -> RevisionListResponse:
        """
        Returns a list of revisions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        return self._get(
            f"/songs/{song_id}/revisions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    revision_list_params.RevisionListParams,
                ),
            ),
            cast_to=RevisionListResponse,
        )

    def forks(
        self,
        revison_id: str,
        *,
        song_id: str,
        name: str,
        id: str | Omit = omit,
        author: AuthorParam | Omit = omit,
        collaborators: Iterable[revision_forks_params.Collaborator] | Omit = omit,
        counters: SongCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        description: str | Omit = omit,
        is_fork: bool | Omit = omit,
        is_forkable: bool | Omit = omit,
        is_public: bool | Omit = omit,
        modified_on: Union[str, datetime] | Omit = omit,
        original: SongOriginalParam | Omit = omit,
        picture: PictureParam | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Song:
        """
        Create a fork

        Args:
          collaborators

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        if not revison_id:
            raise ValueError(f"Expected a non-empty value for `revison_id` but received {revison_id!r}")
        return self._post(
            f"/songs/{song_id}/revisions/{revison_id}/forks",
            body=maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "author": author,
                    "collaborators": collaborators,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "description": description,
                    "is_fork": is_fork,
                    "is_forkable": is_forkable,
                    "is_public": is_public,
                    "modified_on": modified_on,
                    "original": original,
                    "picture": picture,
                    "slug": slug,
                },
                revision_forks_params.RevisionForksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Song,
        )


class AsyncRevisionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return AsyncRevisionsResourceWithStreamingResponse(self)

    async def list(
        self,
        song_id: str,
        *,
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
    ) -> RevisionListResponse:
        """
        Returns a list of revisions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        return await self._get(
            f"/songs/{song_id}/revisions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    revision_list_params.RevisionListParams,
                ),
            ),
            cast_to=RevisionListResponse,
        )

    async def forks(
        self,
        revison_id: str,
        *,
        song_id: str,
        name: str,
        id: str | Omit = omit,
        author: AuthorParam | Omit = omit,
        collaborators: Iterable[revision_forks_params.Collaborator] | Omit = omit,
        counters: SongCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        description: str | Omit = omit,
        is_fork: bool | Omit = omit,
        is_forkable: bool | Omit = omit,
        is_public: bool | Omit = omit,
        modified_on: Union[str, datetime] | Omit = omit,
        original: SongOriginalParam | Omit = omit,
        picture: PictureParam | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Song:
        """
        Create a fork

        Args:
          collaborators

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        if not revison_id:
            raise ValueError(f"Expected a non-empty value for `revison_id` but received {revison_id!r}")
        return await self._post(
            f"/songs/{song_id}/revisions/{revison_id}/forks",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "author": author,
                    "collaborators": collaborators,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "description": description,
                    "is_fork": is_fork,
                    "is_forkable": is_forkable,
                    "is_public": is_public,
                    "modified_on": modified_on,
                    "original": original,
                    "picture": picture,
                    "slug": slug,
                },
                revision_forks_params.RevisionForksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Song,
        )


class RevisionsResourceWithRawResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.list = to_raw_response_wrapper(
            revisions.list,
        )
        self.forks = to_raw_response_wrapper(
            revisions.forks,
        )


class AsyncRevisionsResourceWithRawResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.list = async_to_raw_response_wrapper(
            revisions.list,
        )
        self.forks = async_to_raw_response_wrapper(
            revisions.forks,
        )


class RevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.list = to_streamed_response_wrapper(
            revisions.list,
        )
        self.forks = to_streamed_response_wrapper(
            revisions.forks,
        )


class AsyncRevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.list = async_to_streamed_response_wrapper(
            revisions.list,
        )
        self.forks = async_to_streamed_response_wrapper(
            revisions.forks,
        )
