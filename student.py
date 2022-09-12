# Object Oriented Programming
# 3rd Approach
class Student(): # By Convention the 1st letter of the name of the class is in uppercase.
    # Method: A method is just a function inside of a class.
     # Dunder Init method: The __init__ method is meant to initialize specific objects from a class (blueprint/template).This is what lets us create multiple objects(instances) of our class.
    def __init__(self, name, house):
        # This are instance variables(Arguments). Self here refers to specific objects, it helps to create instance variables for all the objects(instances) that we create using this class.
        self.name = name    
        self.house = house
    
    def __str__(self):              
        return f"{self.name} from {self.house}"

    # These are instance methods. As this methods have a scope over all the objects of this particular class.
    @property        
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    
    #Decorators: Functions that modify the behaviour of other functions. 
    @property       # Getter: A getter is an instance method. A getter is a method for some class that gets some value. Using a getter and setter enables python to automatically detect when we are trying to manually set a value.
    def house(self):
        return self._house
    
    @house.setter   # Setter: A setter is a function in some class that sets some value.
    def house(self, house):
        if house not in ['Gryffindor','Hufflepuff','Ravenclaw','Slytherin']:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    # student.house = 'Kolkata'
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) # Constructo call: This is the line of code that is going to instantiate a student object using the student class that holds the blueprint of creating student objects.


if __name__ == '__main__':
    main()