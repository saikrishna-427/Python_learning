from functools import reduce
  

def nested_sum(l):
  total = 0
  for n in l:
    if type(n) == int:
      total = total + n
    else:
      type(n) == list
      total = nested_sum(n) + total
  return total  


l = [[3],2,3,[2,[4,5]],[3,5]]
print(nested_sum(l))
