# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types.songs import CollaboratorListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollaborators:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: BandlabSDK) -> None:
        collaborator = client.songs.collaborators.list(
            song_id="songId",
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollaboratorListResponse, collaborator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BandlabSDK) -> None:
        collaborator = client.songs.collaborators.list(
            song_id="songId",
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(CollaboratorListResponse, collaborator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BandlabSDK) -> None:
        response = client.songs.collaborators.with_raw_response.list(
            song_id="songId",
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collaborator = response.parse()
        assert_matches_type(CollaboratorListResponse, collaborator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BandlabSDK) -> None:
        with client.songs.collaborators.with_streaming_response.list(
            song_id="songId",
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collaborator = response.parse()
            assert_matches_type(CollaboratorListResponse, collaborator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `song_id` but received ''"):
            client.songs.collaborators.with_raw_response.list(
                song_id="",
                community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: BandlabSDK) -> None:
        collaborator = client.songs.collaborators.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert collaborator is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: BandlabSDK) -> None:
        response = client.songs.collaborators.with_raw_response.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collaborator = response.parse()
        assert collaborator is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: BandlabSDK) -> None:
        with client.songs.collaborators.with_streaming_response.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collaborator = response.parse()
            assert collaborator is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `song_id` but received ''"):
            client.songs.collaborators.with_raw_response.remove(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                song_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.songs.collaborators.with_raw_response.remove(
                user_id="",
                song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncCollaborators:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBandlabSDK) -> None:
        collaborator = await async_client.songs.collaborators.list(
            song_id="songId",
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollaboratorListResponse, collaborator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        collaborator = await async_client.songs.collaborators.list(
            song_id="songId",
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(CollaboratorListResponse, collaborator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.songs.collaborators.with_raw_response.list(
            song_id="songId",
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collaborator = await response.parse()
        assert_matches_type(CollaboratorListResponse, collaborator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.songs.collaborators.with_streaming_response.list(
            song_id="songId",
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collaborator = await response.parse()
            assert_matches_type(CollaboratorListResponse, collaborator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `song_id` but received ''"):
            await async_client.songs.collaborators.with_raw_response.list(
                song_id="",
                community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncBandlabSDK) -> None:
        collaborator = await async_client.songs.collaborators.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert collaborator is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.songs.collaborators.with_raw_response.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collaborator = await response.parse()
        assert collaborator is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.songs.collaborators.with_streaming_response.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collaborator = await response.parse()
            assert collaborator is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `song_id` but received ''"):
            await async_client.songs.collaborators.with_raw_response.remove(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                song_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.songs.collaborators.with_raw_response.remove(
                user_id="",
                song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
