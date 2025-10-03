# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types.collections import Post

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPosts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BandlabSDK) -> None:
        post = client.collections.posts.retrieve(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Post, post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BandlabSDK) -> None:
        response = client.collections.posts.with_raw_response.retrieve(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(Post, post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BandlabSDK) -> None:
        with client.collections.posts.with_streaming_response.retrieve(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(Post, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.posts.with_raw_response.retrieve(
                post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.collections.posts.with_raw_response.retrieve(
                post_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: BandlabSDK) -> None:
        post = client.collections.posts.add(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Post, post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: BandlabSDK) -> None:
        response = client.collections.posts.with_raw_response.add(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(Post, post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: BandlabSDK) -> None:
        with client.collections.posts.with_streaming_response.add(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(Post, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.posts.with_raw_response.add(
                post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.collections.posts.with_raw_response.add(
                post_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: BandlabSDK) -> None:
        post = client.collections.posts.remove(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert post is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: BandlabSDK) -> None:
        response = client.collections.posts.with_raw_response.remove(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert post is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: BandlabSDK) -> None:
        with client.collections.posts.with_streaming_response.remove(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.posts.with_raw_response.remove(
                post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.collections.posts.with_raw_response.remove(
                post_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_position(self, client: BandlabSDK) -> None:
        post = client.collections.posts.update_position(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert post is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_position_with_all_params(self, client: BandlabSDK) -> None:
        post = client.collections.posts.update_position(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            order=0,
        )
        assert post is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_position(self, client: BandlabSDK) -> None:
        response = client.collections.posts.with_raw_response.update_position(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert post is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_position(self, client: BandlabSDK) -> None:
        with client.collections.posts.with_streaming_response.update_position(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_position(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.posts.with_raw_response.update_position(
                post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.collections.posts.with_raw_response.update_position(
                post_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncPosts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        post = await async_client.collections.posts.retrieve(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Post, post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.collections.posts.with_raw_response.retrieve(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(Post, post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.collections.posts.with_streaming_response.retrieve(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(Post, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.posts.with_raw_response.retrieve(
                post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.collections.posts.with_raw_response.retrieve(
                post_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncBandlabSDK) -> None:
        post = await async_client.collections.posts.add(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Post, post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.collections.posts.with_raw_response.add(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(Post, post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.collections.posts.with_streaming_response.add(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(Post, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.posts.with_raw_response.add(
                post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.collections.posts.with_raw_response.add(
                post_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncBandlabSDK) -> None:
        post = await async_client.collections.posts.remove(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert post is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.collections.posts.with_raw_response.remove(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert post is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.collections.posts.with_streaming_response.remove(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.posts.with_raw_response.remove(
                post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.collections.posts.with_raw_response.remove(
                post_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_position(self, async_client: AsyncBandlabSDK) -> None:
        post = await async_client.collections.posts.update_position(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert post is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_position_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        post = await async_client.collections.posts.update_position(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            order=0,
        )
        assert post is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_position(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.collections.posts.with_raw_response.update_position(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert post is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_position(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.collections.posts.with_streaming_response.update_position(
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_position(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.posts.with_raw_response.update_position(
                post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.collections.posts.with_raw_response.update_position(
                post_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
