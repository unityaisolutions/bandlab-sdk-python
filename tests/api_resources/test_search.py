# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types import (
    SongList,
    CollectionList,
    SearchSearchBandsResponse,
    SearchGlobalSearchResponse,
)
from bandlab_sdk.types.users import UserList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_global_search(self, client: BandlabSDK) -> None:
        search = client.search.global_search(
            query="query",
        )
        assert_matches_type(SearchGlobalSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_global_search_with_all_params(self, client: BandlabSDK) -> None:
        search = client.search.global_search(
            query="query",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(SearchGlobalSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_global_search(self, client: BandlabSDK) -> None:
        response = client.search.with_raw_response.global_search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchGlobalSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_global_search(self, client: BandlabSDK) -> None:
        with client.search.with_streaming_response.global_search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchGlobalSearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_bands(self, client: BandlabSDK) -> None:
        search = client.search.search_bands(
            query="query",
        )
        assert_matches_type(SearchSearchBandsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_bands_with_all_params(self, client: BandlabSDK) -> None:
        search = client.search.search_bands(
            query="query",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(SearchSearchBandsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search_bands(self, client: BandlabSDK) -> None:
        response = client.search.with_raw_response.search_bands(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchSearchBandsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search_bands(self, client: BandlabSDK) -> None:
        with client.search.with_streaming_response.search_bands(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchSearchBandsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_collections(self, client: BandlabSDK) -> None:
        search = client.search.search_collections(
            query="query",
        )
        assert_matches_type(CollectionList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_collections_with_all_params(self, client: BandlabSDK) -> None:
        search = client.search.search_collections(
            query="query",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(CollectionList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search_collections(self, client: BandlabSDK) -> None:
        response = client.search.with_raw_response.search_collections(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(CollectionList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search_collections(self, client: BandlabSDK) -> None:
        with client.search.with_streaming_response.search_collections(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(CollectionList, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_songs(self, client: BandlabSDK) -> None:
        search = client.search.search_songs(
            query="query",
        )
        assert_matches_type(SongList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_songs_with_all_params(self, client: BandlabSDK) -> None:
        search = client.search.search_songs(
            query="query",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(SongList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search_songs(self, client: BandlabSDK) -> None:
        response = client.search.with_raw_response.search_songs(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SongList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search_songs(self, client: BandlabSDK) -> None:
        with client.search.with_streaming_response.search_songs(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SongList, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_users(self, client: BandlabSDK) -> None:
        search = client.search.search_users(
            query="query",
        )
        assert_matches_type(UserList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_users_with_all_params(self, client: BandlabSDK) -> None:
        search = client.search.search_users(
            query="query",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(UserList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search_users(self, client: BandlabSDK) -> None:
        response = client.search.with_raw_response.search_users(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(UserList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search_users(self, client: BandlabSDK) -> None:
        with client.search.with_streaming_response.search_users(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(UserList, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_global_search(self, async_client: AsyncBandlabSDK) -> None:
        search = await async_client.search.global_search(
            query="query",
        )
        assert_matches_type(SearchGlobalSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_global_search_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        search = await async_client.search.global_search(
            query="query",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(SearchGlobalSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_global_search(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.search.with_raw_response.global_search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchGlobalSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_global_search(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.search.with_streaming_response.global_search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchGlobalSearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_bands(self, async_client: AsyncBandlabSDK) -> None:
        search = await async_client.search.search_bands(
            query="query",
        )
        assert_matches_type(SearchSearchBandsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_bands_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        search = await async_client.search.search_bands(
            query="query",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(SearchSearchBandsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search_bands(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.search.with_raw_response.search_bands(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchSearchBandsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search_bands(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.search.with_streaming_response.search_bands(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchSearchBandsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_collections(self, async_client: AsyncBandlabSDK) -> None:
        search = await async_client.search.search_collections(
            query="query",
        )
        assert_matches_type(CollectionList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_collections_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        search = await async_client.search.search_collections(
            query="query",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(CollectionList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search_collections(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.search.with_raw_response.search_collections(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(CollectionList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search_collections(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.search.with_streaming_response.search_collections(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(CollectionList, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_songs(self, async_client: AsyncBandlabSDK) -> None:
        search = await async_client.search.search_songs(
            query="query",
        )
        assert_matches_type(SongList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_songs_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        search = await async_client.search.search_songs(
            query="query",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(SongList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search_songs(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.search.with_raw_response.search_songs(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SongList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search_songs(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.search.with_streaming_response.search_songs(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SongList, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_users(self, async_client: AsyncBandlabSDK) -> None:
        search = await async_client.search.search_users(
            query="query",
        )
        assert_matches_type(UserList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_users_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        search = await async_client.search.search_users(
            query="query",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(UserList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search_users(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.search.with_raw_response.search_users(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(UserList, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search_users(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.search.with_streaming_response.search_users(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(UserList, search, path=["response"])

        assert cast(Any, response.is_closed) is True
