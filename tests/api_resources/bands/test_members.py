# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bandlab_sdk import BandlabSDK, AsyncBandlabSDK
from tests.utils import assert_matches_type
from bandlab_sdk._utils import parse_datetime
from bandlab_sdk.types.bands import GroupMember, GroupMemberList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BandlabSDK) -> None:
        member = client.bands.members.retrieve(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BandlabSDK) -> None:
        response = client.bands.members.with_raw_response.retrieve(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BandlabSDK) -> None:
        with client.bands.members.with_streaming_response.retrieve(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(GroupMember, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            client.bands.members.with_raw_response.retrieve(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                band_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.bands.members.with_raw_response.retrieve(
                user_id="",
                band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: BandlabSDK) -> None:
        member = client.bands.members.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: BandlabSDK) -> None:
        member = client.bands.members.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            badges=["string"],
            counters={
                "bands": 0,
                "collections": 0,
                "followers": 0,
                "following": 0,
            },
            created_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
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
            role="None",
            skills=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            username="username",
        )
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: BandlabSDK) -> None:
        response = client.bands.members.with_raw_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: BandlabSDK) -> None:
        with client.bands.members.with_streaming_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(GroupMember, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            client.bands.members.with_raw_response.update(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                band_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.bands.members.with_raw_response.update(
                user_id="",
                band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: BandlabSDK) -> None:
        member = client.bands.members.list(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupMemberList, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BandlabSDK) -> None:
        member = client.bands.members.list(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(GroupMemberList, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BandlabSDK) -> None:
        response = client.bands.members.with_raw_response.list(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(GroupMemberList, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BandlabSDK) -> None:
        with client.bands.members.with_streaming_response.list(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(GroupMemberList, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            client.bands.members.with_raw_response.list(
                band_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: BandlabSDK) -> None:
        member = client.bands.members.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert member is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: BandlabSDK) -> None:
        response = client.bands.members.with_raw_response.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert member is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: BandlabSDK) -> None:
        with client.bands.members.with_streaming_response.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: BandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            client.bands.members.with_raw_response.remove(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                band_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.bands.members.with_raw_response.remove(
                user_id="",
                band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        member = await async_client.bands.members.retrieve(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.bands.members.with_raw_response.retrieve(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.bands.members.with_streaming_response.retrieve(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(GroupMember, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            await async_client.bands.members.with_raw_response.retrieve(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                band_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.bands.members.with_raw_response.retrieve(
                user_id="",
                band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBandlabSDK) -> None:
        member = await async_client.bands.members.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        member = await async_client.bands.members.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            badges=["string"],
            counters={
                "bands": 0,
                "collections": 0,
                "followers": 0,
                "following": 0,
            },
            created_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            genres=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
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
            role="None",
            skills=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            username="username",
        )
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.bands.members.with_raw_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.bands.members.with_streaming_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(GroupMember, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            await async_client.bands.members.with_raw_response.update(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                band_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.bands.members.with_raw_response.update(
                user_id="",
                band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBandlabSDK) -> None:
        member = await async_client.bands.members.list(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupMemberList, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBandlabSDK) -> None:
        member = await async_client.bands.members.list(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            limit=0,
            offset=0,
        )
        assert_matches_type(GroupMemberList, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.bands.members.with_raw_response.list(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(GroupMemberList, member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.bands.members.with_streaming_response.list(
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(GroupMemberList, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            await async_client.bands.members.with_raw_response.list(
                band_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncBandlabSDK) -> None:
        member = await async_client.bands.members.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert member is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncBandlabSDK) -> None:
        response = await async_client.bands.members.with_raw_response.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert member is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncBandlabSDK) -> None:
        async with async_client.bands.members.with_streaming_response.remove(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncBandlabSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `band_id` but received ''"):
            await async_client.bands.members.with_raw_response.remove(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                band_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.bands.members.with_raw_response.remove(
                user_id="",
                band_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
