# # # imports class
# # from student_data import Student
# #
# # # inherits first_name, last_name attributes
# class Devops(Student):
#     def __init__(self, id,first_name, last_name,skills,age):
#         super().__init__(first_name, last_name, age)
#         self.skills = skills
#         self.id = id
#
#
#     def spartan_summary(self):
#         print("ID:",self.id, "\nName:",self.first_name,"\nSurname:",self.last_name,"\nSkills:", self.skills )
#     def spartan_skills(self):
#         print("Skills:", self.skills)
# #
# student_one = Devops("1241","Marcus","Tse", "SQL")
# # student_one.full_name() # method is hidden to the user




#
#
# student_one.spartan_skills()
# student_one.spartan_summary()

# Imports everything (*) from student_data
from student_data import *

# The subclass devops has student as its base class
class Devops(Student): # The class inherits all the characteristics from student_data
    def __init__(self, name, age, course, skills):
        super().__init__(name, age, course)
        self.skills = skills # unique to devops only

    # Here in the student class there is a different fuctionality
    def power(self):
        print("remember to use power words to sell yourself")


#Recalls the instance of the class

# instance of method has been named from Devops
b =  Devops("bob", "25", "Computer Science", "SQL, Python and AWS\n")
# instance of Student
a = Student("bob", "25", "Computer Science")

#Both produce different outputs because the behaviour in the parent class and child class differs
a.power()
# a.graduate()
print("___")
b.power()
# b.graduate()
