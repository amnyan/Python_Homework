# Write a recursive function to reverse a given string.

def reverse(str):
    if len(str) < 1:
        return str
    
    return str[-1] + reverse(str[:-1])

text = "Arman"
print(reverse(text))