print("welcome to the interactive data collector")

name=input("enter your name: ")
age=int(input("enter your age: "))
height=float(input("enter your height : "))
favnumber=int(input("enter your fav number: "))

print("\n Thank you!for your information :\n")

print(f"name:{name}(type:{type(name)},"
      f"\nmemory address:{id(name)})\n")

print(f"age:{age}(type:{type(age)},"
      f"\nmemory address:{id(age)})\n")

print(f"height:{height}(type:{type(height)},"
      f"\nmemory address:{id(height)})\n")

print(f"favourite number:{favnumber}(type:{type(favnumber)},"
      f"\nmemory address:{id(favnumber)})\n")

print("\n__birth year calculation__:\n")
import datetime
current_year=datetime.datetime.now().year
birth_year=current_year-age

print(f"\nYour birth year is approximately{birth_year}(based on your age of {age}).\n")

print("thank you! \n")                   




