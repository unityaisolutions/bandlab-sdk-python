# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from .posts import (
    PostsResource,
    AsyncPostsResource,
    PostsResourceWithRawResponse,
    AsyncPostsResourceWithRawResponse,
    PostsResourceWithStreamingResponse,
    AsyncPostsResourceWithStreamingResponse,
)
from ...types import Type, community_create_params, community_update_params
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
from ...types.type import Type
from ..._base_client import make_request_options
from ...types.community import Community
from ...types.creator_param import CreatorParam
from ...types.picture_param import PictureParam
from ...types.community_counters_param import CommunityCountersParam
from ...types.group_member_summary_param import GroupMemberSummaryParam

__all__ = ["CommunitiesResource", "AsyncCommunitiesResource"]


class CommunitiesResource(SyncAPIResource):
    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def posts(self) -> PostsResource:
        return PostsResource(self._client)

    @cached_property
    def invites(self) -> InvitesResource:
        return InvitesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CommunitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CommunitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommunitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return CommunitiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        id: str | Omit = omit,
        about: str | Omit = omit,
        counters: CommunityCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        is_comments_enabled: bool | Omit = omit,
        members: Iterable[GroupMemberSummaryParam] | Omit = omit,
        picture: PictureParam | Omit = omit,
        type: Type | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Community:
        """
        Create a new community

        Args:
          members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communities",
            body=maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "about": about,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "is_comments_enabled": is_comments_enabled,
                    "members": members,
                    "picture": picture,
                    "type": type,
                    "username": username,
                },
                community_create_params.CommunityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Community,
        )

    def retrieve(
        self,
        community_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Community:
        """
        Returns a single community

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return self._get(
            f"/communities/{community_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Community,
        )

    def update(
        self,
        community_id: str,
        *,
        name: str,
        id: str | Omit = omit,
        about: str | Omit = omit,
        counters: CommunityCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        is_comments_enabled: bool | Omit = omit,
        members: Iterable[GroupMemberSummaryParam] | Omit = omit,
        picture: PictureParam | Omit = omit,
        type: Type | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Community:
        """
        Updates a community

        Args:
          members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return self._patch(
            f"/communities/{community_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "about": about,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "is_comments_enabled": is_comments_enabled,
                    "members": members,
                    "picture": picture,
                    "type": type,
                    "username": username,
                },
                community_update_params.CommunityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Community,
        )

    def delete(
        self,
        community_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a community

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/communities/{community_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCommunitiesResource(AsyncAPIResource):
    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def posts(self) -> AsyncPostsResource:
        return AsyncPostsResource(self._client)

    @cached_property
    def invites(self) -> AsyncInvitesResource:
        return AsyncInvitesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCommunitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommunitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommunitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/bandlab-sdk-python#with_streaming_response
        """
        return AsyncCommunitiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        id: str | Omit = omit,
        about: str | Omit = omit,
        counters: CommunityCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        is_comments_enabled: bool | Omit = omit,
        members: Iterable[GroupMemberSummaryParam] | Omit = omit,
        picture: PictureParam | Omit = omit,
        type: Type | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Community:
        """
        Create a new community

        Args:
          members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communities",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "about": about,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "is_comments_enabled": is_comments_enabled,
                    "members": members,
                    "picture": picture,
                    "type": type,
                    "username": username,
                },
                community_create_params.CommunityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Community,
        )

    async def retrieve(
        self,
        community_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Community:
        """
        Returns a single community

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return await self._get(
            f"/communities/{community_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Community,
        )

    async def update(
        self,
        community_id: str,
        *,
        name: str,
        id: str | Omit = omit,
        about: str | Omit = omit,
        counters: CommunityCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        is_comments_enabled: bool | Omit = omit,
        members: Iterable[GroupMemberSummaryParam] | Omit = omit,
        picture: PictureParam | Omit = omit,
        type: Type | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Community:
        """
        Updates a community

        Args:
          members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return await self._patch(
            f"/communities/{community_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "about": about,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "is_comments_enabled": is_comments_enabled,
                    "members": members,
                    "picture": picture,
                    "type": type,
                    "username": username,
                },
                community_update_params.CommunityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Community,
        )

    async def delete(
        self,
        community_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a community

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/communities/{community_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CommunitiesResourceWithRawResponse:
    def __init__(self, communities: CommunitiesResource) -> None:
        self._communities = communities

        self.create = to_raw_response_wrapper(
            communities.create,
        )
        self.retrieve = to_raw_response_wrapper(
            communities.retrieve,
        )
        self.update = to_raw_response_wrapper(
            communities.update,
        )
        self.delete = to_raw_response_wrapper(
            communities.delete,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._communities.members)

    @cached_property
    def posts(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self._communities.posts)

    @cached_property
    def invites(self) -> InvitesResourceWithRawResponse:
        return InvitesResourceWithRawResponse(self._communities.invites)


class AsyncCommunitiesResourceWithRawResponse:
    def __init__(self, communities: AsyncCommunitiesResource) -> None:
        self._communities = communities

        self.create = async_to_raw_response_wrapper(
            communities.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            communities.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            communities.update,
        )
        self.delete = async_to_raw_response_wrapper(
            communities.delete,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._communities.members)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self._communities.posts)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithRawResponse:
        return AsyncInvitesResourceWithRawResponse(self._communities.invites)


class CommunitiesResourceWithStreamingResponse:
    def __init__(self, communities: CommunitiesResource) -> None:
        self._communities = communities

        self.create = to_streamed_response_wrapper(
            communities.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            communities.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            communities.update,
        )
        self.delete = to_streamed_response_wrapper(
            communities.delete,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._communities.members)

    @cached_property
    def posts(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self._communities.posts)

    @cached_property
    def invites(self) -> InvitesResourceWithStreamingResponse:
        return InvitesResourceWithStreamingResponse(self._communities.invites)


class AsyncCommunitiesResourceWithStreamingResponse:
    def __init__(self, communities: AsyncCommunitiesResource) -> None:
        self._communities = communities

        self.create = async_to_streamed_response_wrapper(
            communities.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            communities.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            communities.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            communities.delete,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._communities.members)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self._communities.posts)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithStreamingResponse:
        return AsyncInvitesResourceWithStreamingResponse(self._communities.invites)
