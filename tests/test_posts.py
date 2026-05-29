import unittest

from app import create_app, db
from app.posts.models import Post

class PostTestCase(unittest.TestCase):

    def setUp(self):

        self.app = create_app("testing")

        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):

        with self.app.app_context():
            db.drop_all()

    def test_create_post(self):

        response = self.client.post(
            "/post/create",
            data={
                "title": "Test",
                "content": "Test content",
                "category": "news"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)

    def test_all_posts(self):

        response = self.client.get("/post")

        self.assertEqual(response.status_code, 200)