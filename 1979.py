# =================== Find Greatest Common Divisor of Array




# Given an array nums, find:

# Smallest number
# Largest number
# Return their GCD (Greatest Common Divisor)




# --- Solution 1 :- Using math.gcd and min/max functions


import math

def findGCD(nums):
    return math.gcd(min(nums), max(nums))

nums = [2, 5, 6, 9, 10]
print(findGCD(nums)) 


