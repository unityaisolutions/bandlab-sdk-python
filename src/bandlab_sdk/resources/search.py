# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    search_search_bands_params,
    search_search_songs_params,
    search_search_users_params,
    search_global_search_params,
    search_search_collections_params,
)
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
from ..types.song_list import SongList
from ..types.collection_list import CollectionList
from ..types.users.user_list import UserList
from ..types.search_search_bands_response import SearchSearchBandsResponse
from ..types.search_global_search_response import SearchGlobalSearchResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def global_search(
        self,
        *,
        query: str,
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
    ) -> SearchGlobalSearchResponse:
        """
        Search global

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    search_global_search_params.SearchGlobalSearchParams,
                ),
            ),
            cast_to=SearchGlobalSearchResponse,
        )

    def search_bands(
        self,
        *,
        query: str,
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
    ) -> SearchSearchBandsResponse:
        """
        Search users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/bands",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    search_search_bands_params.SearchSearchBandsParams,
                ),
            ),
            cast_to=SearchSearchBandsResponse,
        )

    def search_collections(
        self,
        *,
        query: str,
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
    ) -> CollectionList:
        """
        Search users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    search_search_collections_params.SearchSearchCollectionsParams,
                ),
            ),
            cast_to=CollectionList,
        )

    def search_songs(
        self,
        *,
        query: str,
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
        Search users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/songs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    search_search_songs_params.SearchSearchSongsParams,
                ),
            ),
            cast_to=SongList,
        )

    def search_users(
        self,
        *,
        query: str,
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
    ) -> UserList:
        """
        Search users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    search_search_users_params.SearchSearchUsersParams,
                ),
            ),
            cast_to=UserList,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def global_search(
        self,
        *,
        query: str,
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
    ) -> SearchGlobalSearchResponse:
        """
        Search global

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    search_global_search_params.SearchGlobalSearchParams,
                ),
            ),
            cast_to=SearchGlobalSearchResponse,
        )

    async def search_bands(
        self,
        *,
        query: str,
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
    ) -> SearchSearchBandsResponse:
        """
        Search users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/bands",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    search_search_bands_params.SearchSearchBandsParams,
                ),
            ),
            cast_to=SearchSearchBandsResponse,
        )

    async def search_collections(
        self,
        *,
        query: str,
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
    ) -> CollectionList:
        """
        Search users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    search_search_collections_params.SearchSearchCollectionsParams,
                ),
            ),
            cast_to=CollectionList,
        )

    async def search_songs(
        self,
        *,
        query: str,
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
        Search users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/songs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    search_search_songs_params.SearchSearchSongsParams,
                ),
            ),
            cast_to=SongList,
        )

    async def search_users(
        self,
        *,
        query: str,
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
    ) -> UserList:
        """
        Search users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "offset": offset,
                    },
                    search_search_users_params.SearchSearchUsersParams,
                ),
            ),
            cast_to=UserList,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.global_search = to_raw_response_wrapper(
            search.global_search,
        )
        self.search_bands = to_raw_response_wrapper(
            search.search_bands,
        )
        self.search_collections = to_raw_response_wrapper(
            search.search_collections,
        )
        self.search_songs = to_raw_response_wrapper(
            search.search_songs,
        )
        self.search_users = to_raw_response_wrapper(
            search.search_users,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.global_search = async_to_raw_response_wrapper(
            search.global_search,
        )
        self.search_bands = async_to_raw_response_wrapper(
            search.search_bands,
        )
        self.search_collections = async_to_raw_response_wrapper(
            search.search_collections,
        )
        self.search_songs = async_to_raw_response_wrapper(
            search.search_songs,
        )
        self.search_users = async_to_raw_response_wrapper(
            search.search_users,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.global_search = to_streamed_response_wrapper(
            search.global_search,
        )
        self.search_bands = to_streamed_response_wrapper(
            search.search_bands,
        )
        self.search_collections = to_streamed_response_wrapper(
            search.search_collections,
        )
        self.search_songs = to_streamed_response_wrapper(
            search.search_songs,
        )
        self.search_users = to_streamed_response_wrapper(
            search.search_users,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.global_search = async_to_streamed_response_wrapper(
            search.global_search,
        )
        self.search_bands = async_to_streamed_response_wrapper(
            search.search_bands,
        )
        self.search_collections = async_to_streamed_response_wrapper(
            search.search_collections,
        )
        self.search_songs = async_to_streamed_response_wrapper(
            search.search_songs,
        )
        self.search_users = async_to_streamed_response_wrapper(
            search.search_users,
        )
