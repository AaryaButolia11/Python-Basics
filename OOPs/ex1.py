class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def getAvgs(self):
        sum=0
        for i in range(0,3):
            sum=sum+self.marks[i]
        avg = sum /len(self.marks)
        print(f"hi {self.name} your avg score is: {avg}")
        



s1 = Student("Aarya Butolia",[98,99,97])
s1.getAvgs()

# to change name
s1.name="Aarya Sanyog Butolia"
s1.getAvgs()
