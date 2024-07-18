# Write a recursive function to print each character of a string on a new line.

def each_char(str):
    if not str:
        return 
    
    print(str[0])
    each_char(str[1:])

each_char("Arman")