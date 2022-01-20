
user_age: int = int(input("How old are you? "))
year: int = int(input("What year is it? "))
age_in_2041: int = (2041-year)+user_age

print("In 2041, you'll be " + str(age_in_2041))

user_age = user_age +1
year = year+1
print("In "+str(year)+", you'll be "+str(user_age))