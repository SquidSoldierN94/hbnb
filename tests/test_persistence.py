import unittest
from persistence.in_memory_repository import InMemoryRepository

class TestInMemoryRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryRepository()

    def test_add_and_get_all(self):
        self.repo.add({'name': 'John Doe', 'email': 'john@example.com'})
        users = self.repo.get_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['name'], 'John Doe')

if __name__ == '__main__':
    unittest.main()
