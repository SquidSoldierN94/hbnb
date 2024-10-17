import unittest
from business.facade import Facade

class TestFacade(unittest.TestCase):
    def setUp(self):
        self.facade = Facade()

    def test_get_all_users(self):
        users = self.facade.get_all_users()
        self.assertIsInstance(users, list)

    def test_add_user(self):
        user = self.facade.add_user({'name': 'John Doe', 'email': 'john@example.com'})
        self.assertIn('id', user)
        self.assertEqual(user['name'], 'John Doe')

if __name__ == '__main__':
    unittest.main()
