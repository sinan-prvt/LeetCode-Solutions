# =================== Longest Substring Without Repeating Characters



# Given a string s,
# return the length of the longest substring that contains no duplicate characters.




# --- Solution 1 :


# def lengstr(s):
#     char_set = set()
#     left = 0 
#     max_len = 0

#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)
#     return max_len

# s = "abcabcbb"
# print(lengstr(s))

# print(lengstr(["class","mud","class","class","mud","mud","class"]))




# --- Solution 2 :


def longstr(s):
    char_index = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len

s = "abcabcbb"
print(longstr(s))
print(longstr(["class","mud","class","class","mud","mud","class"]))