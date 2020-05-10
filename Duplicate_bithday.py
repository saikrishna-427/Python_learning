#finding duplicate birthdays in lists of python
def has_duplicates(dates):
  word_checked = {}
  same_date = []
  for i in dates:
    if i not in word_checked:
      word_checked[i] = 1
    else:
      if word_checked[i] == 1:
        same_date.append(i)
        word_checked[i] = word_checked[i] + 1
  return word_checked

dates = [(2020, 5, 17),(2019, 5, 17),(2020, 5, 17)]
has_duplicates(dates)
    
