# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk.types import Collection
from bandlab_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: BandlabSDK) -> None:
        collection = client.collections.create(
            name="name",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: BandlabSDK) -> None:
        collection = client.collections.create(
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counters={
                "items": 0,
                "likes": 0,
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
            is_public=True,
            last_updated_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            posts=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "caption": "caption",
                    "client_id": "Angular",
                    "comments": [
                        {
                            "id": 0,
                            "content": "content",
                            "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "creator": {
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
                            "timestamp": 0,
                        }
                    ],
                    "counters": {
                        "comments": 0,
                        "likes": 0,
                        "reposts": 0,
                    },
                    "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "creator": {
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
                    "image": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "counters": {"likes": 0},
                        "picture": {
                            "is_default": True,
                            "l": "l",
                            "m": "m",
                            "s": "s",
                            "url": "url",
                        },
                    },
                    "message": "message",
                    "revision": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "client_id": "Angular",
                        "counters": {
                            "comments": 0,
                            "forks": 0,
                            "likes": 0,
                            "plays": 0,
                        },
                        "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "creator": {
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
                        "description": "description",
                        "is_fork": True,
                        "is_public": True,
                        "lyrics": {"content": "content"},
                        "mixdown": {
                            "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "name": "name",
                            "status": "Empty",
                        },
                        "parent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "post_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "stamp": "stamp",
                    },
                    "type": "Revision",
                    "video": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "counters": {
                            "likes": 0,
                            "views": 0,
                        },
                        "duration": 0,
                        "picture": {
                            "is_default": True,
                            "l": "l",
                            "m": "m",
                            "s": "s",
                            "url": "url",
                        },
                        "status": "Empty",
                    },
                }
            ],
            type="Playlist",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: BandlabSDK) -> None:
        response = client.collections.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: BandlabSDK) -> None:
        with client.collections.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BandlabSDK) -> None:
        collection = client.collections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BandlabSDK) -> None:
        response = client.collections.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BandlabSDK) -> None:
        with client.collections.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: BandlabSDK) -> None:
        collection = client.collections.update(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: BandlabSDK) -> None:
        collection = client.collections.update(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counters={
                "items": 0,
                "likes": 0,
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
            is_public=True,
            last_updated_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            posts=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "caption": "caption",
                    "client_id": "Angular",
                    "comments": [
                        {
                            "id": 0,
                            "content": "content",
                            "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "creator": {
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
                            "timestamp": 0,
                        }
                    ],
                    "counters": {
                        "comments": 0,
                        "likes": 0,
                        "reposts": 0,
                    },
                    "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "creator": {
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
                    "image": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "counters": {"likes": 0},
                        "picture": {
                            "is_default": True,
                            "l": "l",
                            "m": "m",
                            "s": "s",
                            "url": "url",
                        },
                    },
                    "message": "message",
                    "revision": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "client_id": "Angular",
                        "counters": {
                            "comments": 0,
                            "forks": 0,
                            "likes": 0,
                            "plays": 0,
                        },
                        "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "creator": {
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
                        "description": "description",
                        "is_fork": True,
                        "is_public": True,
                        "lyrics": {"content": "content"},
                        "mixdown": {
                            "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "name": "name",
                            "status": "Empty",
                        },
                        "parent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "post_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "stamp": "stamp",
                    },
                    "type": "Revision",
                    "video": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "counters": {
                            "likes": 0,
                            "views": 0,
                        },
                        "duration": 0,
                        "picture": {
                            "is_default": True,
                            "l": "l",
                            "m": "m",
                            "s": "s",
                            "url": "url",
                        },
                        "status": "Empty",
                    },
                }
            ],
            type="Playlist",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: BandlabSDK) -> None:
        response = client.collections.with_raw_response.update(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: BandlabSDK) -> None:
        with client.collections.with_streaming_response.update(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.with_raw_response.update(
                collection_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: BandlabSDK) -> None:
        collection = client.collections.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert collection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: BandlabSDK) -> None:
        response = client.collections.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert collection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: BandlabSDK) -> None:
        with client.collections.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert collection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.with_raw_response.delete(
                "",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBandlabSDK) -> None:
        collection = await async_client.collections.create(
            name="name",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        collection = await async_client.collections.create(
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counters={
                "items": 0,
                "likes": 0,
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
            is_public=True,
            last_updated_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            posts=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "caption": "caption",
                    "client_id": "Angular",
                    "comments": [
                        {
                            "id": 0,
                            "content": "content",
                            "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "creator": {
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
                            "timestamp": 0,
                        }
                    ],
                    "counters": {
                        "comments": 0,
                        "likes": 0,
                        "reposts": 0,
                    },
                    "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "creator": {
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
                    "image": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "counters": {"likes": 0},
                        "picture": {
                            "is_default": True,
                            "l": "l",
                            "m": "m",
                            "s": "s",
                            "url": "url",
                        },
                    },
                    "message": "message",
                    "revision": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "client_id": "Angular",
                        "counters": {
                            "comments": 0,
                            "forks": 0,
                            "likes": 0,
                            "plays": 0,
                        },
                        "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "creator": {
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
                        "description": "description",
                        "is_fork": True,
                        "is_public": True,
                        "lyrics": {"content": "content"},
                        "mixdown": {
                            "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "name": "name",
                            "status": "Empty",
                        },
                        "parent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "post_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "stamp": "stamp",
                    },
                    "type": "Revision",
                    "video": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "counters": {
                            "likes": 0,
                            "views": 0,
                        },
                        "duration": 0,
                        "picture": {
                            "is_default": True,
                            "l": "l",
                            "m": "m",
                            "s": "s",
                            "url": "url",
                        },
                        "status": "Empty",
                    },
                }
            ],
            type="Playlist",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.collections.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.collections.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        collection = await async_client.collections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.collections.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.collections.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBandlabSDK) -> None:
        collection = await async_client.collections.update(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        collection = await async_client.collections.update(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counters={
                "items": 0,
                "likes": 0,
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
            is_public=True,
            last_updated_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            picture={
                "is_default": True,
                "l": "l",
                "m": "m",
                "s": "s",
                "url": "url",
            },
            posts=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "caption": "caption",
                    "client_id": "Angular",
                    "comments": [
                        {
                            "id": 0,
                            "content": "content",
                            "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "creator": {
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
                            "timestamp": 0,
                        }
                    ],
                    "counters": {
                        "comments": 0,
                        "likes": 0,
                        "reposts": 0,
                    },
                    "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "creator": {
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
                    "image": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "counters": {"likes": 0},
                        "picture": {
                            "is_default": True,
                            "l": "l",
                            "m": "m",
                            "s": "s",
                            "url": "url",
                        },
                    },
                    "message": "message",
                    "revision": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "client_id": "Angular",
                        "counters": {
                            "comments": 0,
                            "forks": 0,
                            "likes": 0,
                            "plays": 0,
                        },
                        "created_on": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "creator": {
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
                        "description": "description",
                        "is_fork": True,
                        "is_public": True,
                        "lyrics": {"content": "content"},
                        "mixdown": {
                            "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "name": "name",
                            "status": "Empty",
                        },
                        "parent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "post_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "stamp": "stamp",
                    },
                    "type": "Revision",
                    "video": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "counters": {
                            "likes": 0,
                            "views": 0,
                        },
                        "duration": 0,
                        "picture": {
                            "is_default": True,
                            "l": "l",
                            "m": "m",
                            "s": "s",
                            "url": "url",
                        },
                        "status": "Empty",
                    },
                }
            ],
            type="Playlist",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.collections.with_raw_response.update(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.collections.with_streaming_response.update(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.with_raw_response.update(
                collection_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBandlabSDK) -> None:
        collection = await async_client.collections.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert collection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.collections.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert collection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.collections.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert collection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.with_raw_response.delete(
                "",
            )
