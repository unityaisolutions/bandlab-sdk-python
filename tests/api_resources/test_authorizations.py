# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types import AuthorizationCreateSessionKeyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthorizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_session_key(self, client: BandlabSDK) -> None:
        authorization = client.authorizations.create_session_key()
        assert_matches_type(AuthorizationCreateSessionKeyResponse, authorization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_session_key_with_all_params(self, client: BandlabSDK) -> None:
        authorization = client.authorizations.create_session_key(
            access_token="accessToken",
            email="email",
            key="key",
            login="login",
            name="name",
            password="password",
            provider="Password",
            referral="referral",
            refresh_token="refreshToken",
            register=True,
            remember_me=True,
            username="username",
        )
        assert_matches_type(AuthorizationCreateSessionKeyResponse, authorization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_session_key(self, client: BandlabSDK) -> None:
        response = client.authorizations.with_raw_response.create_session_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authorization = response.parse()
        assert_matches_type(AuthorizationCreateSessionKeyResponse, authorization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_session_key(self, client: BandlabSDK) -> None:
        with client.authorizations.with_streaming_response.create_session_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authorization = response.parse()
            assert_matches_type(AuthorizationCreateSessionKeyResponse, authorization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthorizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_session_key(self, async_client: AsyncBandlabSDK) -> None:
        authorization = await async_client.authorizations.create_session_key()
        assert_matches_type(AuthorizationCreateSessionKeyResponse, authorization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_session_key_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        authorization = await async_client.authorizations.create_session_key(
            access_token="accessToken",
            email="email",
            key="key",
            login="login",
            name="name",
            password="password",
            provider="Password",
            referral="referral",
            refresh_token="refreshToken",
            register=True,
            remember_me=True,
            username="username",
        )
        assert_matches_type(AuthorizationCreateSessionKeyResponse, authorization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_session_key(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.authorizations.with_raw_response.create_session_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authorization = await response.parse()
        assert_matches_type(AuthorizationCreateSessionKeyResponse, authorization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_session_key(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.authorizations.with_streaming_response.create_session_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authorization = await response.parse()
            assert_matches_type(AuthorizationCreateSessionKeyResponse, authorization, path=["response"])

        assert cast(Any, response.is_closed) is True
