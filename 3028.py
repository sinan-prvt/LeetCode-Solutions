# =================== Ant on the Boundary


# Given an array of non-zero integers nums,
# an ant starts at position 0 (boundary).
# For each value:
#   - move right if positive
#   - move left if negative
# Count how many times the ant returns to position 0
# after completing each move.



# --- Solution 1 :- Using Simple Loop and Condition Check (It is Best Solution)


# def countAnts(nums):
#     position = 0 
#     count = 0

#     for move in nums:
#         position += move

#         if position == 0:
#             count += 1
    
#     return count

# nums = [1, -1, 2, -2, 3, -3]
# nums2 = [1, 2, -3, 3, -2, -1]

# print(countAnts(nums))
# print(countAnts(nums2))





# --- Solution 2 :- In Pythonic way 


def countAnts(nums):
    position = 0
    return sum((position := position + move) == 0 for move in nums)

nums = [1, -1, 2, -2, 3, -3]
nums2 = [1, 2, -3, 3, -2, -1]

print(countAnts(nums))
print(countAnts(nums2))


