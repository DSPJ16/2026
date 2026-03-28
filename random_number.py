import random

print("=== Random Number Generator ===")

low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))

result = random.randint(low, high)

print(f"Your random number is: {result}")
