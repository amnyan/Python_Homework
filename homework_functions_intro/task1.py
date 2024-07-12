def print_n_zero(count):
  for i in range(count, -1, -1):
    print(i,end=', ')


number = input("Please enter the Number : ")
if number.isdigit():
  number = int(number)
  print_n_zero(number)
else:
  print(f"{number} is invalid number!!!")
