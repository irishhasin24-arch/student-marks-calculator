print("STUDENT MARKS CALCULATOR")

name = input("enter student name:")

maths=float(input("enter maths marks:")
statistics=float(input("enter statistics marks:")
economics=float(input("enter economics marks:")
physics=float(input("enter physics marks:")
chemistry=float(input("enter chemistry marks:")

total = maths + statistics + economics + physics + chemistry 
percentage = total/5
print("\nStudent Name:", name)
print("total marks:",total, "/500")
print("percentage:"< percentage, "%")

if percentage >= 90:
   print("Grade:A+")
elif percentage >= 80:
  print("Grade:A")
elif percantage >= 70:
  print("Grade:B")
elif percentage >= 60:
  print("Grade:C")
elif percantage >= 40:
  print("Grade:D")
else:
  print("Grade:F")
  
