class InMemoryRepository:
    def __init__(self):
        self.storage = []
        self.id_counter = 1
    
    def get_all(self):
        return self.storage
    
    def add(self, data):
        data['id'] = self.id_counter
        self.id_counter += 1
        self.storage.append(data)
        return data
