***
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
***
# Read the inputs
a = int(input())  # Seating capacity of L1
b = int(input())  # Seating capacity of L2
c = int(input())  # Seating capacity of L3
allocated_lab = input().strip()  # Lab allocated for ACE training

# Determine the minimum seating capacity lab amongst available labs
if allocated_lab == 'L1':
    # L1 is allocated, compare L2 and L3
    if b < c:
        print("L2 program")
    else:
        print("L3 program")
elif allocated_lab == 'L2':
    # L2 is allocated, compare L1 and L3
    if a < c:
        print("L1 program")
    else:
        print("L3 program")
elif allocated_lab == 'L3':
    # L3 is allocated, compare L1 and L2
    if a < b:
        print("L1 program")
    else:
        print("L2 program")
else:
    print("Invalid lab input")
