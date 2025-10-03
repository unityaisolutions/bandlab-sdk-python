# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types import (
    Revision,
)
from bandlab_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRevisions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: BandlabSDK) -> None:
        revision = client.revisions.create()
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: BandlabSDK) -> None:
        revision = client.revisions.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            aux_channels=[
                {
                    "id": "id",
                    "effects": [
                        {
                            "bypass": True,
                            "params": {},
                            "slug": "slug",
                        }
                    ],
                    "preset": "preset",
                    "return_level": 0,
                }
            ],
            client_id="Angular",
            counters={
                "comments": 0,
                "forks": 0,
                "likes": 0,
                "plays": 0,
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
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            is_fork=True,
            is_public=True,
            key="key",
            mastering={
                "dry_sample_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "preset": "preset",
            },
            mixdown={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "status": "Empty",
            },
            modified_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            samples=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "status": "Empty",
                }
            ],
            song={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "author": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "conversation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "type": "User",
                    "username": "username",
                },
                "counters": {
                    "collaborators": 0,
                    "comments": 0,
                    "forks": 0,
                    "likes": 0,
                    "plays": 0,
                    "public_revisions": 0,
                },
                "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                "description": "description",
                "is_fork": True,
                "is_forkable": True,
                "is_public": True,
                "name": "name",
                "original": {
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
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
                "slug": "slug",
            },
            stamp="stamp",
            tracks=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "status": "Empty",
                }
            ],
        )
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: BandlabSDK) -> None:
        response = client.revisions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: BandlabSDK) -> None:
        with client.revisions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(Revision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BandlabSDK) -> None:
        revision = client.revisions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BandlabSDK) -> None:
        response = client.revisions.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BandlabSDK) -> None:
        with client.revisions.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(Revision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.revisions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: BandlabSDK) -> None:
        revision = client.revisions.update(
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: BandlabSDK) -> None:
        revision = client.revisions.update(
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            aux_channels=[
                {
                    "id": "id",
                    "effects": [
                        {
                            "bypass": True,
                            "params": {},
                            "slug": "slug",
                        }
                    ],
                    "preset": "preset",
                    "return_level": 0,
                }
            ],
            client_id="Angular",
            counters={
                "comments": 0,
                "forks": 0,
                "likes": 0,
                "plays": 0,
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
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            is_fork=True,
            is_public=True,
            key="key",
            mastering={
                "dry_sample_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "preset": "preset",
            },
            mixdown={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "status": "Empty",
            },
            modified_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            samples=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "status": "Empty",
                }
            ],
            song={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "author": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "conversation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "type": "User",
                    "username": "username",
                },
                "counters": {
                    "collaborators": 0,
                    "comments": 0,
                    "forks": 0,
                    "likes": 0,
                    "plays": 0,
                    "public_revisions": 0,
                },
                "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                "description": "description",
                "is_fork": True,
                "is_forkable": True,
                "is_public": True,
                "name": "name",
                "original": {
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
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
                "slug": "slug",
            },
            stamp="stamp",
            tracks=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "status": "Empty",
                }
            ],
        )
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: BandlabSDK) -> None:
        response = client.revisions.with_raw_response.update(
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: BandlabSDK) -> None:
        with client.revisions.with_streaming_response.update(
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(Revision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.revisions.with_raw_response.update(
                revision_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_play(self, client: BandlabSDK) -> None:
        revision = client.revisions.add_play(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert revision is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_play(self, client: BandlabSDK) -> None:
        response = client.revisions.with_raw_response.add_play(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert revision is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_play(self, client: BandlabSDK) -> None:
        with client.revisions.with_streaming_response.add_play(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert revision is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_play(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.revisions.with_raw_response.add_play(
                "",
            )


class TestAsyncRevisions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBandlabSDK) -> None:
        revision = await async_client.revisions.create()
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        revision = await async_client.revisions.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            aux_channels=[
                {
                    "id": "id",
                    "effects": [
                        {
                            "bypass": True,
                            "params": {},
                            "slug": "slug",
                        }
                    ],
                    "preset": "preset",
                    "return_level": 0,
                }
            ],
            client_id="Angular",
            counters={
                "comments": 0,
                "forks": 0,
                "likes": 0,
                "plays": 0,
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
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            is_fork=True,
            is_public=True,
            key="key",
            mastering={
                "dry_sample_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "preset": "preset",
            },
            mixdown={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "status": "Empty",
            },
            modified_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            samples=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "status": "Empty",
                }
            ],
            song={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "author": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "conversation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "type": "User",
                    "username": "username",
                },
                "counters": {
                    "collaborators": 0,
                    "comments": 0,
                    "forks": 0,
                    "likes": 0,
                    "plays": 0,
                    "public_revisions": 0,
                },
                "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                "description": "description",
                "is_fork": True,
                "is_forkable": True,
                "is_public": True,
                "name": "name",
                "original": {
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
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
                "slug": "slug",
            },
            stamp="stamp",
            tracks=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "status": "Empty",
                }
            ],
        )
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.revisions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.revisions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(Revision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        revision = await async_client.revisions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.revisions.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.revisions.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(Revision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.revisions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBandlabSDK) -> None:
        revision = await async_client.revisions.update(
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        revision = await async_client.revisions.update(
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            aux_channels=[
                {
                    "id": "id",
                    "effects": [
                        {
                            "bypass": True,
                            "params": {},
                            "slug": "slug",
                        }
                    ],
                    "preset": "preset",
                    "return_level": 0,
                }
            ],
            client_id="Angular",
            counters={
                "comments": 0,
                "forks": 0,
                "likes": 0,
                "plays": 0,
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
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            is_fork=True,
            is_public=True,
            key="key",
            mastering={
                "dry_sample_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "preset": "preset",
            },
            mixdown={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "status": "Empty",
            },
            modified_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            post_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            samples=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "status": "Empty",
                }
            ],
            song={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "author": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "conversation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "type": "User",
                    "username": "username",
                },
                "counters": {
                    "collaborators": 0,
                    "comments": 0,
                    "forks": 0,
                    "likes": 0,
                    "plays": 0,
                    "public_revisions": 0,
                },
                "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                "description": "description",
                "is_fork": True,
                "is_forkable": True,
                "is_public": True,
                "name": "name",
                "original": {
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
                "picture": {
                    "is_default": True,
                    "l": "l",
                    "m": "m",
                    "s": "s",
                    "url": "url",
                },
                "slug": "slug",
            },
            stamp="stamp",
            tracks=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                    "status": "Empty",
                }
            ],
        )
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.revisions.with_raw_response.update(
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(Revision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.revisions.with_streaming_response.update(
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(Revision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.revisions.with_raw_response.update(
                revision_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_play(self, async_client: AsyncBandlabSDK) -> None:
        revision = await async_client.revisions.add_play(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert revision is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_play(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.revisions.with_raw_response.add_play(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert revision is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_play(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.revisions.with_streaming_response.add_play(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert revision is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_play(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.revisions.with_raw_response.add_play(
                "",
            )
