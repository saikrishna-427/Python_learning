#function that takes a list of numbers and returns the cumulative sum

def cum(lst):
  sum_of_numbers = 0
  cum_list = list()
  for i in lst:
    sum_of_numbers += i
    cum_list.append(sum_of_numbers)
  return cum_list

cum([1,2,3])
