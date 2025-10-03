# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types import PostList
from bandlab_sdk.types.users import UserList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFollowing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: BandlabSDK) -> None:
        following = client.users.following.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BandlabSDK) -> None:
        following = client.users.following.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(UserList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BandlabSDK) -> None:
        response = client.users.following.with_raw_response.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = response.parse()
        assert_matches_type(UserList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BandlabSDK) -> None:
        with client.users.following.with_streaming_response.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = response.parse()
            assert_matches_type(UserList, following, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.following.with_raw_response.list(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_posts(self, client: BandlabSDK) -> None:
        following = client.users.following.list_posts(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PostList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_posts_with_all_params(self, client: BandlabSDK) -> None:
        following = client.users.following.list_posts(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(PostList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_posts(self, client: BandlabSDK) -> None:
        response = client.users.following.with_raw_response.list_posts(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = response.parse()
        assert_matches_type(PostList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_posts(self, client: BandlabSDK) -> None:
        with client.users.following.with_streaming_response.list_posts(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = response.parse()
            assert_matches_type(PostList, following, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_posts(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.following.with_raw_response.list_posts(
                user_id="",
            )


class TestAsyncFollowing:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBandlabSDK) -> None:
        following = await async_client.users.following.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        following = await async_client.users.following.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(UserList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.users.following.with_raw_response.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = await response.parse()
        assert_matches_type(UserList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.users.following.with_streaming_response.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = await response.parse()
            assert_matches_type(UserList, following, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.following.with_raw_response.list(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_posts(self, async_client: AsyncBandlabSDK) -> None:
        following = await async_client.users.following.list_posts(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PostList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_posts_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        following = await async_client.users.following.list_posts(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(PostList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_posts(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.users.following.with_raw_response.list_posts(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = await response.parse()
        assert_matches_type(PostList, following, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_posts(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.users.following.with_streaming_response.list_posts(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = await response.parse()
            assert_matches_type(PostList, following, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_posts(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.following.with_raw_response.list_posts(
                user_id="",
            )
