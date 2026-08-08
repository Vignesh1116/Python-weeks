# # 7) What will be the output?
# # ```
# # print("Enter a number:")
# # n=int(input())
# # print(n)
# # print(n+1)
# # print(n+2)
# # print(n+3)
# # ```



# class student:
#     Name=None
#     tamil=None
#     english=None
#     maths=None
#     science=None
#     social=None


#     def total(self):
#         print(self.Name+" your total is: ",self.tamil+self.english+self.maths+self.science+self.social)

# stud=student()
# stud.Name="santhosh"
# stud.tamil=90
# stud.english=98
# stud.maths=99
# stud.science=80
# stud.social=100


# stud2=student()
# stud2.Name="Vignesh"
# stud2.tamil=99
# stud2.english=99
# stud2.maths=100
# stud2.science=99
# stud2.social=100



# print(stud.Name)
# print(stud2.Name)

class parent:
    def __init__(self,networth):
        self.networth=networth
        print(networth)

class child(parent):
    def __init__(self,networth):
          super().__init__(networth)
          print("child",networth)
child1 = child(10000)
                