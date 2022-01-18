class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage:
    def save_to_database(self, person, save_to):
        if save_to == 'db':
            print(f'Save the {person} to database')
        elif save_to == 'json':
            print(f'Save the {person} to a JSON file')
        else
            print(f'invalid  storage type')

    
person = Person('Tarek Haydar')
storage = PersonStorage()
storage.save_to_database(person, 'db')

#ABC => Abstract base class
class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass
    
class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')
        
storage = PersonXML()
storage.save(person)


