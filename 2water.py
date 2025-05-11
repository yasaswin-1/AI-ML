import math

def water_jug_problem(jug1, jug2, target):
    if target % math.gcd(jug1, jug2) != 0 or target > max(jug1, jug2):
        print("Target volume cannot be reached.")
        return
    j1, j2 = 0, 0
    while j1 != target and j2 != target:
        if j1 == 0:
            j1 = jug1
        elif j2 == jug2:
            j2 = 0
        else:
            pour = min(j1, jug2 - j2)
            j1, j2 = j1 - pour, j2 + pour
        print(f"({j1}, {j2})")
    
    if j1 == target:
        print(f"({j1}, {0})")
    else:
        print(f"({0}, {j2})")

jug1 = int(input("Enter the capacity of the first jug: "))
jug2 = int(input("Enter the capacity of the second jug: "))
target = int(input("Enter the target volume: "))
water_jug_problem(max(jug1, jug2), min(jug1, jug2), target)
