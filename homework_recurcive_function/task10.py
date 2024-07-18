# Write a recursive function to check if a given string is a palindrome.

def palindrom(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    
    return palindrom(str[1:-1])
    
    
print(palindrom("ArmrA"))
    
    
