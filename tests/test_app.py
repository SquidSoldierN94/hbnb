import unittest
from app import create_app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_users(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        response = self.client.post('/api/users', json={'name': 'John Doe', 'email': 'john@example.com'})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
