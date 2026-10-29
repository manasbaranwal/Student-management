class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

if __name__ == "__main__":
    s1 = Student("Alex", 101)
    s1.display()