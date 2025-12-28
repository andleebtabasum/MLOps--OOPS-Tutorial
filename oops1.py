class Employee:
    def __init__(self):
        self.id=123
        self.designation="software engineer"
        self.salary=50000

    def travel(self,destination):
        print("sam is travelling to",destination)
sam=Employee()
print("The employee Id of Sam is: ",sam.id)
print("The designation of Sam is :",sam.designation)
print(f"Sam gets a salary of {sam.salary}INR")

sam.travel("New York")