import pytest
from utils.client import PostsClient
from validators.schema_validator import validate_schema

"""
Validate GET /posts returns a non-empty list of posts
"""
def test_get_all_posts_status_code(api_session):
    client = PostsClient(api_session)
    response = client.get_posts()
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0

@pytest.mark.parametrize("post_id", [10, 11, 12])
def test_get_single_post_content(api_session, post_id):
    client = PostsClient(api_session)
    response = client.get_post_by_id(post_id)
    assert response.status_code == 200

def test_get_posts_contract(api_session):
    client = PostsClient(api_session)
    response = client.get_posts()
    posts = response.json()

    validate_schema(posts[0], "schema\schema_posts.json")