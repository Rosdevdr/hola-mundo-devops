import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_hello_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_hello_content(self):
        response = self.client.get("/")
        self.assertIn(b"Hola Mundo", response.data)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()