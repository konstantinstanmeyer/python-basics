# code from https://cdn.cs50.net/python/2022/x/lectures/8/src8/wizard.py

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

# student inherits the functionality from the wizard class
# abstracts the error handling and avoids the need for copy-pasting
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")