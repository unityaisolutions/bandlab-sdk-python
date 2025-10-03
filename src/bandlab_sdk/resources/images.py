# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import image_create_post_params
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
from ..types.collections import ClientID
from ..types.creator_param import CreatorParam
from ..types.collections.post import Post
from ..types.posts.comment_param import CommentParam
from ..types.collections.client_id import ClientID
from ..types.shared_params.image_sample import ImageSample
from ..types.shared_params.video_sample import VideoSample
from ..types.shared_params.post_counters import PostCounters
from ..types.shared_params.revision_summary import RevisionSummary

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return ImagesResourceWithStreamingResponse(self)

    def create_post(
        self,
        image_id: str,
        *,
        id: str | Omit = omit,
        caption: str | Omit = omit,
        client_id: ClientID | Omit = omit,
        comments: Iterable[CommentParam] | Omit = omit,
        counters: PostCounters | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        image: ImageSample | Omit = omit,
        message: str | Omit = omit,
        revision: RevisionSummary | Omit = omit,
        type: Literal["Revision", "Image", "Video", "Text"] | Omit = omit,
        video: VideoSample | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Post:
        """
        Create a image post

        Args:
          comments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._post(
            f"/images/{image_id}/posts",
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
                image_create_post_params.ImageCreatePostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Post,
        )


class AsyncImagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncImagesResourceWithStreamingResponse(self)

    async def create_post(
        self,
        image_id: str,
        *,
        id: str | Omit = omit,
        caption: str | Omit = omit,
        client_id: ClientID | Omit = omit,
        comments: Iterable[CommentParam] | Omit = omit,
        counters: PostCounters | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        image: ImageSample | Omit = omit,
        message: str | Omit = omit,
        revision: RevisionSummary | Omit = omit,
        type: Literal["Revision", "Image", "Video", "Text"] | Omit = omit,
        video: VideoSample | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Post:
        """
        Create a image post

        Args:
          comments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._post(
            f"/images/{image_id}/posts",
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
                image_create_post_params.ImageCreatePostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Post,
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.create_post = to_raw_response_wrapper(
            images.create_post,
        )


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.create_post = async_to_raw_response_wrapper(
            images.create_post,
        )


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.create_post = to_streamed_response_wrapper(
            images.create_post,
        )


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.create_post = async_to_streamed_response_wrapper(
            images.create_post,
        )
