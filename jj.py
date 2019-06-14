class Student:
    def __init__(self,name="ok",stuID=0):
        self.name = name
        self.stuDI = stuID
        print("calling Student.__init__: name=%s" %name)
    def __del__(self):
        print("__del__ is being called: name=%s" %self.name)
    def talk(self):
        print("%s is talking" %self.name)
if __name__ == "__main__":
    s1 = Student("ling",13)
    s1.talk()
    Student.talk(s1)
    print('\nUsing "del s1" to delete s1')
    del s1
    print("\n======================")
    s2 = Student("dudu",2)
    s2.talk()
    Student.talk(s2)