# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    me,
    badges,
    genres,
    images,
    labels,
    logins,
    search,
    skills,
    videos,
    invites,
    reports,
    feedback,
    versions,
    passwords,
    revisions,
    validation,
    authorizations,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, BandlabSDKError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.push import push
from .resources.bands import bands
from .resources.posts import posts
from .resources.songs import songs
from .resources.users import users
from .resources.emails import emails
from .resources.settings import settings
from .resources.collections import collections
from .resources.communities import communities

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "BandlabSDK",
    "AsyncBandlabSDK",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://test.bandlab.com/api/v1.3",
    "environment_1": "https://bandlab.com/api/v1.3",
}


class BandlabSDK(SyncAPIClient):
    validation: validation.ValidationResource
    me: me.MeResource
    users: users.UsersResource
    bands: bands.BandsResource
    collections: collections.CollectionsResource
    posts: posts.PostsResource
    videos: videos.VideosResource
    images: images.ImagesResource
    revisions: revisions.RevisionsResource
    invites: invites.InvitesResource
    reports: reports.ReportsResource
    feedback: feedback.FeedbackResource
    versions: versions.VersionsResource
    labels: labels.LabelsResource
    genres: genres.GenresResource
    skills: skills.SkillsResource
    badges: badges.BadgesResource
    push: push.PushResource
    search: search.SearchResource
    authorizations: authorizations.AuthorizationsResource
    logins: logins.LoginsResource
    emails: emails.EmailsResource
    passwords: passwords.PasswordsResource
    settings: settings.SettingsResource
    communities: communities.CommunitiesResource
    songs: songs.SongsResource
    with_raw_response: BandlabSDKWithRawResponse
    with_streaming_response: BandlabSDKWithStreamedResponse

    # client options
    bearer_token: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous BandlabSDK client instance.

        This automatically infers the `bearer_token` argument from the `BANDLAB_SDK_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("BANDLAB_SDK_BEARER_TOKEN")
        if bearer_token is None:
            raise BandlabSDKError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the BANDLAB_SDK_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("BANDLAB_SDK_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `BANDLAB_SDK_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.validation = validation.ValidationResource(self)
        self.me = me.MeResource(self)
        self.users = users.UsersResource(self)
        self.bands = bands.BandsResource(self)
        self.collections = collections.CollectionsResource(self)
        self.posts = posts.PostsResource(self)
        self.videos = videos.VideosResource(self)
        self.images = images.ImagesResource(self)
        self.revisions = revisions.RevisionsResource(self)
        self.invites = invites.InvitesResource(self)
        self.reports = reports.ReportsResource(self)
        self.feedback = feedback.FeedbackResource(self)
        self.versions = versions.VersionsResource(self)
        self.labels = labels.LabelsResource(self)
        self.genres = genres.GenresResource(self)
        self.skills = skills.SkillsResource(self)
        self.badges = badges.BadgesResource(self)
        self.push = push.PushResource(self)
        self.search = search.SearchResource(self)
        self.authorizations = authorizations.AuthorizationsResource(self)
        self.logins = logins.LoginsResource(self)
        self.emails = emails.EmailsResource(self)
        self.passwords = passwords.PasswordsResource(self)
        self.settings = settings.SettingsResource(self)
        self.communities = communities.CommunitiesResource(self)
        self.songs = songs.SongsResource(self)
        self.with_raw_response = BandlabSDKWithRawResponse(self)
        self.with_streaming_response = BandlabSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBandlabSDK(AsyncAPIClient):
    validation: validation.AsyncValidationResource
    me: me.AsyncMeResource
    users: users.AsyncUsersResource
    bands: bands.AsyncBandsResource
    collections: collections.AsyncCollectionsResource
    posts: posts.AsyncPostsResource
    videos: videos.AsyncVideosResource
    images: images.AsyncImagesResource
    revisions: revisions.AsyncRevisionsResource
    invites: invites.AsyncInvitesResource
    reports: reports.AsyncReportsResource
    feedback: feedback.AsyncFeedbackResource
    versions: versions.AsyncVersionsResource
    labels: labels.AsyncLabelsResource
    genres: genres.AsyncGenresResource
    skills: skills.AsyncSkillsResource
    badges: badges.AsyncBadgesResource
    push: push.AsyncPushResource
    search: search.AsyncSearchResource
    authorizations: authorizations.AsyncAuthorizationsResource
    logins: logins.AsyncLoginsResource
    emails: emails.AsyncEmailsResource
    passwords: passwords.AsyncPasswordsResource
    settings: settings.AsyncSettingsResource
    communities: communities.AsyncCommunitiesResource
    songs: songs.AsyncSongsResource
    with_raw_response: AsyncBandlabSDKWithRawResponse
    with_streaming_response: AsyncBandlabSDKWithStreamedResponse

    # client options
    bearer_token: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBandlabSDK client instance.

        This automatically infers the `bearer_token` argument from the `BANDLAB_SDK_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("BANDLAB_SDK_BEARER_TOKEN")
        if bearer_token is None:
            raise BandlabSDKError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the BANDLAB_SDK_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("BANDLAB_SDK_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `BANDLAB_SDK_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.validation = validation.AsyncValidationResource(self)
        self.me = me.AsyncMeResource(self)
        self.users = users.AsyncUsersResource(self)
        self.bands = bands.AsyncBandsResource(self)
        self.collections = collections.AsyncCollectionsResource(self)
        self.posts = posts.AsyncPostsResource(self)
        self.videos = videos.AsyncVideosResource(self)
        self.images = images.AsyncImagesResource(self)
        self.revisions = revisions.AsyncRevisionsResource(self)
        self.invites = invites.AsyncInvitesResource(self)
        self.reports = reports.AsyncReportsResource(self)
        self.feedback = feedback.AsyncFeedbackResource(self)
        self.versions = versions.AsyncVersionsResource(self)
        self.labels = labels.AsyncLabelsResource(self)
        self.genres = genres.AsyncGenresResource(self)
        self.skills = skills.AsyncSkillsResource(self)
        self.badges = badges.AsyncBadgesResource(self)
        self.push = push.AsyncPushResource(self)
        self.search = search.AsyncSearchResource(self)
        self.authorizations = authorizations.AsyncAuthorizationsResource(self)
        self.logins = logins.AsyncLoginsResource(self)
        self.emails = emails.AsyncEmailsResource(self)
        self.passwords = passwords.AsyncPasswordsResource(self)
        self.settings = settings.AsyncSettingsResource(self)
        self.communities = communities.AsyncCommunitiesResource(self)
        self.songs = songs.AsyncSongsResource(self)
        self.with_raw_response = AsyncBandlabSDKWithRawResponse(self)
        self.with_streaming_response = AsyncBandlabSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BandlabSDKWithRawResponse:
    def __init__(self, client: BandlabSDK) -> None:
        self.validation = validation.ValidationResourceWithRawResponse(client.validation)
        self.me = me.MeResourceWithRawResponse(client.me)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.bands = bands.BandsResourceWithRawResponse(client.bands)
        self.collections = collections.CollectionsResourceWithRawResponse(client.collections)
        self.posts = posts.PostsResourceWithRawResponse(client.posts)
        self.videos = videos.VideosResourceWithRawResponse(client.videos)
        self.images = images.ImagesResourceWithRawResponse(client.images)
        self.revisions = revisions.RevisionsResourceWithRawResponse(client.revisions)
        self.invites = invites.InvitesResourceWithRawResponse(client.invites)
        self.reports = reports.ReportsResourceWithRawResponse(client.reports)
        self.feedback = feedback.FeedbackResourceWithRawResponse(client.feedback)
        self.versions = versions.VersionsResourceWithRawResponse(client.versions)
        self.labels = labels.LabelsResourceWithRawResponse(client.labels)
        self.genres = genres.GenresResourceWithRawResponse(client.genres)
        self.skills = skills.SkillsResourceWithRawResponse(client.skills)
        self.badges = badges.BadgesResourceWithRawResponse(client.badges)
        self.push = push.PushResourceWithRawResponse(client.push)
        self.search = search.SearchResourceWithRawResponse(client.search)
        self.authorizations = authorizations.AuthorizationsResourceWithRawResponse(client.authorizations)
        self.logins = logins.LoginsResourceWithRawResponse(client.logins)
        self.emails = emails.EmailsResourceWithRawResponse(client.emails)
        self.passwords = passwords.PasswordsResourceWithRawResponse(client.passwords)
        self.settings = settings.SettingsResourceWithRawResponse(client.settings)
        self.communities = communities.CommunitiesResourceWithRawResponse(client.communities)
        self.songs = songs.SongsResourceWithRawResponse(client.songs)


class AsyncBandlabSDKWithRawResponse:
    def __init__(self, client: AsyncBandlabSDK) -> None:
        self.validation = validation.AsyncValidationResourceWithRawResponse(client.validation)
        self.me = me.AsyncMeResourceWithRawResponse(client.me)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.bands = bands.AsyncBandsResourceWithRawResponse(client.bands)
        self.collections = collections.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.posts = posts.AsyncPostsResourceWithRawResponse(client.posts)
        self.videos = videos.AsyncVideosResourceWithRawResponse(client.videos)
        self.images = images.AsyncImagesResourceWithRawResponse(client.images)
        self.revisions = revisions.AsyncRevisionsResourceWithRawResponse(client.revisions)
        self.invites = invites.AsyncInvitesResourceWithRawResponse(client.invites)
        self.reports = reports.AsyncReportsResourceWithRawResponse(client.reports)
        self.feedback = feedback.AsyncFeedbackResourceWithRawResponse(client.feedback)
        self.versions = versions.AsyncVersionsResourceWithRawResponse(client.versions)
        self.labels = labels.AsyncLabelsResourceWithRawResponse(client.labels)
        self.genres = genres.AsyncGenresResourceWithRawResponse(client.genres)
        self.skills = skills.AsyncSkillsResourceWithRawResponse(client.skills)
        self.badges = badges.AsyncBadgesResourceWithRawResponse(client.badges)
        self.push = push.AsyncPushResourceWithRawResponse(client.push)
        self.search = search.AsyncSearchResourceWithRawResponse(client.search)
        self.authorizations = authorizations.AsyncAuthorizationsResourceWithRawResponse(client.authorizations)
        self.logins = logins.AsyncLoginsResourceWithRawResponse(client.logins)
        self.emails = emails.AsyncEmailsResourceWithRawResponse(client.emails)
        self.passwords = passwords.AsyncPasswordsResourceWithRawResponse(client.passwords)
        self.settings = settings.AsyncSettingsResourceWithRawResponse(client.settings)
        self.communities = communities.AsyncCommunitiesResourceWithRawResponse(client.communities)
        self.songs = songs.AsyncSongsResourceWithRawResponse(client.songs)


class BandlabSDKWithStreamedResponse:
    def __init__(self, client: BandlabSDK) -> None:
        self.validation = validation.ValidationResourceWithStreamingResponse(client.validation)
        self.me = me.MeResourceWithStreamingResponse(client.me)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.bands = bands.BandsResourceWithStreamingResponse(client.bands)
        self.collections = collections.CollectionsResourceWithStreamingResponse(client.collections)
        self.posts = posts.PostsResourceWithStreamingResponse(client.posts)
        self.videos = videos.VideosResourceWithStreamingResponse(client.videos)
        self.images = images.ImagesResourceWithStreamingResponse(client.images)
        self.revisions = revisions.RevisionsResourceWithStreamingResponse(client.revisions)
        self.invites = invites.InvitesResourceWithStreamingResponse(client.invites)
        self.reports = reports.ReportsResourceWithStreamingResponse(client.reports)
        self.feedback = feedback.FeedbackResourceWithStreamingResponse(client.feedback)
        self.versions = versions.VersionsResourceWithStreamingResponse(client.versions)
        self.labels = labels.LabelsResourceWithStreamingResponse(client.labels)
        self.genres = genres.GenresResourceWithStreamingResponse(client.genres)
        self.skills = skills.SkillsResourceWithStreamingResponse(client.skills)
        self.badges = badges.BadgesResourceWithStreamingResponse(client.badges)
        self.push = push.PushResourceWithStreamingResponse(client.push)
        self.search = search.SearchResourceWithStreamingResponse(client.search)
        self.authorizations = authorizations.AuthorizationsResourceWithStreamingResponse(client.authorizations)
        self.logins = logins.LoginsResourceWithStreamingResponse(client.logins)
        self.emails = emails.EmailsResourceWithStreamingResponse(client.emails)
        self.passwords = passwords.PasswordsResourceWithStreamingResponse(client.passwords)
        self.settings = settings.SettingsResourceWithStreamingResponse(client.settings)
        self.communities = communities.CommunitiesResourceWithStreamingResponse(client.communities)
        self.songs = songs.SongsResourceWithStreamingResponse(client.songs)


class AsyncBandlabSDKWithStreamedResponse:
    def __init__(self, client: AsyncBandlabSDK) -> None:
        self.validation = validation.AsyncValidationResourceWithStreamingResponse(client.validation)
        self.me = me.AsyncMeResourceWithStreamingResponse(client.me)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.bands = bands.AsyncBandsResourceWithStreamingResponse(client.bands)
        self.collections = collections.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.posts = posts.AsyncPostsResourceWithStreamingResponse(client.posts)
        self.videos = videos.AsyncVideosResourceWithStreamingResponse(client.videos)
        self.images = images.AsyncImagesResourceWithStreamingResponse(client.images)
        self.revisions = revisions.AsyncRevisionsResourceWithStreamingResponse(client.revisions)
        self.invites = invites.AsyncInvitesResourceWithStreamingResponse(client.invites)
        self.reports = reports.AsyncReportsResourceWithStreamingResponse(client.reports)
        self.feedback = feedback.AsyncFeedbackResourceWithStreamingResponse(client.feedback)
        self.versions = versions.AsyncVersionsResourceWithStreamingResponse(client.versions)
        self.labels = labels.AsyncLabelsResourceWithStreamingResponse(client.labels)
        self.genres = genres.AsyncGenresResourceWithStreamingResponse(client.genres)
        self.skills = skills.AsyncSkillsResourceWithStreamingResponse(client.skills)
        self.badges = badges.AsyncBadgesResourceWithStreamingResponse(client.badges)
        self.push = push.AsyncPushResourceWithStreamingResponse(client.push)
        self.search = search.AsyncSearchResourceWithStreamingResponse(client.search)
        self.authorizations = authorizations.AsyncAuthorizationsResourceWithStreamingResponse(client.authorizations)
        self.logins = logins.AsyncLoginsResourceWithStreamingResponse(client.logins)
        self.emails = emails.AsyncEmailsResourceWithStreamingResponse(client.emails)
        self.passwords = passwords.AsyncPasswordsResourceWithStreamingResponse(client.passwords)
        self.settings = settings.AsyncSettingsResourceWithStreamingResponse(client.settings)
        self.communities = communities.AsyncCommunitiesResourceWithStreamingResponse(client.communities)
        self.songs = songs.AsyncSongsResourceWithStreamingResponse(client.songs)


Client = BandlabSDK

AsyncClient = AsyncBandlabSDK
