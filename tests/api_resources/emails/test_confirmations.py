# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfirmations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_confirm(self, client: BandlabSDK) -> None:
        confirmation = client.emails.confirmations.confirm()
        assert confirmation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_confirm_with_all_params(self, client: BandlabSDK) -> None:
        confirmation = client.emails.confirmations.confirm(
            code="code",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert confirmation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_confirm(self, client: BandlabSDK) -> None:
        response = client.emails.confirmations.with_raw_response.confirm()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        confirmation = response.parse()
        assert confirmation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_confirm(self, client: BandlabSDK) -> None:
        with client.emails.confirmations.with_streaming_response.confirm() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            confirmation = response.parse()
            assert confirmation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resend(self, client: BandlabSDK) -> None:
        confirmation = client.emails.confirmations.resend()
        assert confirmation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resend(self, client: BandlabSDK) -> None:
        response = client.emails.confirmations.with_raw_response.resend()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        confirmation = response.parse()
        assert confirmation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resend(self, client: BandlabSDK) -> None:
        with client.emails.confirmations.with_streaming_response.resend() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            confirmation = response.parse()
            assert confirmation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncConfirmations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_confirm(self, async_client: AsyncBandlabSDK) -> None:
        confirmation = await async_client.emails.confirmations.confirm()
        assert confirmation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_confirm_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        confirmation = await async_client.emails.confirmations.confirm(
            code="code",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert confirmation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.emails.confirmations.with_raw_response.confirm()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        confirmation = await response.parse()
        assert confirmation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.emails.confirmations.with_streaming_response.confirm() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            confirmation = await response.parse()
            assert confirmation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resend(self, async_client: AsyncBandlabSDK) -> None:
        confirmation = await async_client.emails.confirmations.resend()
        assert confirmation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resend(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.emails.confirmations.with_raw_response.resend()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        confirmation = await response.parse()
        assert confirmation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resend(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.emails.confirmations.with_streaming_response.resend() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            confirmation = await response.parse()
            assert confirmation is None

        assert cast(Any, response.is_closed) is True
