***
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
***
def check_character(char):
    if char.isalpha():
        if char.lower() in 'aeiou':
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Not an alphabet"
char = input()
result = check_character(char)
print(result)
