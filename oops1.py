
#create a class
class Employee:
    # define attributes 
    def __init__(self):
        self.id=123
        self.designation="software engineer"
        self.salary=50000
# define method
    def travel(self,destination):
        print("sam is travelling to",destination)


        
# create an object
emp=Employee()

# create an attribute outside of the constructor


emp.name="Sam Altman"
print("The employee Id of Sam is: ",emp.id)
print("The designation of Sam is :",emp.designation)
print(f"Sam gets a salary of {emp.salary}INR")
print("The name of the employee is :",emp.name)

# Manually calling the methods of the class
emp.travel("New York")