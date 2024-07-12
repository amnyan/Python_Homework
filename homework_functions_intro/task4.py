def count_of_digit(number):
  sum = 0
  while(number):
    sum += number % 10
    number //= 10
  return sum

number = input("Please enter the Number : ")
if number[0] in  ['-','+']:
      number = number[1:]
if number.isdigit():
   print(f"The count of digits of {number} is {count_of_digit(int(number))}")
else:
  print(f'{number} is invalid integer!!!')
