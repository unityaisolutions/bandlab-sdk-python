# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types import GenreListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenres:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: BandlabSDK) -> None:
        genre = client.genres.list()
        assert_matches_type(GenreListResponse, genre, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BandlabSDK) -> None:
        response = client.genres.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        genre = response.parse()
        assert_matches_type(GenreListResponse, genre, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BandlabSDK) -> None:
        with client.genres.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            genre = response.parse()
            assert_matches_type(GenreListResponse, genre, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenres:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBandlabSDK) -> None:
        genre = await async_client.genres.list()
        assert_matches_type(GenreListResponse, genre, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.genres.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        genre = await response.parse()
        assert_matches_type(GenreListResponse, genre, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.genres.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            genre = await response.parse()
            assert_matches_type(GenreListResponse, genre, path=["response"])

        assert cast(Any, response.is_closed) is True
