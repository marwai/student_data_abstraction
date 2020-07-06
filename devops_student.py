# imports class
from student_data import Student

# inherits first_name, last_name attributes
class Devops(Student):
    def __init__(self, id,first_name, last_name,skills, ):
        super().__init__(first_name, last_name)
        self.skills = skills
        self.id = id

    0
    def spartan_summary(self):
        print("ID:",self.id, "\nName:",self.first_name,"\nSurname:",self.last_name,"\nSkills:", self.skills )
    def spartan_skills(self):
        print("Skills:", self.skills)

student_one = Devops("1241","Marcus","Tse", "SQL")
# student_one.full_name()
# student_one.spartan_skills()
student_one.spartan_summary()
