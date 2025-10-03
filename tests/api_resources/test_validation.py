# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types import ValidationValidateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate(self, client: BandlabSDK) -> None:
        validation = client.validation.validate(
            entity_type="user",
        )
        assert_matches_type(ValidationValidateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: BandlabSDK) -> None:
        validation = client.validation.validate(
            entity_type="user",
            name="name",
            username="username",
        )
        assert_matches_type(ValidationValidateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: BandlabSDK) -> None:
        response = client.validation.with_raw_response.validate(
            entity_type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validation = response.parse()
        assert_matches_type(ValidationValidateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: BandlabSDK) -> None:
        with client.validation.with_streaming_response.validate(
            entity_type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validation = response.parse()
            assert_matches_type(ValidationValidateResponse, validation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncValidation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncBandlabSDK) -> None:
        validation = await async_client.validation.validate(
            entity_type="user",
        )
        assert_matches_type(ValidationValidateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        validation = await async_client.validation.validate(
            entity_type="user",
            name="name",
            username="username",
        )
        assert_matches_type(ValidationValidateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.validation.with_raw_response.validate(
            entity_type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validation = await response.parse()
        assert_matches_type(ValidationValidateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.validation.with_streaming_response.validate(
            entity_type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validation = await response.parse()
            assert_matches_type(ValidationValidateResponse, validation, path=["response"])

        assert cast(Any, response.is_closed) is True
