# =================== Find All Duplicates in an Array



# Given array nums of size n:

# Values are in range [1, n]
# Each number appears once or twice

# Return all numbers that appear twice




# --- Solution 1 :-


def findDuplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num in seen:
            result.append(num)
        else:
            seen.add(num)
    return result

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(nums))