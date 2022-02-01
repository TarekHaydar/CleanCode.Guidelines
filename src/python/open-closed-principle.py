# Open for extensions, closed for modifications.

# Implementing a new way to save the person metadata requires 
# new modifications to the 'save' method inside the 'PersonStorage' class.
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage:
    def save(self, person, save_to):
        if save_to == 'db':
            print(f'Save the {person} to database')
            return

        if save_to == 'json':
            print(f'Save the {person} to a JSON file')
            return
            
        else:
            print(f'invalid  storage type')

    
person = Person('Tarek Haydar')
storage = PersonStorage()
storage.save(person, 'db')

# Resolve making new modification with Abstractions.
# ABC => Abstract base class
import ABC

class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass
    
class PersonStorageDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')


class PersonStorageJSON(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')
        
class PersonStorageXML(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a XML file')

storage = PersonStorageXML()
storage.save(person)


