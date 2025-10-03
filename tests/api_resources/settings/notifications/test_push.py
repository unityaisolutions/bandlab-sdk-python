# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types.settings.notifications import SettingsPush, SettingsEmail

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPush:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BandlabSDK) -> None:
        push = client.settings.notifications.push.retrieve()
        assert_matches_type(SettingsEmail, push, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BandlabSDK) -> None:
        response = client.settings.notifications.push.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = response.parse()
        assert_matches_type(SettingsEmail, push, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BandlabSDK) -> None:
        with client.settings.notifications.push.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = response.parse()
            assert_matches_type(SettingsEmail, push, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: BandlabSDK) -> None:
        push = client.settings.notifications.push.update()
        assert_matches_type(SettingsPush, push, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: BandlabSDK) -> None:
        push = client.settings.notifications.push.update(
            invitation_to_band=True,
            invitation_to_song=True,
            join_to_band_request=True,
            new_band_member=True,
            new_revision=True,
            new_song_collaborator=True,
            new_song_in_band=True,
            request_to_join_approved=True,
        )
        assert_matches_type(SettingsPush, push, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: BandlabSDK) -> None:
        response = client.settings.notifications.push.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = response.parse()
        assert_matches_type(SettingsPush, push, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: BandlabSDK) -> None:
        with client.settings.notifications.push.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = response.parse()
            assert_matches_type(SettingsPush, push, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPush:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        push = await async_client.settings.notifications.push.retrieve()
        assert_matches_type(SettingsEmail, push, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.settings.notifications.push.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = await response.parse()
        assert_matches_type(SettingsEmail, push, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.settings.notifications.push.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = await response.parse()
            assert_matches_type(SettingsEmail, push, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBandlabSDK) -> None:
        push = await async_client.settings.notifications.push.update()
        assert_matches_type(SettingsPush, push, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        push = await async_client.settings.notifications.push.update(
            invitation_to_band=True,
            invitation_to_song=True,
            join_to_band_request=True,
            new_band_member=True,
            new_revision=True,
            new_song_collaborator=True,
            new_song_in_band=True,
            request_to_join_approved=True,
        )
        assert_matches_type(SettingsPush, push, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.settings.notifications.push.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = await response.parse()
        assert_matches_type(SettingsPush, push, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.settings.notifications.push.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = await response.parse()
            assert_matches_type(SettingsPush, push, path=["response"])

        assert cast(Any, response.is_closed) is True
