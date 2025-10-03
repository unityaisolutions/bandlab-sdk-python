# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk._utils import parse_datetime
from bandlab_sdk.types.collections import Post

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_view(self, client: BandlabSDK) -> None:
        video = client.videos.add_view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert video is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_view(self, client: BandlabSDK) -> None:
        response = client.videos.with_raw_response.add_view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert video is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_view(self, client: BandlabSDK) -> None:
        with client.videos.with_streaming_response.add_view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert video is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_view(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `video_id` but received ''"):
            client.videos.with_raw_response.add_view(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_post(self, client: BandlabSDK) -> None:
        video = client.videos.create_post(
            video_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Post, video, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_post_with_all_params(self, client: BandlabSDK) -> None:
        video = client.videos.create_post(
            video_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            caption="caption",
            client_id="Angular",
            comments=[
                {
                    "id": 0,
                    "content": "content",
                    "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "creator": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "is_verified": True,
                        "name": "name",
                        "picture": {
                            "is_default": True,
                            "l": "l",
                            "m": "m",
                            "s": "s",
                            "url": "url",
                        },
                        "username": "username",
                    },
                    "timestamp": 0,
                }
            ],
            counters={
                "comments": 0,
                "likes": 0,
                "reposts": 0,
            },
            created_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            creator={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "is_verified": True,
                "name": "name",
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
                "username": "username",
            },
            image={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "counters": {"likes": 0},
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
            },
            message="message",
            revision={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "client_id": "Angular",
                "counters": {
                    "comments": 0,
                    "forks": 0,
                    "likes": 0,
                    "plays": 0,
                },
                "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                "creator": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "is_verified": True,
                    "name": "name",
                    "picture": {
                        "is_default": True,
                        "l": "l",
                        "m": "m",
                        "s": "s",
                        "url": "url",
                    },
                    "username": "username",
                },
                "description": "description",
                "is_fork": True,
                "is_public": True,
                "lyrics": {"content": "content"},
                "mixdown": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "status": "Empty",
                },
                "parent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "post_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "stamp": "stamp",
            },
            type="Revision",
            video={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "counters": {
                    "likes": 0,
                    "views": 0,
                },
                "duration": 0,
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
                "status": "Empty",
            },
        )
        assert_matches_type(Post, video, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_post(self, client: BandlabSDK) -> None:
        response = client.videos.with_raw_response.create_post(
            video_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(Post, video, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_post(self, client: BandlabSDK) -> None:
        with client.videos.with_streaming_response.create_post(
            video_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(Post, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_post(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `video_id` but received ''"):
            client.videos.with_raw_response.create_post(
                video_id="",
            )


class TestAsyncVideos:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_view(self, async_client: AsyncBandlabSDK) -> None:
        video = await async_client.videos.add_view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert video is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_view(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.videos.with_raw_response.add_view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert video is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_view(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.videos.with_streaming_response.add_view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert video is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_view(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `video_id` but received ''"):
            await async_client.videos.with_raw_response.add_view(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_post(self, async_client: AsyncBandlabSDK) -> None:
        video = await async_client.videos.create_post(
            video_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Post, video, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_post_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        video = await async_client.videos.create_post(
            video_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            caption="caption",
            client_id="Angular",
            comments=[
                {
                    "id": 0,
                    "content": "content",
                    "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "creator": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "is_verified": True,
                        "name": "name",
                        "picture": {
                            "is_default": True,
                            "l": "l",
                            "m": "m",
                            "s": "s",
                            "url": "url",
                        },
                        "username": "username",
                    },
                    "timestamp": 0,
                }
            ],
            counters={
                "comments": 0,
                "likes": 0,
                "reposts": 0,
            },
            created_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            creator={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "is_verified": True,
                "name": "name",
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
                "username": "username",
            },
            image={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "counters": {"likes": 0},
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
            },
            message="message",
            revision={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "client_id": "Angular",
                "counters": {
                    "comments": 0,
                    "forks": 0,
                    "likes": 0,
                    "plays": 0,
                },
                "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                "creator": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "is_verified": True,
                    "name": "name",
                    "picture": {
                        "is_default": True,
                        "l": "l",
                        "m": "m",
                        "s": "s",
                        "url": "url",
                    },
                    "username": "username",
                },
                "description": "description",
                "is_fork": True,
                "is_public": True,
                "lyrics": {"content": "content"},
                "mixdown": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "status": "Empty",
                },
                "parent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "post_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "stamp": "stamp",
            },
            type="Revision",
            video={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "counters": {
                    "likes": 0,
                    "views": 0,
                },
                "duration": 0,
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
                "status": "Empty",
            },
        )
        assert_matches_type(Post, video, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_post(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.videos.with_raw_response.create_post(
            video_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(Post, video, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_post(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.videos.with_streaming_response.create_post(
            video_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(Post, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_post(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `video_id` but received ''"):
            await async_client.videos.with_raw_response.create_post(
                video_id="",
            )
