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
# Function to check if the character is a vowel, consonant, or not an alphabet
def check_character(char):
    if char.isalpha():
        if char.lower() in 'aeiou':
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Not an alphabet"

# Input: A single character from the user
char = input()

# Output: Vowel, Consonant, or Not an alphabet
result = check_character(char)
print(result)
