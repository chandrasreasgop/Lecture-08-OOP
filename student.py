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
        if not name:
            raise ValueError("Missing name")
        if house not in ['Gryffindor','Hufflepuff','Ravenclaw','Slytherin']:
            raise ValueError("Invalid house")
        self.name = name    # This are instance variables. (Argument)
        self.house = house
    
    def __str__(self):              
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) # Constructo call: This is the line of code that is going to instantiate a student object using the student class that holds the blueprint of creating student objects.


if __name__ == '__main__':
    main()