# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ...types import song_update_params, song_list_posts_params
from .invites import (
    InvitesResource,
    AsyncInvitesResource,
    InvitesResourceWithRawResponse,
    AsyncInvitesResourceWithRawResponse,
    InvitesResourceWithStreamingResponse,
    AsyncInvitesResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .revisions import (
    RevisionsResource,
    AsyncRevisionsResource,
    RevisionsResourceWithRawResponse,
    AsyncRevisionsResourceWithRawResponse,
    RevisionsResourceWithStreamingResponse,
    AsyncRevisionsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.song import Song
from .collaborators import (
    CollaboratorsResource,
    AsyncCollaboratorsResource,
    CollaboratorsResourceWithRawResponse,
    AsyncCollaboratorsResourceWithRawResponse,
    CollaboratorsResourceWithStreamingResponse,
    AsyncCollaboratorsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.post_list import PostList
from ...types.author_param import AuthorParam
from ...types.creator_param import CreatorParam
from ...types.picture_param import PictureParam
from ...types.song_counters_param import SongCountersParam
from ...types.song_original_param import SongOriginalParam

__all__ = ["SongsResource", "AsyncSongsResource"]


class SongsResource(SyncAPIResource):
    @cached_property
    def collaborators(self) -> CollaboratorsResource:
        return CollaboratorsResource(self._client)

    @cached_property
    def revisions(self) -> RevisionsResource:
        return RevisionsResource(self._client)

    @cached_property
    def invites(self) -> InvitesResource:
        return InvitesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SongsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SongsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SongsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return SongsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        song_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Song:
        """
        Returns a single song

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        return self._get(
            f"/songs/{song_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Song,
        )

    def update(
        self,
        song_id: str,
        *,
        name: str,
        id: str | Omit = omit,
        author: AuthorParam | Omit = omit,
        collaborators: Iterable[song_update_params.Collaborator] | Omit = omit,
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
        Updates a song

        Args:
          collaborators

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        return self._patch(
            f"/songs/{song_id}",
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
                song_update_params.SongUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Song,
        )

    def delete(
        self,
        song_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a song

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/songs/{song_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_posts(
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
    ) -> PostList:
        """
        Returns a list of posts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        return self._get(
            f"/song/{song_id}/posts",
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
                    song_list_posts_params.SongListPostsParams,
                ),
            ),
            cast_to=PostList,
        )


class AsyncSongsResource(AsyncAPIResource):
    @cached_property
    def collaborators(self) -> AsyncCollaboratorsResource:
        return AsyncCollaboratorsResource(self._client)

    @cached_property
    def revisions(self) -> AsyncRevisionsResource:
        return AsyncRevisionsResource(self._client)

    @cached_property
    def invites(self) -> AsyncInvitesResource:
        return AsyncInvitesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSongsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSongsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSongsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return AsyncSongsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        song_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Song:
        """
        Returns a single song

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        return await self._get(
            f"/songs/{song_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Song,
        )

    async def update(
        self,
        song_id: str,
        *,
        name: str,
        id: str | Omit = omit,
        author: AuthorParam | Omit = omit,
        collaborators: Iterable[song_update_params.Collaborator] | Omit = omit,
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
        Updates a song

        Args:
          collaborators

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        return await self._patch(
            f"/songs/{song_id}",
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
                song_update_params.SongUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Song,
        )

    async def delete(
        self,
        song_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a song

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/songs/{song_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_posts(
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
    ) -> PostList:
        """
        Returns a list of posts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not song_id:
            raise ValueError(f"Expected a non-empty value for `song_id` but received {song_id!r}")
        return await self._get(
            f"/song/{song_id}/posts",
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
                    song_list_posts_params.SongListPostsParams,
                ),
            ),
            cast_to=PostList,
        )


class SongsResourceWithRawResponse:
    def __init__(self, songs: SongsResource) -> None:
        self._songs = songs

        self.retrieve = to_raw_response_wrapper(
            songs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            songs.update,
        )
        self.delete = to_raw_response_wrapper(
            songs.delete,
        )
        self.list_posts = to_raw_response_wrapper(
            songs.list_posts,
        )

    @cached_property
    def collaborators(self) -> CollaboratorsResourceWithRawResponse:
        return CollaboratorsResourceWithRawResponse(self._songs.collaborators)

    @cached_property
    def revisions(self) -> RevisionsResourceWithRawResponse:
        return RevisionsResourceWithRawResponse(self._songs.revisions)

    @cached_property
    def invites(self) -> InvitesResourceWithRawResponse:
        return InvitesResourceWithRawResponse(self._songs.invites)


class AsyncSongsResourceWithRawResponse:
    def __init__(self, songs: AsyncSongsResource) -> None:
        self._songs = songs

        self.retrieve = async_to_raw_response_wrapper(
            songs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            songs.update,
        )
        self.delete = async_to_raw_response_wrapper(
            songs.delete,
        )
        self.list_posts = async_to_raw_response_wrapper(
            songs.list_posts,
        )

    @cached_property
    def collaborators(self) -> AsyncCollaboratorsResourceWithRawResponse:
        return AsyncCollaboratorsResourceWithRawResponse(self._songs.collaborators)

    @cached_property
    def revisions(self) -> AsyncRevisionsResourceWithRawResponse:
        return AsyncRevisionsResourceWithRawResponse(self._songs.revisions)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithRawResponse:
        return AsyncInvitesResourceWithRawResponse(self._songs.invites)


class SongsResourceWithStreamingResponse:
    def __init__(self, songs: SongsResource) -> None:
        self._songs = songs

        self.retrieve = to_streamed_response_wrapper(
            songs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            songs.update,
        )
        self.delete = to_streamed_response_wrapper(
            songs.delete,
        )
        self.list_posts = to_streamed_response_wrapper(
            songs.list_posts,
        )

    @cached_property
    def collaborators(self) -> CollaboratorsResourceWithStreamingResponse:
        return CollaboratorsResourceWithStreamingResponse(self._songs.collaborators)

    @cached_property
    def revisions(self) -> RevisionsResourceWithStreamingResponse:
        return RevisionsResourceWithStreamingResponse(self._songs.revisions)

    @cached_property
    def invites(self) -> InvitesResourceWithStreamingResponse:
        return InvitesResourceWithStreamingResponse(self._songs.invites)


class AsyncSongsResourceWithStreamingResponse:
    def __init__(self, songs: AsyncSongsResource) -> None:
        self._songs = songs

        self.retrieve = async_to_streamed_response_wrapper(
            songs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            songs.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            songs.delete,
        )
        self.list_posts = async_to_streamed_response_wrapper(
            songs.list_posts,
        )

    @cached_property
    def collaborators(self) -> AsyncCollaboratorsResourceWithStreamingResponse:
        return AsyncCollaboratorsResourceWithStreamingResponse(self._songs.collaborators)

    @cached_property
    def revisions(self) -> AsyncRevisionsResourceWithStreamingResponse:
        return AsyncRevisionsResourceWithStreamingResponse(self._songs.revisions)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithStreamingResponse:
        return AsyncInvitesResourceWithStreamingResponse(self._songs.invites)
