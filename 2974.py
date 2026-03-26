# =================== Minimum Number Game




# Given an even-length array nums:

# Each round:
# Alice removes smallest
# Bob removes next smallest
# Bob adds to arr, then Alice adds

# Repeat until empty → return arr

# Sort the array
# Take numbers in pairs:
# swap each pair
# Return the new array



# --- Solution 1 :- Sorting and Swapping Pairs


def minNumber(nums):
    nums.sort()

    for i in range(0, len(nums), 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

nums = [3, 1, 4, 2]
print(minNumber(nums))


