# # class Student:
# #     def info(self):
# #         pass
# # student_details = Student()
# # Currently not abstract
# # student_details.info()
#
# ##This is abstract
# from abc import ABC, abstractmethod
# class Student(ABC):
#     @abstractmethod
#     def info(self):
#         pass
#
# # Currently not abstract
# student_details.info()
#
# ##part 2
# class Adults(Student): # needs to be define other this will be abstract
#     def info(self):
#         print("hi spartan")
#
# # stu = Student()
# human = Adults() # Can't instantiate abstract class Student with abstract methods info
# # stu.info()



# Parent class

# class Student:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     # when a method has a body, it is a normal method
#     def full_name(self):
#         print(self.first_name, self.last_name)
#     # a method with no body is called declared meaning the definition is blank
#     # these are known as abstract methods
#     def age(self):
#         pass
    # a with class with an abstract method is also an abstract class
from abc import ABC, abstractmethod
# The super class, Student is the class that other classes inherits from
class Student:
    # method (behaviour) initialises the variables
    def __init__(self, name, age, course): # (name, age, course attributes are defined)
        self.name = name
        self.__age = age
        self.course = course

    # Details of the student
    def details(self):
        # basic print functions
        print("Name: " + self.name)
        print("Age: " + self.__age)
        print("University course: " + self.course)

    def graduate(self):
        print("I graduated from university recently")
    # @abstract methods allows us to declare an method with no body in the parent class, keeping it hidden
    @abstractmethod
    def power(self):
         pass
