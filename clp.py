from itertools import product
import math

def find_combination(T, k):
    for combo in product(range(1, 10), repeat=k):  # Avoid 0 since it nullifies the product
        prod = math.prod(combo)
        if prod == T:
            return combo
    return None

# Input from user
T = int(input("Enter the target product T: "))
k = int(input("Enter the number of digits k: "))

result = find_combination(T, k)
if result:
    print("Output:", *result)
else:
    print("No combination found.")
