# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

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
from ...types.posts import comment_list_params, comment_create_params
from ..._base_client import make_request_options
from ...types.creator_param import CreatorParam
from ...types.posts.comment import Comment
from ...types.posts.comment_list_response import CommentListResponse

__all__ = ["CommentsResource", "AsyncCommentsResource"]


class CommentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return CommentsResourceWithStreamingResponse(self)

    def create(
        self,
        post_id: str,
        *,
        id: int | Omit = omit,
        content: str | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        timestamp: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Comment:
        """
        Creates a comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._post(
            f"/posts/{post_id}/comments",
            body=maybe_transform(
                {
                    "id": id,
                    "content": content,
                    "created_on": created_on,
                    "creator": creator,
                    "timestamp": timestamp,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Comment,
        )

    def list(
        self,
        post_id: str,
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
    ) -> CommentListResponse:
        """
        Returns list of comments

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._get(
            f"/posts/{post_id}/comments",
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
                    comment_list_params.CommentListParams,
                ),
            ),
            cast_to=CommentListResponse,
        )

    def delete(
        self,
        comment_id: int,
        *,
        post_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/posts/{post_id}/comments/{comment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCommentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncCommentsResourceWithStreamingResponse(self)

    async def create(
        self,
        post_id: str,
        *,
        id: int | Omit = omit,
        content: str | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        timestamp: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Comment:
        """
        Creates a comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._post(
            f"/posts/{post_id}/comments",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "content": content,
                    "created_on": created_on,
                    "creator": creator,
                    "timestamp": timestamp,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Comment,
        )

    async def list(
        self,
        post_id: str,
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
    ) -> CommentListResponse:
        """
        Returns list of comments

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._get(
            f"/posts/{post_id}/comments",
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
                    comment_list_params.CommentListParams,
                ),
            ),
            cast_to=CommentListResponse,
        )

    async def delete(
        self,
        comment_id: int,
        *,
        post_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/posts/{post_id}/comments/{comment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CommentsResourceWithRawResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create = to_raw_response_wrapper(
            comments.create,
        )
        self.list = to_raw_response_wrapper(
            comments.list,
        )
        self.delete = to_raw_response_wrapper(
            comments.delete,
        )


class AsyncCommentsResourceWithRawResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create = async_to_raw_response_wrapper(
            comments.create,
        )
        self.list = async_to_raw_response_wrapper(
            comments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            comments.delete,
        )


class CommentsResourceWithStreamingResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create = to_streamed_response_wrapper(
            comments.create,
        )
        self.list = to_streamed_response_wrapper(
            comments.list,
        )
        self.delete = to_streamed_response_wrapper(
            comments.delete,
        )


class AsyncCommentsResourceWithStreamingResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create = async_to_streamed_response_wrapper(
            comments.create,
        )
        self.list = async_to_streamed_response_wrapper(
            comments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            comments.delete,
        )
