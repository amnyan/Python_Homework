def max(ls):
  maximum = ls[0]
  for i in range(1,len(ls)):
    if ls[i] > maximum:
      maximum = ls[i]
  return maximum

def min(ls):
  minimum = ls[0]
  for i in range(1,len(ls)):
    if ls[i] < minimum:
      minimum = ls[i]
  return minimum


ls = [1,2,3,4,5,6]

print(f"Max of array is {max(ls)}")
print(f"Min of array is {min(ls)}")
