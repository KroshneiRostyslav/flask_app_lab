import unittest

from app import create_app, db
from app.posts.models import Post


class PostTestCase(unittest.TestCase):

    def setUp(self):

        self.app = create_app("testing")

        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            post = Post(
                title="Existing post",
                content="Existing content",
                category="news"
            )

            db.session.add(post)
            db.session.commit()

    def tearDown(self):

        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    # CREATE
    def test_create_post(self):

        response = self.client.post(
            "/posts/post/create",
            data={
                "title": "Test title",
                "content": "Test content",
                "category": "tech"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)

    # ALL POSTS
    def test_all_posts(self):

        response = self.client.get("/posts/post")

        self.assertEqual(response.status_code, 200)

    # DETAIL POST
    def test_detail_post(self):

        response = self.client.get("/posts/post/1")

        self.assertEqual(response.status_code, 200)

    # DELETE POST
    def test_delete_post(self):

        response = self.client.post(
            "/posts/post/1/delete",
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)

        with self.app.app_context():

            post = db.session.get(Post, 1)

            self.assertIsNone(post)