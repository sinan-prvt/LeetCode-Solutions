# =================== Two Sum


# Given an array nums and an integer target,
# return the indices of two numbers




# --- Solution 1 :


# def twosum(nums, target):
#     seen = {}

#     for i, num in enumerate(nums):
#         complement = target - num

#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i
    
    
# nums = [2, 7, 11, 15]
# target = 9

# print(twosum(nums, target))





# --- Solution 2 :


def twosum(arr, target):
    arr_with_index = list(enumerate(arr))
    arr_with_index.sort(key=lambda x: x[1])

    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr_with_index[left][1] + arr_with_index[right][1]

        if current_sum == target:
            return [arr_with_index[left][0], arr_with_index[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
        
    return None

nums = [2, 7, 11, 15]
target = 9

print(twosum(nums, target))
