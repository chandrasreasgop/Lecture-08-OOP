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

    @classmethod # This is a classmethod. We don't need to create an instance of this class to be able to use this method.
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    # Total Encapsulation can be seen here. As all the code that is reated to creating a student object and performing functions on it is encoded in the Student class.


def main():
    student = Student.get()
    print(student)


if __name__ == '__main__':
    main()