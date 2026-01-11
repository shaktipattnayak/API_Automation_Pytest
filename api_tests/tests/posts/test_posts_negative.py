import pytest
from utils.client import PostsClient

@pytest.mark.parametrize("invalid_input", [1000, 8888, 3333])
def test_get_post_with_invalid_id(api_session, invalid_input):
    """
    Validate API behavior for invalid post IDs
    """
    client = PostsClient(api_session)
    response = client.get_post_by_id(invalid_input)
    assert response.status_code in [400, 404]