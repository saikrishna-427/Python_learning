import random

#function for Random birthdays /did not considered year

def ramdom_bday(n):
  std_bmonth = 1
  std_bday = 1
  birthday = list()
  for i in range(n):
    t = (random.randint(std_bmonth, 12),random.randint(std_bday, 30))
    birthday.append(t)
  
  return birthday

# Function for probability
def probability1():
  prob = 1
  for key in lst:
    value_dup = lst[key]
    prob = prob * (value_dup/no_of_students)
  return prob


no_of_students = 23
students_bday = ramdom_bday(no_of_students)
lst = has_duplicates(students_bday)
print(lst)
probability1()
