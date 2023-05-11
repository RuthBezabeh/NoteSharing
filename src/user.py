import topic 
import note
class User:
    def __init__(self, name):
        self.name = name
        self.id = 001
        self.collectionId = 001
    def upload(self, topic, file):
        with open(file, 'rb') as file:
            binaryFile = file.read()
        #create new note object
        #add to users collection
        #add to topic collection