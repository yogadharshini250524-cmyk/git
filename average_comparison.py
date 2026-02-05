# Program to count how many numbers are above average

# Get space-separated numbers from user
input_string = input("Enter numbers (space-separated): ")
numbers = list(map(int, input_string.split()))

# Calculate average using loop
total = 0
for num in numbers:
    total = total + num

average = total / len(numbers)

# Count how many numbers are above average
count = 0
for num in numbers:
    if num > average:
        count = count + 1

# Display result
print(f"\nAverage: {average:.2f}")
print(f"Numbers above average: {count}")
