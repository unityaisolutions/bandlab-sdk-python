# Shared Types

```python
from bandlab_sdk.types import (
    ImageSample,
    ImageSampleCounters,
    Lyrics,
    PostCounters,
    RevisionSummary,
    VideoSample,
    VideoSampleCounters,
)
```

# Validation

Types:

```python
from bandlab_sdk.types import ValidationValidateResponse
```

Methods:

- <code title="get /validation/{entityType}">client.validation.<a href="./src/bandlab_sdk/resources/validation.py">validate</a>(entity_type, \*\*<a href="src/bandlab_sdk/types/validation_validate_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/validation_validate_response.py">ValidationValidateResponse</a></code>

# Me

Types:

```python
from bandlab_sdk.types import GeoCoordinate, Location, Picture, Profile, UserCounters
```

Methods:

- <code title="get /me">client.me.<a href="./src/bandlab_sdk/resources/me.py">retrieve</a>() -> <a href="./src/bandlab_sdk/types/profile.py">Profile</a></code>
- <code title="patch /me">client.me.<a href="./src/bandlab_sdk/resources/me.py">update</a>(\*\*<a href="src/bandlab_sdk/types/me_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/profile.py">Profile</a></code>

# Users

Types:

```python
from bandlab_sdk.types import (
    CollectionList,
    SongList,
    UserRetrieveResponse,
    UserCreateAccessKeyResponse,
    UserListCommunitiesResponse,
)
```

Methods:

- <code title="get /users/{userId}">client.users.<a href="./src/bandlab_sdk/resources/users/users.py">retrieve</a>(user_id) -> <a href="./src/bandlab_sdk/types/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="post /users/{userId}/keys">client.users.<a href="./src/bandlab_sdk/resources/users/users.py">create_access_key</a>(user_id) -> <a href="./src/bandlab_sdk/types/user_create_access_key_response.py">UserCreateAccessKeyResponse</a></code>
- <code title="get /users/{userId}/bands">client.users.<a href="./src/bandlab_sdk/resources/users/users.py">list_bands</a>(user_id, \*\*<a href="src/bandlab_sdk/types/user_list_bands_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/band.py">Band</a></code>
- <code title="get /users/{userId}/collections">client.users.<a href="./src/bandlab_sdk/resources/users/users.py">list_collections</a>(user_id, \*\*<a href="src/bandlab_sdk/types/user_list_collections_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collection_list.py">CollectionList</a></code>
- <code title="get /users/{userId}/communities">client.users.<a href="./src/bandlab_sdk/resources/users/users.py">list_communities</a>(user_id, \*\*<a href="src/bandlab_sdk/types/user_list_communities_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/user_list_communities_response.py">UserListCommunitiesResponse</a></code>
- <code title="get /users/{userId}/posts">client.users.<a href="./src/bandlab_sdk/resources/users/users.py">list_posts</a>(user_id, \*\*<a href="src/bandlab_sdk/types/user_list_posts_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/post_list.py">PostList</a></code>
- <code title="get /users/{userId}/songs">client.users.<a href="./src/bandlab_sdk/resources/users/users.py">list_songs</a>(user_id, \*\*<a href="src/bandlab_sdk/types/user_list_songs_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/song_list.py">SongList</a></code>

## Followers

Types:

```python
from bandlab_sdk.types.users import Paging, UserList
```

Methods:

- <code title="get /users/{userId}/followers">client.users.followers.<a href="./src/bandlab_sdk/resources/users/followers.py">list</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/follower_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/users/user_list.py">UserList</a></code>
- <code title="post /users/{userId}/followers">client.users.followers.<a href="./src/bandlab_sdk/resources/users/followers.py">add</a>(user_id) -> None</code>
- <code title="delete /users/{userId}/followers">client.users.followers.<a href="./src/bandlab_sdk/resources/users/followers.py">remove</a>(user_id) -> None</code>

## Following

Methods:

- <code title="get /users/{userId}/following">client.users.following.<a href="./src/bandlab_sdk/resources/users/following.py">list</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/following_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/users/user_list.py">UserList</a></code>
- <code title="get /users/{userId}/following/posts">client.users.following.<a href="./src/bandlab_sdk/resources/users/following.py">list_posts</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/following_list_posts_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/post_list.py">PostList</a></code>

## Invites

Types:

```python
from bandlab_sdk.types.users import InviteList
```

Methods:

- <code title="get /users/{userId}/invites">client.users.invites.<a href="./src/bandlab_sdk/resources/users/invites.py">list</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/invite_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/users/invite_list.py">InviteList</a></code>
- <code title="post /users/{userId}/invites">client.users.invites.<a href="./src/bandlab_sdk/resources/users/invites.py">send</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/invite_send_params.py">params</a>) -> None</code>

## Notifications

Types:

```python
from bandlab_sdk.types.users import NotificationList, NotificationPatch, NotificationCountResponse
```

Methods:

- <code title="patch /users/{userId}/notifications/{notificationId}">client.users.notifications.<a href="./src/bandlab_sdk/resources/users/notifications.py">update</a>(notification_id, \*, user_id, \*\*<a href="src/bandlab_sdk/types/users/notification_update_params.py">params</a>) -> None</code>
- <code title="get /users/{userId}/notifications">client.users.notifications.<a href="./src/bandlab_sdk/resources/users/notifications.py">list</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/notification_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/users/notification_list.py">NotificationList</a></code>
- <code title="get /users/{userId}/notifications/count">client.users.notifications.<a href="./src/bandlab_sdk/resources/users/notifications.py">count</a>(user_id) -> <a href="./src/bandlab_sdk/types/users/notification_count_response.py">NotificationCountResponse</a></code>
- <code title="get /users/{userId}/notifications/following">client.users.notifications.<a href="./src/bandlab_sdk/resources/users/notifications.py">list_following</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/notification_list_following_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/users/notification_list.py">NotificationList</a></code>
- <code title="patch /users/{userId}/notifications">client.users.notifications.<a href="./src/bandlab_sdk/resources/users/notifications.py">update_all</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/notification_update_all_params.py">params</a>) -> None</code>

## Recommendations

Methods:

- <code title="get /users/{userId}/recommendations/users">client.users.recommendations.<a href="./src/bandlab_sdk/resources/users/recommendations.py">list_users</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/recommendation_list_users_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collections/user_summary_list.py">UserSummaryList</a></code>

## Contacts

Types:

```python
from bandlab_sdk.types.users import ContactListBandsResponse
```

Methods:

- <code title="get /users/{userId}/contacts/bands">client.users.contacts.<a href="./src/bandlab_sdk/resources/users/contacts.py">list_bands</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/contact_list_bands_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/users/contact_list_bands_response.py">ContactListBandsResponse</a></code>
- <code title="get /users/{userId}/contacts/users">client.users.contacts.<a href="./src/bandlab_sdk/resources/users/contacts.py">list_users</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/contact_list_users_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collections/user_summary_list.py">UserSummaryList</a></code>

## Blocks

### Users

Methods:

- <code title="get /users/{userId}/blocks/users">client.users.blocks.users.<a href="./src/bandlab_sdk/resources/users/blocks/users.py">list</a>(user_id, \*\*<a href="src/bandlab_sdk/types/users/blocks/user_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collections/user_summary_list.py">UserSummaryList</a></code>
- <code title="post /users/{userId}/blocks/users/{blockedUserId}">client.users.blocks.users.<a href="./src/bandlab_sdk/resources/users/blocks/users.py">add</a>(blocked_user_id, \*, user_id) -> None</code>
- <code title="delete /users/{userId}/blocks/users/{blockedUserId}">client.users.blocks.users.<a href="./src/bandlab_sdk/resources/users/blocks/users.py">remove</a>(blocked_user_id, \*, user_id) -> None</code>

# Bands

Types:

```python
from bandlab_sdk.types import Band, BandCounters, Creator, GroupMemberSummary
```

Methods:

- <code title="post /bands">client.bands.<a href="./src/bandlab_sdk/resources/bands/bands.py">create</a>(\*\*<a href="src/bandlab_sdk/types/band_create_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/band.py">Band</a></code>
- <code title="get /bands/{bandId}">client.bands.<a href="./src/bandlab_sdk/resources/bands/bands.py">retrieve</a>(band_id) -> <a href="./src/bandlab_sdk/types/band.py">Band</a></code>
- <code title="patch /bands/{bandId}">client.bands.<a href="./src/bandlab_sdk/resources/bands/bands.py">update</a>(band_id, \*\*<a href="src/bandlab_sdk/types/band_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/band.py">Band</a></code>
- <code title="delete /bands/{bandId}">client.bands.<a href="./src/bandlab_sdk/resources/bands/bands.py">delete</a>(band_id) -> None</code>
- <code title="get /bands/{bandId}/posts">client.bands.<a href="./src/bandlab_sdk/resources/bands/bands.py">list_posts</a>(band_id, \*\*<a href="src/bandlab_sdk/types/band_list_posts_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/post_list.py">PostList</a></code>
- <code title="get /bands/{bandId}/songs">client.bands.<a href="./src/bandlab_sdk/resources/bands/bands.py">list_songs</a>(band_id, \*\*<a href="src/bandlab_sdk/types/band_list_songs_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/song_list.py">SongList</a></code>

## Members

Types:

```python
from bandlab_sdk.types.bands import GroupMember, GroupMemberList
```

Methods:

- <code title="get /bands/{bandId}/members/{userId}">client.bands.members.<a href="./src/bandlab_sdk/resources/bands/members.py">retrieve</a>(user_id, \*, band_id) -> <a href="./src/bandlab_sdk/types/bands/group_member.py">GroupMember</a></code>
- <code title="patch /bands/{bandId}/members/{userId}">client.bands.members.<a href="./src/bandlab_sdk/resources/bands/members.py">update</a>(user_id, \*, band_id, \*\*<a href="src/bandlab_sdk/types/bands/member_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/bands/group_member.py">GroupMember</a></code>
- <code title="get /bands/{bandId}/members">client.bands.members.<a href="./src/bandlab_sdk/resources/bands/members.py">list</a>(band_id, \*\*<a href="src/bandlab_sdk/types/bands/member_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/bands/group_member_list.py">GroupMemberList</a></code>
- <code title="delete /bands/{bandId}/members/{userId}">client.bands.members.<a href="./src/bandlab_sdk/resources/bands/members.py">remove</a>(user_id, \*, band_id) -> None</code>

## Invites

Methods:

- <code title="get /bands/{bandId}/invites">client.bands.invites.<a href="./src/bandlab_sdk/resources/bands/invites.py">list</a>(band_id, \*\*<a href="src/bandlab_sdk/types/bands/invite_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/users/invite_list.py">InviteList</a></code>
- <code title="post /bands/{bandId}/invites">client.bands.invites.<a href="./src/bandlab_sdk/resources/bands/invites.py">send</a>(band_id, \*\*<a href="src/bandlab_sdk/types/bands/invite_send_params.py">params</a>) -> None</code>

# Collections

Types:

```python
from bandlab_sdk.types import Collection, CollectionCounters
```

Methods:

- <code title="post /collections">client.collections.<a href="./src/bandlab_sdk/resources/collections/collections.py">create</a>(\*\*<a href="src/bandlab_sdk/types/collection_create_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collection.py">Collection</a></code>
- <code title="get /collections/{collectionId}">client.collections.<a href="./src/bandlab_sdk/resources/collections/collections.py">retrieve</a>(collection_id) -> <a href="./src/bandlab_sdk/types/collection.py">Collection</a></code>
- <code title="patch /collections/{collectionId}">client.collections.<a href="./src/bandlab_sdk/resources/collections/collections.py">update</a>(collection_id, \*\*<a href="src/bandlab_sdk/types/collection_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collection.py">Collection</a></code>
- <code title="delete /collections/{collectionId}">client.collections.<a href="./src/bandlab_sdk/resources/collections/collections.py">delete</a>(collection_id) -> None</code>

## Posts

Types:

```python
from bandlab_sdk.types.collections import ClientID, Post, Status
```

Methods:

- <code title="get /collections/{collectionId}/posts/{postId}">client.collections.posts.<a href="./src/bandlab_sdk/resources/collections/posts.py">retrieve</a>(post_id, \*, collection_id) -> <a href="./src/bandlab_sdk/types/collections/post.py">Post</a></code>
- <code title="post /collections/{collectionId}/posts/{postId}">client.collections.posts.<a href="./src/bandlab_sdk/resources/collections/posts.py">add</a>(post_id, \*, collection_id) -> <a href="./src/bandlab_sdk/types/collections/post.py">Post</a></code>
- <code title="delete /collections/{collectionId}/posts/{postId}">client.collections.posts.<a href="./src/bandlab_sdk/resources/collections/posts.py">remove</a>(post_id, \*, collection_id) -> None</code>
- <code title="patch /collections/{collectionId}/posts/{postId}">client.collections.posts.<a href="./src/bandlab_sdk/resources/collections/posts.py">update_position</a>(post_id, \*, collection_id, \*\*<a href="src/bandlab_sdk/types/collections/post_update_position_params.py">params</a>) -> None</code>

## Likes

Types:

```python
from bandlab_sdk.types.collections import UserSummaryList
```

Methods:

- <code title="get /collections/{collectionId}/likes">client.collections.likes.<a href="./src/bandlab_sdk/resources/collections/likes.py">list</a>(collection_id, \*\*<a href="src/bandlab_sdk/types/collections/like_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collections/user_summary_list.py">UserSummaryList</a></code>
- <code title="post /collections/{collectionId}/likes">client.collections.likes.<a href="./src/bandlab_sdk/resources/collections/likes.py">add</a>(collection_id) -> None</code>
- <code title="delete /collections/{collectionId}/likes">client.collections.likes.<a href="./src/bandlab_sdk/resources/collections/likes.py">remove</a>(collection_id) -> None</code>

# Posts

Types:

```python
from bandlab_sdk.types import Invite, PostList, SongSummary, UserSummary
```

Methods:

- <code title="get /posts/{postId}">client.posts.<a href="./src/bandlab_sdk/resources/posts/posts.py">retrieve</a>(post_id) -> <a href="./src/bandlab_sdk/types/invite.py">Invite</a></code>
- <code title="patch /posts/{postId}">client.posts.<a href="./src/bandlab_sdk/resources/posts/posts.py">update</a>(post_id) -> None</code>
- <code title="get /posts">client.posts.<a href="./src/bandlab_sdk/resources/posts/posts.py">list</a>(\*\*<a href="src/bandlab_sdk/types/post_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/post_list.py">PostList</a></code>
- <code title="delete /posts/{postId}">client.posts.<a href="./src/bandlab_sdk/resources/posts/posts.py">delete</a>(post_id) -> None</code>

## Comments

Types:

```python
from bandlab_sdk.types.posts import Comment, CommentListResponse
```

Methods:

- <code title="post /posts/{postId}/comments">client.posts.comments.<a href="./src/bandlab_sdk/resources/posts/comments.py">create</a>(post_id, \*\*<a href="src/bandlab_sdk/types/posts/comment_create_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/posts/comment.py">Comment</a></code>
- <code title="get /posts/{postId}/comments">client.posts.comments.<a href="./src/bandlab_sdk/resources/posts/comments.py">list</a>(post_id, \*\*<a href="src/bandlab_sdk/types/posts/comment_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/posts/comment_list_response.py">CommentListResponse</a></code>
- <code title="delete /posts/{postId}/comments/{commentId}">client.posts.comments.<a href="./src/bandlab_sdk/resources/posts/comments.py">delete</a>(comment_id, \*, post_id) -> None</code>

## Likes

Methods:

- <code title="post /posts/{postId}/likes">client.posts.likes.<a href="./src/bandlab_sdk/resources/posts/likes.py">create</a>(post_id) -> None</code>
- <code title="get /posts/{postId}/likes">client.posts.likes.<a href="./src/bandlab_sdk/resources/posts/likes.py">list</a>(post_id, \*\*<a href="src/bandlab_sdk/types/posts/like_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collections/user_summary_list.py">UserSummaryList</a></code>
- <code title="delete /posts/{postId}/likes">client.posts.likes.<a href="./src/bandlab_sdk/resources/posts/likes.py">delete</a>(post_id) -> None</code>

# Videos

Methods:

- <code title="post /videos/{videoId}/views">client.videos.<a href="./src/bandlab_sdk/resources/videos.py">add_view</a>(video_id) -> None</code>
- <code title="post /videos/{videoId}/posts">client.videos.<a href="./src/bandlab_sdk/resources/videos.py">create_post</a>(video_id, \*\*<a href="src/bandlab_sdk/types/video_create_post_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collections/post.py">Post</a></code>

# Images

Methods:

- <code title="post /images/{imageId}/posts">client.images.<a href="./src/bandlab_sdk/resources/images.py">create_post</a>(image_id, \*\*<a href="src/bandlab_sdk/types/image_create_post_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collections/post.py">Post</a></code>

# Revisions

Types:

```python
from bandlab_sdk.types import AudioSample, Mastering, Revision, RevisionCounters
```

Methods:

- <code title="post /revisions">client.revisions.<a href="./src/bandlab_sdk/resources/revisions.py">create</a>(\*\*<a href="src/bandlab_sdk/types/revision_create_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/revision.py">Revision</a></code>
- <code title="get /revisions/{revisionId}">client.revisions.<a href="./src/bandlab_sdk/resources/revisions.py">retrieve</a>(revision_id) -> <a href="./src/bandlab_sdk/types/revision.py">Revision</a></code>
- <code title="patch /revisions/{revisionId}">client.revisions.<a href="./src/bandlab_sdk/resources/revisions.py">update</a>(revision_id, \*\*<a href="src/bandlab_sdk/types/revision_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/revision.py">Revision</a></code>
- <code title="post /revisions/{revisionId}/plays">client.revisions.<a href="./src/bandlab_sdk/resources/revisions.py">add_play</a>(revision_id) -> None</code>

# Invites

Types:

```python
from bandlab_sdk.types import InviteBatch
```

Methods:

- <code title="get /invites/{inviteId}">client.invites.<a href="./src/bandlab_sdk/resources/invites.py">retrieve</a>(invite_id) -> <a href="./src/bandlab_sdk/types/invite.py">Invite</a></code>
- <code title="delete /invites/{inviteId}">client.invites.<a href="./src/bandlab_sdk/resources/invites.py">delete</a>(invite_id) -> None</code>
- <code title="put /invites/{inviteId}">client.invites.<a href="./src/bandlab_sdk/resources/invites.py">accept</a>(invite_id) -> None</code>
- <code title="post /invites">client.invites.<a href="./src/bandlab_sdk/resources/invites.py">send</a>(\*\*<a href="src/bandlab_sdk/types/invite_send_params.py">params</a>) -> None</code>

# Reports

Methods:

- <code title="post /reports">client.reports.<a href="./src/bandlab_sdk/resources/reports.py">create</a>(\*\*<a href="src/bandlab_sdk/types/report_create_params.py">params</a>) -> None</code>

# Feedback

Methods:

- <code title="post /feedback">client.feedback.<a href="./src/bandlab_sdk/resources/feedback.py">create</a>(\*\*<a href="src/bandlab_sdk/types/feedback_create_params.py">params</a>) -> None</code>

# Versions

Types:

```python
from bandlab_sdk.types import VersionRetrieveResponse, VersionValidateResponse
```

Methods:

- <code title="get /versions/{clientId}">client.versions.<a href="./src/bandlab_sdk/resources/versions.py">retrieve</a>(client_id) -> <a href="./src/bandlab_sdk/types/version_retrieve_response.py">VersionRetrieveResponse</a></code>
- <code title="get /versions/{clientId}/{version}/valid">client.versions.<a href="./src/bandlab_sdk/resources/versions.py">validate</a>(version, \*, client_id, \*\*<a href="src/bandlab_sdk/types/version_validate_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/version_validate_response.py">VersionValidateResponse</a></code>

# Labels

Types:

```python
from bandlab_sdk.types import LabelListResponse
```

Methods:

- <code title="get /labels">client.labels.<a href="./src/bandlab_sdk/resources/labels.py">list</a>() -> <a href="./src/bandlab_sdk/types/label_list_response.py">LabelListResponse</a></code>

# Genres

Types:

```python
from bandlab_sdk.types import Genre, GenreListResponse
```

Methods:

- <code title="get /genres">client.genres.<a href="./src/bandlab_sdk/resources/genres.py">list</a>() -> <a href="./src/bandlab_sdk/types/genre_list_response.py">GenreListResponse</a></code>

# Skills

Types:

```python
from bandlab_sdk.types import Skill, SkillListResponse
```

Methods:

- <code title="get /skills">client.skills.<a href="./src/bandlab_sdk/resources/skills.py">list</a>() -> <a href="./src/bandlab_sdk/types/skill_list_response.py">SkillListResponse</a></code>

# Badges

Types:

```python
from bandlab_sdk.types import Badge, BadgeListResponse
```

Methods:

- <code title="get /badges">client.badges.<a href="./src/bandlab_sdk/resources/badges.py">list</a>() -> <a href="./src/bandlab_sdk/types/badge_list_response.py">BadgeListResponse</a></code>

# Push

## Registrations

Methods:

- <code title="post /push/registrations">client.push.registrations.<a href="./src/bandlab_sdk/resources/push/registrations.py">create</a>(\*\*<a href="src/bandlab_sdk/types/push/registration_create_params.py">params</a>) -> None</code>
- <code title="delete /push/registrations">client.push.registrations.<a href="./src/bandlab_sdk/resources/push/registrations.py">delete</a>(\*\*<a href="src/bandlab_sdk/types/push/registration_delete_params.py">params</a>) -> None</code>

# Search

Types:

```python
from bandlab_sdk.types import SearchGlobalSearchResponse, SearchSearchBandsResponse
```

Methods:

- <code title="get /search">client.search.<a href="./src/bandlab_sdk/resources/search.py">global_search</a>(\*\*<a href="src/bandlab_sdk/types/search_global_search_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/search_global_search_response.py">SearchGlobalSearchResponse</a></code>
- <code title="get /search/bands">client.search.<a href="./src/bandlab_sdk/resources/search.py">search_bands</a>(\*\*<a href="src/bandlab_sdk/types/search_search_bands_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/search_search_bands_response.py">SearchSearchBandsResponse</a></code>
- <code title="get /search/collections">client.search.<a href="./src/bandlab_sdk/resources/search.py">search_collections</a>(\*\*<a href="src/bandlab_sdk/types/search_search_collections_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collection_list.py">CollectionList</a></code>
- <code title="get /search/songs">client.search.<a href="./src/bandlab_sdk/resources/search.py">search_songs</a>(\*\*<a href="src/bandlab_sdk/types/search_search_songs_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/song_list.py">SongList</a></code>
- <code title="get /search/users">client.search.<a href="./src/bandlab_sdk/resources/search.py">search_users</a>(\*\*<a href="src/bandlab_sdk/types/search_search_users_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/users/user_list.py">UserList</a></code>

# Authorizations

Types:

```python
from bandlab_sdk.types import Provider, AuthorizationCreateSessionKeyResponse
```

Methods:

- <code title="post /authorizations">client.authorizations.<a href="./src/bandlab_sdk/resources/authorizations.py">create_session_key</a>(\*\*<a href="src/bandlab_sdk/types/authorization_create_session_key_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/authorization_create_session_key_response.py">AuthorizationCreateSessionKeyResponse</a></code>

# Logins

Types:

```python
from bandlab_sdk.types import Login, ProviderType139, LoginListResponse
```

Methods:

- <code title="post /logins">client.logins.<a href="./src/bandlab_sdk/resources/logins.py">create</a>(\*\*<a href="src/bandlab_sdk/types/login_create_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/login.py">Login</a></code>
- <code title="put /logins/{providerType}">client.logins.<a href="./src/bandlab_sdk/resources/logins.py">update</a>(provider_type, \*\*<a href="src/bandlab_sdk/types/login_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/login.py">Login</a></code>
- <code title="get /logins">client.logins.<a href="./src/bandlab_sdk/resources/logins.py">list</a>() -> <a href="./src/bandlab_sdk/types/login_list_response.py">LoginListResponse</a></code>
- <code title="delete /logins/{providerType}">client.logins.<a href="./src/bandlab_sdk/resources/logins.py">delete</a>(provider_type) -> None</code>

# Emails

## Confirmations

Methods:

- <code title="put /emails/confirmations">client.emails.confirmations.<a href="./src/bandlab_sdk/resources/emails/confirmations.py">confirm</a>(\*\*<a href="src/bandlab_sdk/types/emails/confirmation_confirm_params.py">params</a>) -> None</code>
- <code title="post /emails/confirmations">client.emails.confirmations.<a href="./src/bandlab_sdk/resources/emails/confirmations.py">resend</a>() -> None</code>

# Passwords

Methods:

- <code title="put /passwords">client.passwords.<a href="./src/bandlab_sdk/resources/passwords.py">change</a>(\*\*<a href="src/bandlab_sdk/types/password_change_params.py">params</a>) -> None</code>
- <code title="post /passwords">client.passwords.<a href="./src/bandlab_sdk/resources/passwords.py">reset</a>(\*\*<a href="src/bandlab_sdk/types/password_reset_params.py">params</a>) -> None</code>
- <code title="delete /passwords">client.passwords.<a href="./src/bandlab_sdk/resources/passwords.py">send_restore_email</a>(\*\*<a href="src/bandlab_sdk/types/password_send_restore_email_params.py">params</a>) -> None</code>

# Settings

## Notifications

### Email

Types:

```python
from bandlab_sdk.types.settings.notifications import SettingsEmail
```

Methods:

- <code title="get /settings/notifications/email">client.settings.notifications.email.<a href="./src/bandlab_sdk/resources/settings/notifications/email.py">retrieve</a>() -> <a href="./src/bandlab_sdk/types/settings/notifications/settings_email.py">SettingsEmail</a></code>
- <code title="patch /settings/notifications/email">client.settings.notifications.email.<a href="./src/bandlab_sdk/resources/settings/notifications/email.py">update</a>(\*\*<a href="src/bandlab_sdk/types/settings/notifications/email_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/settings/notifications/settings_email.py">SettingsEmail</a></code>

### Push

Types:

```python
from bandlab_sdk.types.settings.notifications import SettingsPush
```

Methods:

- <code title="get /settings/notifications/push">client.settings.notifications.push.<a href="./src/bandlab_sdk/resources/settings/notifications/push.py">retrieve</a>() -> <a href="./src/bandlab_sdk/types/settings/notifications/settings_email.py">SettingsEmail</a></code>
- <code title="patch /settings/notifications/push">client.settings.notifications.push.<a href="./src/bandlab_sdk/resources/settings/notifications/push.py">update</a>(\*\*<a href="src/bandlab_sdk/types/settings/notifications/push_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/settings/notifications/settings_push.py">SettingsPush</a></code>

# Communities

Types:

```python
from bandlab_sdk.types import Community, CommunityCounters, Type
```

Methods:

- <code title="post /communities">client.communities.<a href="./src/bandlab_sdk/resources/communities/communities.py">create</a>(\*\*<a href="src/bandlab_sdk/types/community_create_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/community.py">Community</a></code>
- <code title="get /communities/{communityId}">client.communities.<a href="./src/bandlab_sdk/resources/communities/communities.py">retrieve</a>(community_id) -> <a href="./src/bandlab_sdk/types/community.py">Community</a></code>
- <code title="patch /communities/{communityId}">client.communities.<a href="./src/bandlab_sdk/resources/communities/communities.py">update</a>(community_id, \*\*<a href="src/bandlab_sdk/types/community_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/community.py">Community</a></code>
- <code title="delete /communities/{communityId}">client.communities.<a href="./src/bandlab_sdk/resources/communities/communities.py">delete</a>(community_id) -> None</code>

## Members

Methods:

- <code title="get /communities/{communityId}/members/{userId}">client.communities.members.<a href="./src/bandlab_sdk/resources/communities/members.py">retrieve</a>(user_id, \*, community_id) -> <a href="./src/bandlab_sdk/types/bands/group_member.py">GroupMember</a></code>
- <code title="patch /communities/{communityId}/members/{userId}">client.communities.members.<a href="./src/bandlab_sdk/resources/communities/members.py">update</a>(user_id, \*, community_id, \*\*<a href="src/bandlab_sdk/types/communities/member_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/bands/group_member.py">GroupMember</a></code>
- <code title="get /communities/{communityId}/members">client.communities.members.<a href="./src/bandlab_sdk/resources/communities/members.py">list</a>(community_id, \*\*<a href="src/bandlab_sdk/types/communities/member_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/bands/group_member_list.py">GroupMemberList</a></code>
- <code title="delete /communities/{communityId}/members/{userId}">client.communities.members.<a href="./src/bandlab_sdk/resources/communities/members.py">delete</a>(user_id, \*, community_id) -> None</code>

## Posts

Methods:

- <code title="post /community/{communityId}/posts">client.communities.posts.<a href="./src/bandlab_sdk/resources/communities/posts.py">create</a>(community_id, \*\*<a href="src/bandlab_sdk/types/communities/post_create_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/collections/post.py">Post</a></code>
- <code title="get /community/{communityId}/posts">client.communities.posts.<a href="./src/bandlab_sdk/resources/communities/posts.py">list</a>(community_id, \*\*<a href="src/bandlab_sdk/types/communities/post_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/post_list.py">PostList</a></code>

## Invites

Methods:

- <code title="get /community/{communityId}/invites">client.communities.invites.<a href="./src/bandlab_sdk/resources/communities/invites.py">list</a>(community_id, \*\*<a href="src/bandlab_sdk/types/communities/invite_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/users/invite_list.py">InviteList</a></code>
- <code title="post /community/{communityId}/invites">client.communities.invites.<a href="./src/bandlab_sdk/resources/communities/invites.py">send</a>(community_id, \*\*<a href="src/bandlab_sdk/types/communities/invite_send_params.py">params</a>) -> None</code>

# Songs

Types:

```python
from bandlab_sdk.types import Author, Song, SongCounters, SongOriginal
```

Methods:

- <code title="get /songs/{songId}">client.songs.<a href="./src/bandlab_sdk/resources/songs/songs.py">retrieve</a>(song_id) -> <a href="./src/bandlab_sdk/types/song.py">Song</a></code>
- <code title="patch /songs/{songId}">client.songs.<a href="./src/bandlab_sdk/resources/songs/songs.py">update</a>(song_id, \*\*<a href="src/bandlab_sdk/types/song_update_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/song.py">Song</a></code>
- <code title="delete /songs/{songId}">client.songs.<a href="./src/bandlab_sdk/resources/songs/songs.py">delete</a>(song_id) -> None</code>
- <code title="get /song/{songId}/posts">client.songs.<a href="./src/bandlab_sdk/resources/songs/songs.py">list_posts</a>(song_id, \*\*<a href="src/bandlab_sdk/types/song_list_posts_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/post_list.py">PostList</a></code>

## Collaborators

Types:

```python
from bandlab_sdk.types.songs import CollaboratorListResponse
```

Methods:

- <code title="get /songs/{songId}/collaborators">client.songs.collaborators.<a href="./src/bandlab_sdk/resources/songs/collaborators.py">list</a>(song_id, \*\*<a href="src/bandlab_sdk/types/songs/collaborator_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/songs/collaborator_list_response.py">CollaboratorListResponse</a></code>
- <code title="delete /songs/{songId}/collaborators/{userId}">client.songs.collaborators.<a href="./src/bandlab_sdk/resources/songs/collaborators.py">remove</a>(user_id, \*, song_id) -> None</code>

## Revisions

Types:

```python
from bandlab_sdk.types.songs import RevisionListResponse
```

Methods:

- <code title="get /songs/{songId}/revisions">client.songs.revisions.<a href="./src/bandlab_sdk/resources/songs/revisions.py">list</a>(song_id, \*\*<a href="src/bandlab_sdk/types/songs/revision_list_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/songs/revision_list_response.py">RevisionListResponse</a></code>
- <code title="post /songs/{songId}/revisions/{revisonId}/forks">client.songs.revisions.<a href="./src/bandlab_sdk/resources/songs/revisions.py">forks</a>(revison_id, \*, song_id, \*\*<a href="src/bandlab_sdk/types/songs/revision_forks_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/song.py">Song</a></code>

## Invites

Methods:

- <code title="get /song/{songId}/invites">client.songs.invites.<a href="./src/bandlab_sdk/resources/songs/invites.py">list_invites</a>(song_id, \*\*<a href="src/bandlab_sdk/types/songs/invite_list_invites_params.py">params</a>) -> <a href="./src/bandlab_sdk/types/users/invite_list.py">InviteList</a></code>
- <code title="post /song/{songId}/invites">client.songs.invites.<a href="./src/bandlab_sdk/resources/songs/invites.py">send_invites</a>(song_id, \*\*<a href="src/bandlab_sdk/types/songs/invite_send_invites_params.py">params</a>) -> None</code>
