# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import validation_validate_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.validation_validate_response import ValidationValidateResponse

__all__ = ["ValidationResource", "AsyncValidationResource"]


class ValidationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ValidationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return ValidationResourceWithStreamingResponse(self)

    def validate(
        self,
        entity_type: Literal["user", "band", "song"],
        *,
        name: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidationValidateResponse:
        """
        Validates the user fields

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_type:
            raise ValueError(f"Expected a non-empty value for `entity_type` but received {entity_type!r}")
        return self._get(
            f"/validation/{entity_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "username": username,
                    },
                    validation_validate_params.ValidationValidateParams,
                ),
            ),
            cast_to=ValidationValidateResponse,
        )


class AsyncValidationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValidationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValidationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bandlab-sdk-python#with_streaming_response
        """
        return AsyncValidationResourceWithStreamingResponse(self)

    async def validate(
        self,
        entity_type: Literal["user", "band", "song"],
        *,
        name: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidationValidateResponse:
        """
        Validates the user fields

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_type:
            raise ValueError(f"Expected a non-empty value for `entity_type` but received {entity_type!r}")
        return await self._get(
            f"/validation/{entity_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "username": username,
                    },
                    validation_validate_params.ValidationValidateParams,
                ),
            ),
            cast_to=ValidationValidateResponse,
        )


class ValidationResourceWithRawResponse:
    def __init__(self, validation: ValidationResource) -> None:
        self._validation = validation

        self.validate = to_raw_response_wrapper(
            validation.validate,
        )


class AsyncValidationResourceWithRawResponse:
    def __init__(self, validation: AsyncValidationResource) -> None:
        self._validation = validation

        self.validate = async_to_raw_response_wrapper(
            validation.validate,
        )


class ValidationResourceWithStreamingResponse:
    def __init__(self, validation: ValidationResource) -> None:
        self._validation = validation

        self.validate = to_streamed_response_wrapper(
            validation.validate,
        )


class AsyncValidationResourceWithStreamingResponse:
    def __init__(self, validation: AsyncValidationResource) -> None:
        self._validation = validation

        self.validate = async_to_streamed_response_wrapper(
            validation.validate,
        )
