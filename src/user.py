import topic 
import note
class User:
    def __init__(self, name):
        self.name = name
        self.id = 1
        self.collectionId = 1

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_collection_id(self):
        return self.collectionId
    
    def upload(self, topic, file):
        with open(file, 'rb') as file:
            binaryFile = file.read()
        #create new note object
        #add to users collection
        #add to topic collection