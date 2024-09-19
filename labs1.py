***
There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
***
# Read the inputs
x = int(input())  # Seating capacity of L1
y = int(input())  # Seating capacity of L2
z = int(input())  # Seating capacity of L3
n = int(input())  # Number of students

# Determine the suitable lab
suitable_lab = None
if x >= n:
    suitable_lab = ("L1", x)
if y >= n:
    if suitable_lab is None or y > suitable_lab[1]:
        suitable_lab = ("L2", y)
if z >= n:
    if suitable_lab is None or z > suitable_lab[1]:
        suitable_lab = ("L3", z)

# Output the result
if suitable_lab:
    print(suitable_lab[0], "program")
else:
    print("No suitable lab")  # In case no lab can accommodate the students
