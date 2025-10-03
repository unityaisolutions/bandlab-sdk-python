# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.users import recommendation_list_users_params
from ..._base_client import make_request_options
from ...types.collections.user_summary_list import UserSummaryList

__all__ = ["RecommendationsResource", "AsyncRecommendationsResource"]


class RecommendationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecommendationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RecommendationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecommendationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return RecommendationsResourceWithStreamingResponse(self)

    def list_users(
        self,
        user_id: str,
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
    ) -> UserSummaryList:
        """
        Returns a recommended users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/users/{user_id}/recommendations/users",
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
                    recommendation_list_users_params.RecommendationListUsersParams,
                ),
            ),
            cast_to=UserSummaryList,
        )


class AsyncRecommendationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecommendationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecommendationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecommendationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncRecommendationsResourceWithStreamingResponse(self)

    async def list_users(
        self,
        user_id: str,
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
    ) -> UserSummaryList:
        """
        Returns a recommended users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/users/{user_id}/recommendations/users",
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
                    recommendation_list_users_params.RecommendationListUsersParams,
                ),
            ),
            cast_to=UserSummaryList,
        )


class RecommendationsResourceWithRawResponse:
    def __init__(self, recommendations: RecommendationsResource) -> None:
        self._recommendations = recommendations

        self.list_users = to_raw_response_wrapper(
            recommendations.list_users,
        )


class AsyncRecommendationsResourceWithRawResponse:
    def __init__(self, recommendations: AsyncRecommendationsResource) -> None:
        self._recommendations = recommendations

        self.list_users = async_to_raw_response_wrapper(
            recommendations.list_users,
        )


class RecommendationsResourceWithStreamingResponse:
    def __init__(self, recommendations: RecommendationsResource) -> None:
        self._recommendations = recommendations

        self.list_users = to_streamed_response_wrapper(
            recommendations.list_users,
        )


class AsyncRecommendationsResourceWithStreamingResponse:
    def __init__(self, recommendations: AsyncRecommendationsResource) -> None:
        self._recommendations = recommendations

        self.list_users = async_to_streamed_response_wrapper(
            recommendations.list_users,
        )
