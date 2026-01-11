class PostsClient:
    def __init__(self, session):
        self.session = session
    
    def get_all_posts(self):
        return self.session.get(f"{self.session.base_url}/posts")

    # alias kept for backwards-compatibility with tests expecting get_posts()
    def get_posts(self):
        return self.get_all_posts()
    
    def get_post_by_id(self, post_id):
        return self.session.get(f"{self.session.base_url}/posts/{post_id}")
    
