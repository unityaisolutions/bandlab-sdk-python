# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ...types import (
    band_create_params,
    band_update_params,
    band_list_posts_params,
    band_list_songs_params,
)
from .invites import (
    InvitesResource,
    AsyncInvitesResource,
    InvitesResourceWithRawResponse,
    AsyncInvitesResourceWithRawResponse,
    InvitesResourceWithStreamingResponse,
    AsyncInvitesResourceWithStreamingResponse,
)
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
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
from ...types.band import Band
from ..._base_client import make_request_options
from ...types.post_list import PostList
from ...types.song_list import SongList
from ...types.genre_param import GenreParam
from ...types.creator_param import CreatorParam
from ...types.picture_param import PictureParam
from ...types.band_counters_param import BandCountersParam
from ...types.group_member_summary_param import GroupMemberSummaryParam

__all__ = ["BandsResource", "AsyncBandsResource"]


class BandsResource(SyncAPIResource):
    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def invites(self) -> InvitesResource:
        return InvitesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return BandsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        id: str | Omit = omit,
        about: str | Omit = omit,
        conversation_id: str | Omit = omit,
        counters: BandCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        genres: Iterable[GenreParam] | Omit = omit,
        is_open: bool | Omit = omit,
        members: Iterable[GroupMemberSummaryParam] | Omit = omit,
        picture: PictureParam | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Band:
        """
        Create a new band

        Args:
          genres

          members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/bands",
            body=maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "about": about,
                    "conversation_id": conversation_id,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "genres": genres,
                    "is_open": is_open,
                    "members": members,
                    "picture": picture,
                    "username": username,
                },
                band_create_params.BandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Band,
        )

    def retrieve(
        self,
        band_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Band:
        """
        Returns a single band

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not band_id:
            raise ValueError(f"Expected a non-empty value for `band_id` but received {band_id!r}")
        return self._get(
            f"/bands/{band_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Band,
        )

    def update(
        self,
        band_id: str,
        *,
        name: str,
        id: str | Omit = omit,
        about: str | Omit = omit,
        conversation_id: str | Omit = omit,
        counters: BandCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        genres: Iterable[GenreParam] | Omit = omit,
        is_open: bool | Omit = omit,
        members: Iterable[GroupMemberSummaryParam] | Omit = omit,
        picture: PictureParam | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Band:
        """
        Updates a band

        Args:
          genres

          members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not band_id:
            raise ValueError(f"Expected a non-empty value for `band_id` but received {band_id!r}")
        return self._patch(
            f"/bands/{band_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "about": about,
                    "conversation_id": conversation_id,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "genres": genres,
                    "is_open": is_open,
                    "members": members,
                    "picture": picture,
                    "username": username,
                },
                band_update_params.BandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Band,
        )

    def delete(
        self,
        band_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a band

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not band_id:
            raise ValueError(f"Expected a non-empty value for `band_id` but received {band_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/bands/{band_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_posts(
        self,
        band_id: str,
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
        if not band_id:
            raise ValueError(f"Expected a non-empty value for `band_id` but received {band_id!r}")
        return self._get(
            f"/bands/{band_id}/posts",
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
                    band_list_posts_params.BandListPostsParams,
                ),
            ),
            cast_to=PostList,
        )

    def list_songs(
        self,
        band_id: str,
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
    ) -> SongList:
        """
        Returns a list of songs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not band_id:
            raise ValueError(f"Expected a non-empty value for `band_id` but received {band_id!r}")
        return self._get(
            f"/bands/{band_id}/songs",
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
                    band_list_songs_params.BandListSongsParams,
                ),
            ),
            cast_to=SongList,
        )


class AsyncBandsResource(AsyncAPIResource):
    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def invites(self) -> AsyncInvitesResource:
        return AsyncInvitesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncBandsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        id: str | Omit = omit,
        about: str | Omit = omit,
        conversation_id: str | Omit = omit,
        counters: BandCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        genres: Iterable[GenreParam] | Omit = omit,
        is_open: bool | Omit = omit,
        members: Iterable[GroupMemberSummaryParam] | Omit = omit,
        picture: PictureParam | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Band:
        """
        Create a new band

        Args:
          genres

          members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/bands",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "about": about,
                    "conversation_id": conversation_id,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "genres": genres,
                    "is_open": is_open,
                    "members": members,
                    "picture": picture,
                    "username": username,
                },
                band_create_params.BandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Band,
        )

    async def retrieve(
        self,
        band_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Band:
        """
        Returns a single band

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not band_id:
            raise ValueError(f"Expected a non-empty value for `band_id` but received {band_id!r}")
        return await self._get(
            f"/bands/{band_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Band,
        )

    async def update(
        self,
        band_id: str,
        *,
        name: str,
        id: str | Omit = omit,
        about: str | Omit = omit,
        conversation_id: str | Omit = omit,
        counters: BandCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        genres: Iterable[GenreParam] | Omit = omit,
        is_open: bool | Omit = omit,
        members: Iterable[GroupMemberSummaryParam] | Omit = omit,
        picture: PictureParam | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Band:
        """
        Updates a band

        Args:
          genres

          members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not band_id:
            raise ValueError(f"Expected a non-empty value for `band_id` but received {band_id!r}")
        return await self._patch(
            f"/bands/{band_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "about": about,
                    "conversation_id": conversation_id,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "genres": genres,
                    "is_open": is_open,
                    "members": members,
                    "picture": picture,
                    "username": username,
                },
                band_update_params.BandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Band,
        )

    async def delete(
        self,
        band_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a band

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not band_id:
            raise ValueError(f"Expected a non-empty value for `band_id` but received {band_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/bands/{band_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_posts(
        self,
        band_id: str,
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
        if not band_id:
            raise ValueError(f"Expected a non-empty value for `band_id` but received {band_id!r}")
        return await self._get(
            f"/bands/{band_id}/posts",
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
                    band_list_posts_params.BandListPostsParams,
                ),
            ),
            cast_to=PostList,
        )

    async def list_songs(
        self,
        band_id: str,
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
    ) -> SongList:
        """
        Returns a list of songs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not band_id:
            raise ValueError(f"Expected a non-empty value for `band_id` but received {band_id!r}")
        return await self._get(
            f"/bands/{band_id}/songs",
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
                    band_list_songs_params.BandListSongsParams,
                ),
            ),
            cast_to=SongList,
        )


class BandsResourceWithRawResponse:
    def __init__(self, bands: BandsResource) -> None:
        self._bands = bands

        self.create = to_raw_response_wrapper(
            bands.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bands.retrieve,
        )
        self.update = to_raw_response_wrapper(
            bands.update,
        )
        self.delete = to_raw_response_wrapper(
            bands.delete,
        )
        self.list_posts = to_raw_response_wrapper(
            bands.list_posts,
        )
        self.list_songs = to_raw_response_wrapper(
            bands.list_songs,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._bands.members)

    @cached_property
    def invites(self) -> InvitesResourceWithRawResponse:
        return InvitesResourceWithRawResponse(self._bands.invites)


class AsyncBandsResourceWithRawResponse:
    def __init__(self, bands: AsyncBandsResource) -> None:
        self._bands = bands

        self.create = async_to_raw_response_wrapper(
            bands.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bands.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            bands.update,
        )
        self.delete = async_to_raw_response_wrapper(
            bands.delete,
        )
        self.list_posts = async_to_raw_response_wrapper(
            bands.list_posts,
        )
        self.list_songs = async_to_raw_response_wrapper(
            bands.list_songs,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._bands.members)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithRawResponse:
        return AsyncInvitesResourceWithRawResponse(self._bands.invites)


class BandsResourceWithStreamingResponse:
    def __init__(self, bands: BandsResource) -> None:
        self._bands = bands

        self.create = to_streamed_response_wrapper(
            bands.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bands.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            bands.update,
        )
        self.delete = to_streamed_response_wrapper(
            bands.delete,
        )
        self.list_posts = to_streamed_response_wrapper(
            bands.list_posts,
        )
        self.list_songs = to_streamed_response_wrapper(
            bands.list_songs,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._bands.members)

    @cached_property
    def invites(self) -> InvitesResourceWithStreamingResponse:
        return InvitesResourceWithStreamingResponse(self._bands.invites)


class AsyncBandsResourceWithStreamingResponse:
    def __init__(self, bands: AsyncBandsResource) -> None:
        self._bands = bands

        self.create = async_to_streamed_response_wrapper(
            bands.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bands.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            bands.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            bands.delete,
        )
        self.list_posts = async_to_streamed_response_wrapper(
            bands.list_posts,
        )
        self.list_songs = async_to_streamed_response_wrapper(
            bands.list_songs,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._bands.members)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithStreamingResponse:
        return AsyncInvitesResourceWithStreamingResponse(self._bands.invites)
