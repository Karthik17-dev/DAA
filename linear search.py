# List of numbers
numbers = [10, 20, 30, 40, 50]

# Number to find
search = 30

# Check each number one by one
found = False
for num in numbers:
    if num == search:
        found = True
        break

# Print result
if found:
    print("Number found!")
else:
    print("Number not found!")
