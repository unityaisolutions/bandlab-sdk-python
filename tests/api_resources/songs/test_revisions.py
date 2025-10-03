# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types import Song
from bandlab_sdk._utils import parse_datetime
from bandlab_sdk.types.songs import RevisionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRevisions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: BandlabSDK) -> None:
        revision = client.songs.revisions.list(
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RevisionListResponse, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BandlabSDK) -> None:
        revision = client.songs.revisions.list(
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(RevisionListResponse, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BandlabSDK) -> None:
        response = client.songs.revisions.with_raw_response.list(
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(RevisionListResponse, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BandlabSDK) -> None:
        with client.songs.revisions.with_streaming_response.list(
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(RevisionListResponse, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `song_id` but received ''"):
            client.songs.revisions.with_raw_response.list(
                song_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_forks(self, client: BandlabSDK) -> None:
        revision = client.songs.revisions.forks(
            revison_id="revisonId",
            song_id="songId",
            name="name",
        )
        assert_matches_type(Song, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_forks_with_all_params(self, client: BandlabSDK) -> None:
        revision = client.songs.revisions.forks(
            revison_id="revisonId",
            song_id="songId",
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            author={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "conversation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "type": "User",
                "username": "username",
            },
            collaborators=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "counters": {
                        "bands": 0,
                        "collections": 0,
                        "followers": 0,
                        "following": 0,
                    },
                    "name": "name",
                    "picture": {
                        "is_default": True,
                        "l": "l",
                        "m": "m",
                        "s": "s",
                        "url": "url",
                    },
                    "username": "username",
                }
            ],
            counters={
                "collaborators": 0,
                "comments": 0,
                "forks": 0,
                "likes": 0,
                "plays": 0,
                "public_revisions": 0,
            },
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
            description="description",
            is_fork=True,
            is_forkable=True,
            is_public=True,
            modified_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            original={
                "creator_name": "creatorName",
                "name": "name",
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
                "revision_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "song_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            slug="slug",
        )
        assert_matches_type(Song, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_forks(self, client: BandlabSDK) -> None:
        response = client.songs.revisions.with_raw_response.forks(
            revison_id="revisonId",
            song_id="songId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(Song, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_forks(self, client: BandlabSDK) -> None:
        with client.songs.revisions.with_streaming_response.forks(
            revison_id="revisonId",
            song_id="songId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(Song, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_forks(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `song_id` but received ''"):
            client.songs.revisions.with_raw_response.forks(
                revison_id="revisonId",
                song_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revison_id` but received ''"):
            client.songs.revisions.with_raw_response.forks(
                revison_id="",
                song_id="songId",
                name="name",
            )


class TestAsyncRevisions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBandlabSDK) -> None:
        revision = await async_client.songs.revisions.list(
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RevisionListResponse, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        revision = await async_client.songs.revisions.list(
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(RevisionListResponse, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.songs.revisions.with_raw_response.list(
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(RevisionListResponse, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.songs.revisions.with_streaming_response.list(
            song_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(RevisionListResponse, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `song_id` but received ''"):
            await async_client.songs.revisions.with_raw_response.list(
                song_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_forks(self, async_client: AsyncBandlabSDK) -> None:
        revision = await async_client.songs.revisions.forks(
            revison_id="revisonId",
            song_id="songId",
            name="name",
        )
        assert_matches_type(Song, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_forks_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        revision = await async_client.songs.revisions.forks(
            revison_id="revisonId",
            song_id="songId",
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            author={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "conversation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "type": "User",
                "username": "username",
            },
            collaborators=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "counters": {
                        "bands": 0,
                        "collections": 0,
                        "followers": 0,
                        "following": 0,
                    },
                    "name": "name",
                    "picture": {
                        "is_default": True,
                        "l": "l",
                        "m": "m",
                        "s": "s",
                        "url": "url",
                    },
                    "username": "username",
                }
            ],
            counters={
                "collaborators": 0,
                "comments": 0,
                "forks": 0,
                "likes": 0,
                "plays": 0,
                "public_revisions": 0,
            },
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
            description="description",
            is_fork=True,
            is_forkable=True,
            is_public=True,
            modified_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            original={
                "creator_name": "creatorName",
                "name": "name",
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
                "revision_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "song_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            slug="slug",
        )
        assert_matches_type(Song, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_forks(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.songs.revisions.with_raw_response.forks(
            revison_id="revisonId",
            song_id="songId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(Song, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_forks(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.songs.revisions.with_streaming_response.forks(
            revison_id="revisonId",
            song_id="songId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(Song, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_forks(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `song_id` but received ''"):
            await async_client.songs.revisions.with_raw_response.forks(
                revison_id="revisonId",
                song_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revison_id` but received ''"):
            await async_client.songs.revisions.with_raw_response.forks(
                revison_id="",
                song_id="songId",
                name="name",
            )
