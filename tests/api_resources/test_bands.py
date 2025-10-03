# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types import (
    Band,
    PostList,
    SongList,
)
from bandlab_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBands:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: BandlabSDK) -> None:
        band = client.bands.create(
            name="name",
        )
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: BandlabSDK) -> None:
        band = client.bands.create(
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counters={"members": 0},
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
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            is_open=True,
            members=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "username": "username",
                }
            ],
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            username="username",
        )
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: BandlabSDK) -> None:
        response = client.bands.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = response.parse()
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: BandlabSDK) -> None:
        with client.bands.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = response.parse()
            assert_matches_type(Band, band, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BandlabSDK) -> None:
        band = client.bands.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BandlabSDK) -> None:
        response = client.bands.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = response.parse()
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BandlabSDK) -> None:
        with client.bands.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = response.parse()
            assert_matches_type(Band, band, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            client.bands.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: BandlabSDK) -> None:
        band = client.bands.update(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: BandlabSDK) -> None:
        band = client.bands.update(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counters={"members": 0},
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
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            is_open=True,
            members=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "username": "username",
                }
            ],
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            username="username",
        )
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: BandlabSDK) -> None:
        response = client.bands.with_raw_response.update(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = response.parse()
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: BandlabSDK) -> None:
        with client.bands.with_streaming_response.update(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = response.parse()
            assert_matches_type(Band, band, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            client.bands.with_raw_response.update(
                band_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: BandlabSDK) -> None:
        band = client.bands.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert band is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: BandlabSDK) -> None:
        response = client.bands.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = response.parse()
        assert band is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: BandlabSDK) -> None:
        with client.bands.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = response.parse()
            assert band is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            client.bands.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_posts(self, client: BandlabSDK) -> None:
        band = client.bands.list_posts(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PostList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_posts_with_all_params(self, client: BandlabSDK) -> None:
        band = client.bands.list_posts(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(PostList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_posts(self, client: BandlabSDK) -> None:
        response = client.bands.with_raw_response.list_posts(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = response.parse()
        assert_matches_type(PostList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_posts(self, client: BandlabSDK) -> None:
        with client.bands.with_streaming_response.list_posts(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = response.parse()
            assert_matches_type(PostList, band, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_posts(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            client.bands.with_raw_response.list_posts(
                band_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_songs(self, client: BandlabSDK) -> None:
        band = client.bands.list_songs(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SongList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_songs_with_all_params(self, client: BandlabSDK) -> None:
        band = client.bands.list_songs(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(SongList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_songs(self, client: BandlabSDK) -> None:
        response = client.bands.with_raw_response.list_songs(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = response.parse()
        assert_matches_type(SongList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_songs(self, client: BandlabSDK) -> None:
        with client.bands.with_streaming_response.list_songs(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = response.parse()
            assert_matches_type(SongList, band, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_songs(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            client.bands.with_raw_response.list_songs(
                band_id="",
            )


class TestAsyncBands:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBandlabSDK) -> None:
        band = await async_client.bands.create(
            name="name",
        )
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        band = await async_client.bands.create(
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counters={"members": 0},
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
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            is_open=True,
            members=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "username": "username",
                }
            ],
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            username="username",
        )
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.bands.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = await response.parse()
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.bands.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = await response.parse()
            assert_matches_type(Band, band, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        band = await async_client.bands.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.bands.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = await response.parse()
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.bands.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = await response.parse()
            assert_matches_type(Band, band, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            await async_client.bands.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBandlabSDK) -> None:
        band = await async_client.bands.update(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        band = await async_client.bands.update(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counters={"members": 0},
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
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            is_open=True,
            members=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "username": "username",
                }
            ],
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            username="username",
        )
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.bands.with_raw_response.update(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = await response.parse()
        assert_matches_type(Band, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.bands.with_streaming_response.update(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = await response.parse()
            assert_matches_type(Band, band, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            await async_client.bands.with_raw_response.update(
                band_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBandlabSDK) -> None:
        band = await async_client.bands.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert band is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.bands.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = await response.parse()
        assert band is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.bands.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = await response.parse()
            assert band is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            await async_client.bands.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_posts(self, async_client: AsyncBandlabSDK) -> None:
        band = await async_client.bands.list_posts(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PostList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_posts_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        band = await async_client.bands.list_posts(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(PostList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_posts(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.bands.with_raw_response.list_posts(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = await response.parse()
        assert_matches_type(PostList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_posts(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.bands.with_streaming_response.list_posts(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = await response.parse()
            assert_matches_type(PostList, band, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_posts(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            await async_client.bands.with_raw_response.list_posts(
                band_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_songs(self, async_client: AsyncBandlabSDK) -> None:
        band = await async_client.bands.list_songs(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SongList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_songs_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        band = await async_client.bands.list_songs(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(SongList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_songs(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.bands.with_raw_response.list_songs(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        band = await response.parse()
        assert_matches_type(SongList, band, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_songs(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.bands.with_streaming_response.list_songs(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            band = await response.parse()
            assert_matches_type(SongList, band, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_songs(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            await async_client.bands.with_raw_response.list_songs(
                band_id="",
            )
