# =================== Average Value of Even Numbers That Are Divisible by Three


# Given an array nums, find the average (rounded down) of numbers that are:
# even
# divisible by 3

# If none exist → return 0.



# --- Solution 1 :- Iterate and Calculate Average


def averageValue(nums):
    total = 0
    count = 0

    for num in nums:
        if num % 6 == 0:
            total += num
            count += 1
    return total // count if count else 0

nums = [1, 3, 6, 10, 12, 15]
print(averageValue(nums))