def first_upper(string):
  for i in string:
    if i.isupper():
      return i
  return -1

string = 'this is'
#string = "this is a Man's worlD!!"
check = first_upper(string)
if (check != -1):
  print(f"First Upper is {check}")
else:
  print("The string hasn't upper or invalis!!!")
