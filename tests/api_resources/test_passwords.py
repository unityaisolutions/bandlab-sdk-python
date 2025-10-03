# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPasswords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_change(self, client: BandlabSDK) -> None:
        password = client.passwords.change()
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_change_with_all_params(self, client: BandlabSDK) -> None:
        password = client.passwords.change(
            new_password="newPassword",
            old_password="oldPassword",
        )
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_change(self, client: BandlabSDK) -> None:
        response = client.passwords.with_raw_response.change()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = response.parse()
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_change(self, client: BandlabSDK) -> None:
        with client.passwords.with_streaming_response.change() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = response.parse()
            assert password is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset(self, client: BandlabSDK) -> None:
        password = client.passwords.reset()
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_with_all_params(self, client: BandlabSDK) -> None:
        password = client.passwords.reset(
            code="code",
            new_password="newPassword",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset(self, client: BandlabSDK) -> None:
        response = client.passwords.with_raw_response.reset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = response.parse()
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reset(self, client: BandlabSDK) -> None:
        with client.passwords.with_streaming_response.reset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = response.parse()
            assert password is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_restore_email(self, client: BandlabSDK) -> None:
        password = client.passwords.send_restore_email(
            email="email",
        )
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_restore_email(self, client: BandlabSDK) -> None:
        response = client.passwords.with_raw_response.send_restore_email(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = response.parse()
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_restore_email(self, client: BandlabSDK) -> None:
        with client.passwords.with_streaming_response.send_restore_email(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = response.parse()
            assert password is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPasswords:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_change(self, async_client: AsyncBandlabSDK) -> None:
        password = await async_client.passwords.change()
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_change_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        password = await async_client.passwords.change(
            new_password="newPassword",
            old_password="oldPassword",
        )
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_change(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.passwords.with_raw_response.change()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = await response.parse()
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_change(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.passwords.with_streaming_response.change() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = await response.parse()
            assert password is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset(self, async_client: AsyncBandlabSDK) -> None:
        password = await async_client.passwords.reset()
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        password = await async_client.passwords.reset(
            code="code",
            new_password="newPassword",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.passwords.with_raw_response.reset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = await response.parse()
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.passwords.with_streaming_response.reset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = await response.parse()
            assert password is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_restore_email(self, async_client: AsyncBandlabSDK) -> None:
        password = await async_client.passwords.send_restore_email(
            email="email",
        )
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_restore_email(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.passwords.with_raw_response.send_restore_email(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = await response.parse()
        assert password is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_restore_email(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.passwords.with_streaming_response.send_restore_email(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = await response.parse()
            assert password is None

        assert cast(Any, response.is_closed) is True
