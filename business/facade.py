from business.services.user_service import UserService

class Facade:
    def __init__(self):
        self.user_service = UserService()
    
    def get_all_users(self):
        return self.user_service.get_all_users()
    
    def add_user(self, user_data):
        return self.user_service.add_user(user_data)
