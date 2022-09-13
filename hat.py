import random

class Hat:  # We are going to encapsulate(tuck away) this functionality in our class.
    houses = ['Gryffindor','Hufflepuff','Ravenclaw','Slytherin'] # This is a variable within a class hence it is called a class variable. We don't need self as we are not going to instantiate any other object using this class. As a result we don't need any instance variable to create variables for every object that we create using this class. A simple class variable is going to do, as we will not will use this class as a singleton.  


    # Classmethod: A decorator that we can use to specify that this method, is not by default implicitly an instance method that has access to self(the objects). A classmethod does not have access to self, but it does have access to the class that it belongs to. 
    @classmethod        # This function is only required to run for this specific class and we are not doing to create any other instance of this very class. As a result this function isn't require to run for various differnt objects. 
    def sort(cls, name):
        print(name, "is in",random.choice(cls.houses)) # House is now a class variable accessible by a cls.houses


# hat = Hat()                # Instantiating an Object of the class Hat that we just created. After we introduced class variable and class method in the class hat we no more need to instantiate it. 

Hat.sort("Harry")            # Accessing a class method inside of the class hat. This is how we refer to a class method. We class the class and access the class method. 