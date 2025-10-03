# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.skill_list_response import SkillListResponse

__all__ = ["SkillsResource", "AsyncSkillsResource"]


class SkillsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SkillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return SkillsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillListResponse:
        """Returns all skills"""
        return self._get(
            "/skills",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillListResponse,
        )


class AsyncSkillsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSkillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return AsyncSkillsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillListResponse:
        """Returns all skills"""
        return await self._get(
            "/skills",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillListResponse,
        )


class SkillsResourceWithRawResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.list = to_raw_response_wrapper(
            skills.list,
        )


class AsyncSkillsResourceWithRawResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.list = async_to_raw_response_wrapper(
            skills.list,
        )


class SkillsResourceWithStreamingResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.list = to_streamed_response_wrapper(
            skills.list,
        )


class AsyncSkillsResourceWithStreamingResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.list = async_to_streamed_response_wrapper(
            skills.list,
        )
