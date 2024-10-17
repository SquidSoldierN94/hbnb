from persistence.in_memory_repository import InMemoryRepository

class UserService:
    def __init__(self):
        self.repository = InMemoryRepository()
    
    def get_all_users(self):
        return self.repository.get_all()
    
    def add_user(self, user_data):
        return self.repository.add(user_data)
