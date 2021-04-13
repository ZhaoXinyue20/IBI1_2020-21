class Student:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.progamme = None

    # get student information
    def student_information(self,first_name,last_name,programme):
        self.first_name = first_name
        self.last_name = last_name
        if programme in ["BMI","BMS"]:
            self.programme = programme
        else:
            print("You are not BMI or BMS student.")

    # show info in a single line       
    def show_information(self):
            print("Student's name is " + self.first_name + " " +
              self.last_name + ", undergraduate programme is " + self.programme)

# test
test = Student()
test.student_information("Zoe","Zhao","BMS")
test.show_information()
