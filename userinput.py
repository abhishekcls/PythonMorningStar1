#name=input("Enter your name: ")
'''
print("Your name is "+name)
print("Your name is",name)


age=input("Enter age: ")
qual=input("Qual: ")
print(f"Your name is {name}\nage {age}\nqual {qual}")
'''
#Task1 -> Take Name, Age, Qual from user and display with formatted output
#Task2 -> Take 3 subject marks(out of 100) from user and display total and average
m1=float(input("Enter sub1 marks: "))
print(m1,type(m1))
m2=float(input("Enter sub2 marks: "))
print(m2,type(m2))
m3=float(input("Enter sub3 marks: "))
print(m3,type(m3))
total=m1+m2+m3
avg=total/3
#print(f"Total marks: {total}\tAverage: {avg}")
print(f"Total marks: {total}\nAverage: {avg}")