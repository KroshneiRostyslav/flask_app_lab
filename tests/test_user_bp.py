import unittest 
from app import app 

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
    
    def test_greeting_page(self):
        response = self.client.get("hi/Jonh?age=30")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"JONH", response.data)
        self.assertIn(b"30", response.data)

    def test_admin_page(self):
        response = self.client.get("/admin", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"ADMINISTRATOR", response.data)
        self.assertIn(b"45", response.data)

    def test_products_page(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()