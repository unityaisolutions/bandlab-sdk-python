# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

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
from ..._base_client import make_request_options
from ...types.post_list import PostList
from ...types.collections import ClientID
from ...types.communities import post_list_params, post_create_params
from ...types.creator_param import CreatorParam
from ...types.collections.post import Post
from ...types.posts.comment_param import CommentParam
from ...types.collections.client_id import ClientID

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return PostsResourceWithStreamingResponse(self)

    def create(
        self,
        community_id: str,
        *,
        id: str | Omit = omit,
        caption: str | Omit = omit,
        client_id: ClientID | Omit = omit,
        comments: Iterable[CommentParam] | Omit = omit,
        counters: post_create_params.Counters | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        image: post_create_params.Image | Omit = omit,
        message: str | Omit = omit,
        revision: post_create_params.Revision | Omit = omit,
        type: Literal["Revision", "Image", "Video", "Text"] | Omit = omit,
        video: post_create_params.Video | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Post:
        """
        Create a text post

        Args:
          comments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return self._post(
            f"/community/{community_id}/posts",
            body=maybe_transform(
                {
                    "id": id,
                    "caption": caption,
                    "client_id": client_id,
                    "comments": comments,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "image": image,
                    "message": message,
                    "revision": revision,
                    "type": type,
                    "video": video,
                },
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Post,
        )

    def list(
        self,
        community_id: str,
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
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return self._get(
            f"/community/{community_id}/posts",
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
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=PostList,
        )


class AsyncPostsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncPostsResourceWithStreamingResponse(self)

    async def create(
        self,
        community_id: str,
        *,
        id: str | Omit = omit,
        caption: str | Omit = omit,
        client_id: ClientID | Omit = omit,
        comments: Iterable[CommentParam] | Omit = omit,
        counters: post_create_params.Counters | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        image: post_create_params.Image | Omit = omit,
        message: str | Omit = omit,
        revision: post_create_params.Revision | Omit = omit,
        type: Literal["Revision", "Image", "Video", "Text"] | Omit = omit,
        video: post_create_params.Video | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Post:
        """
        Create a text post

        Args:
          comments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return await self._post(
            f"/community/{community_id}/posts",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "caption": caption,
                    "client_id": client_id,
                    "comments": comments,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "image": image,
                    "message": message,
                    "revision": revision,
                    "type": type,
                    "video": video,
                },
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Post,
        )

    async def list(
        self,
        community_id: str,
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
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return await self._get(
            f"/community/{community_id}/posts",
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
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=PostList,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_raw_response_wrapper(
            posts.create,
        )
        self.list = to_raw_response_wrapper(
            posts.list,
        )


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_raw_response_wrapper(
            posts.create,
        )
        self.list = async_to_raw_response_wrapper(
            posts.list,
        )


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_streamed_response_wrapper(
            posts.create,
        )
        self.list = to_streamed_response_wrapper(
            posts.list,
        )


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_streamed_response_wrapper(
            posts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            posts.list,
        )
