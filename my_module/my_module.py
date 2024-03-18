# 1 for count no. of vowel
def count_vowel(s):
    vowels = "aeiouAEIOU"
    count=0
    for char in  s:
        if char in vowels:
            count+=1
    return count
        

#2  Duplicate vowels and their counts
import numpy as np

def count_duplicate_vowels(user_input):
    myArr = np.array(['a', 'e', 'i', 'o', 'u'])

     
    user_input = user_input.lower()

 
    vowel_counts = {vowel: 0 for vowel in myArr}

     
    for vowel in myArr:
        vowel_counts[vowel] = user_input.count(vowel)


    duplicate_vowels = {vowel: count for vowel, count in vowel_counts.items() if count > 1}

    return duplicate_vowels

 
