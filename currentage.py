***
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
***
# Function to calculate the age
def calculate_age(birth_year, current_year):
    if current_year >= birth_year:
        age = current_year - birth_year
    else:
        age = (100 - birth_year) + current_year
    return age

# Input: Two integers representing the last two digits of the birth year and current year
birth_year = int(input())
current_year = int(input())

# Output: User's current age
age = calculate_age(birth_year, current_year)
print(age)
