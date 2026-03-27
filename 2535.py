# =================== Difference Between Element Sum and Digit Sum of an Array



# Given an array nums:
# Element sum → sum of all numbers
# Digit sum → sum of all digits of all numbers

# Return absolute difference → |element_sum - digit_sum|




# --- Solution 1 :- Iterative Approach


def differenceOfSum(nums):
    element_sum = sum(nums)
    digit_sum = 0

    for num in nums:
        while num > 0:
            digit_sum += num % 10
            num //= 10
    
    return abs(element_sum - digit_sum)

nums = [1, 15, 6, 3]
print(differenceOfSum(nums))