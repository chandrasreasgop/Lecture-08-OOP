# 1st Approach
# def main():
#     name = input("Name: ")
#     house = input("House: ")
#     print(f"{name} from {house}")
#main()




# 2nd Approach
# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")


# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")


# if __name__ == '__main__':
#     main()



# Object Oriented Programming
# 3rd Approach
class Student(): # By Convention the 1st letter of the name of the class is in uppercase.
    def __init__(self, name, house): # Dunder Init method: A method is just a function inside of a class. 
        self.name = name    # This are instance variables. (Argument)
        self.house = house
    
    def __str__(self):              
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    # Decorators: Functions that modify the behaviour of other functions. 
    @property       # Getter: A getter is a function for some class that gets some value. Using a getter and setter enables python to automatically detect when we are trying to manually set a value.
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