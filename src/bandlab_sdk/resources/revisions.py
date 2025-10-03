# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ..types import (
    revision_create_params,
    revision_update_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.revision import Revision
from ..types.collections import ClientID
from ..types.genre_param import GenreParam
from ..types.creator_param import CreatorParam
from ..types.mastering_param import MasteringParam
from ..types.audio_sample_param import AudioSampleParam
from ..types.song_summary_param import SongSummaryParam
from ..types.collections.client_id import ClientID
from ..types.revision_counters_param import RevisionCountersParam

__all__ = ["RevisionsResource", "AsyncRevisionsResource"]


class RevisionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return RevisionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str | Omit = omit,
        aux_channels: Iterable[revision_create_params.AuxChannel] | Omit = omit,
        client_id: ClientID | Omit = omit,
        counters: RevisionCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        description: str | Omit = omit,
        genres: Iterable[GenreParam] | Omit = omit,
        is_fork: bool | Omit = omit,
        is_public: bool | Omit = omit,
        key: str | Omit = omit,
        mastering: MasteringParam | Omit = omit,
        mixdown: AudioSampleParam | Omit = omit,
        modified_on: Union[str, datetime] | Omit = omit,
        parent_id: str | Omit = omit,
        post_id: str | Omit = omit,
        samples: Iterable[AudioSampleParam] | Omit = omit,
        song: SongSummaryParam | Omit = omit,
        stamp: str | Omit = omit,
        tracks: Iterable[AudioSampleParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Revision:
        """
        Create a new revision

        Args:
          aux_channels

          genres

          samples

          tracks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/revisions",
            body=maybe_transform(
                {
                    "id": id,
                    "aux_channels": aux_channels,
                    "client_id": client_id,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "description": description,
                    "genres": genres,
                    "is_fork": is_fork,
                    "is_public": is_public,
                    "key": key,
                    "mastering": mastering,
                    "mixdown": mixdown,
                    "modified_on": modified_on,
                    "parent_id": parent_id,
                    "post_id": post_id,
                    "samples": samples,
                    "song": song,
                    "stamp": stamp,
                    "tracks": tracks,
                },
                revision_create_params.RevisionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Revision,
        )

    def retrieve(
        self,
        revision_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Revision:
        """
        Returns a single revision

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            f"/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Revision,
        )

    def update(
        self,
        revision_id: str,
        *,
        id: str | Omit = omit,
        aux_channels: Iterable[revision_update_params.AuxChannel] | Omit = omit,
        client_id: ClientID | Omit = omit,
        counters: RevisionCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        description: str | Omit = omit,
        genres: Iterable[GenreParam] | Omit = omit,
        is_fork: bool | Omit = omit,
        is_public: bool | Omit = omit,
        key: str | Omit = omit,
        mastering: MasteringParam | Omit = omit,
        mixdown: AudioSampleParam | Omit = omit,
        modified_on: Union[str, datetime] | Omit = omit,
        parent_id: str | Omit = omit,
        post_id: str | Omit = omit,
        samples: Iterable[AudioSampleParam] | Omit = omit,
        song: SongSummaryParam | Omit = omit,
        stamp: str | Omit = omit,
        tracks: Iterable[AudioSampleParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Revision:
        """
        Updates a revision

        Args:
          aux_channels

          genres

          samples

          tracks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._patch(
            f"/revisions/{revision_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "aux_channels": aux_channels,
                    "client_id": client_id,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "description": description,
                    "genres": genres,
                    "is_fork": is_fork,
                    "is_public": is_public,
                    "key": key,
                    "mastering": mastering,
                    "mixdown": mixdown,
                    "modified_on": modified_on,
                    "parent_id": parent_id,
                    "post_id": post_id,
                    "samples": samples,
                    "song": song,
                    "stamp": stamp,
                    "tracks": tracks,
                },
                revision_update_params.RevisionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Revision,
        )

    def add_play(
        self,
        revision_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add a play

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/revisions/{revision_id}/plays",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRevisionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncRevisionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str | Omit = omit,
        aux_channels: Iterable[revision_create_params.AuxChannel] | Omit = omit,
        client_id: ClientID | Omit = omit,
        counters: RevisionCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        description: str | Omit = omit,
        genres: Iterable[GenreParam] | Omit = omit,
        is_fork: bool | Omit = omit,
        is_public: bool | Omit = omit,
        key: str | Omit = omit,
        mastering: MasteringParam | Omit = omit,
        mixdown: AudioSampleParam | Omit = omit,
        modified_on: Union[str, datetime] | Omit = omit,
        parent_id: str | Omit = omit,
        post_id: str | Omit = omit,
        samples: Iterable[AudioSampleParam] | Omit = omit,
        song: SongSummaryParam | Omit = omit,
        stamp: str | Omit = omit,
        tracks: Iterable[AudioSampleParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Revision:
        """
        Create a new revision

        Args:
          aux_channels

          genres

          samples

          tracks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/revisions",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "aux_channels": aux_channels,
                    "client_id": client_id,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "description": description,
                    "genres": genres,
                    "is_fork": is_fork,
                    "is_public": is_public,
                    "key": key,
                    "mastering": mastering,
                    "mixdown": mixdown,
                    "modified_on": modified_on,
                    "parent_id": parent_id,
                    "post_id": post_id,
                    "samples": samples,
                    "song": song,
                    "stamp": stamp,
                    "tracks": tracks,
                },
                revision_create_params.RevisionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Revision,
        )

    async def retrieve(
        self,
        revision_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Revision:
        """
        Returns a single revision

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            f"/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Revision,
        )

    async def update(
        self,
        revision_id: str,
        *,
        id: str | Omit = omit,
        aux_channels: Iterable[revision_update_params.AuxChannel] | Omit = omit,
        client_id: ClientID | Omit = omit,
        counters: RevisionCountersParam | Omit = omit,
        created_on: Union[str, datetime] | Omit = omit,
        creator: CreatorParam | Omit = omit,
        description: str | Omit = omit,
        genres: Iterable[GenreParam] | Omit = omit,
        is_fork: bool | Omit = omit,
        is_public: bool | Omit = omit,
        key: str | Omit = omit,
        mastering: MasteringParam | Omit = omit,
        mixdown: AudioSampleParam | Omit = omit,
        modified_on: Union[str, datetime] | Omit = omit,
        parent_id: str | Omit = omit,
        post_id: str | Omit = omit,
        samples: Iterable[AudioSampleParam] | Omit = omit,
        song: SongSummaryParam | Omit = omit,
        stamp: str | Omit = omit,
        tracks: Iterable[AudioSampleParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Revision:
        """
        Updates a revision

        Args:
          aux_channels

          genres

          samples

          tracks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._patch(
            f"/revisions/{revision_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "aux_channels": aux_channels,
                    "client_id": client_id,
                    "counters": counters,
                    "created_on": created_on,
                    "creator": creator,
                    "description": description,
                    "genres": genres,
                    "is_fork": is_fork,
                    "is_public": is_public,
                    "key": key,
                    "mastering": mastering,
                    "mixdown": mixdown,
                    "modified_on": modified_on,
                    "parent_id": parent_id,
                    "post_id": post_id,
                    "samples": samples,
                    "song": song,
                    "stamp": stamp,
                    "tracks": tracks,
                },
                revision_update_params.RevisionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Revision,
        )

    async def add_play(
        self,
        revision_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add a play

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/revisions/{revision_id}/plays",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RevisionsResourceWithRawResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.create = to_raw_response_wrapper(
            revisions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            revisions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            revisions.update,
        )
        self.add_play = to_raw_response_wrapper(
            revisions.add_play,
        )


class AsyncRevisionsResourceWithRawResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.create = async_to_raw_response_wrapper(
            revisions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            revisions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            revisions.update,
        )
        self.add_play = async_to_raw_response_wrapper(
            revisions.add_play,
        )


class RevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.create = to_streamed_response_wrapper(
            revisions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            revisions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            revisions.update,
        )
        self.add_play = to_streamed_response_wrapper(
            revisions.add_play,
        )


class AsyncRevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.create = async_to_streamed_response_wrapper(
            revisions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            revisions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            revisions.update,
        )
        self.add_play = async_to_streamed_response_wrapper(
            revisions.add_play,
        )
