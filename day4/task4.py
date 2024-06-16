def count(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonant_count = 0
    vowel_count = 0
    
    for char in input_string:
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
        
    return vowel_count, consonant_count

input_string = input("Please Enter sentense  ")
vowel_count,consonant_count = count(input_string)
print(f"vowel_count : {vowel_count} \nconsonant_count : {consonant_count}")