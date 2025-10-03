# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types import Profile
from bandlab_sdk._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BandlabSDK) -> None:
        me = client.me.retrieve()
        assert_matches_type(Profile, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BandlabSDK) -> None:
        response = client.me.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(Profile, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BandlabSDK) -> None:
        with client.me.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(Profile, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: BandlabSDK) -> None:
        me = client.me.update()
        assert_matches_type(Profile, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: BandlabSDK) -> None:
        me = client.me.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            badges=["string"],
            birthday=parse_date("2019-12-27"),
            counters={
                "bands": 0,
                "collections": 0,
                "followers": 0,
                "following": 0,
            },
            created_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            ftue={
                "confirmed_email": True,
                "created_band": True,
                "created_song": True,
                "set_custom_username": True,
                "set_genres": True,
                "set_picture": True,
                "set_skills": True,
            },
            gender="Male",
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            has_password=True,
            is_beta_user=True,
            is_email_confirmed=True,
            is_newbie=True,
            is_social=True,
            is_tippable=True,
            is_verified=True,
            location={
                "city": "city",
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0,
                },
                "country": "country",
            },
            name="name",
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            skills=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            username="username",
        )
        assert_matches_type(Profile, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: BandlabSDK) -> None:
        response = client.me.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(Profile, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: BandlabSDK) -> None:
        with client.me.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(Profile, me, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMe:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        me = await async_client.me.retrieve()
        assert_matches_type(Profile, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.me.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(Profile, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.me.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(Profile, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBandlabSDK) -> None:
        me = await async_client.me.update()
        assert_matches_type(Profile, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        me = await async_client.me.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            badges=["string"],
            birthday=parse_date("2019-12-27"),
            counters={
                "bands": 0,
                "collections": 0,
                "followers": 0,
                "following": 0,
            },
            created_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            ftue={
                "confirmed_email": True,
                "created_band": True,
                "created_song": True,
                "set_custom_username": True,
                "set_genres": True,
                "set_picture": True,
                "set_skills": True,
            },
            gender="Male",
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            has_password=True,
            is_beta_user=True,
            is_email_confirmed=True,
            is_newbie=True,
            is_social=True,
            is_tippable=True,
            is_verified=True,
            location={
                "city": "city",
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0,
                },
                "country": "country",
            },
            name="name",
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            skills=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            username="username",
        )
        assert_matches_type(Profile, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.me.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(Profile, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.me.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(Profile, me, path=["response"])

        assert cast(Any, response.is_closed) is True
