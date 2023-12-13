class Student:
    def __init__(self,name,id,grade):
        self.__student_id = id
        self.__name = name
        self.__grade = grade
    
    def getStudentID(self):
        return self.__student_id
    
    def setStudentID(self,id):
        self.__student_id = id

    def getGrade(self):
        return self.__grade
    
    def setGrade(self,grade):
        self.__grade = grade


AyeAye = Student(5)
print(AyeAye.getStudentID()) # student_id 

