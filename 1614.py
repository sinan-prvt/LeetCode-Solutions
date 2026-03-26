# =================== Maximum Nesting Depth of the Parentheses


# Given a valid parentheses string s, find the maximum nesting depth.

# "(" → increase depth
# ")" → decrease depth
# Track the maximum depth reached




# --- Solution 1 :- Simple Iteration and Depth Tracking


def maxDepth(s):
    depth = 0
    max_depth = 0

    for ch in s:
        if ch == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == ')':
            depth -= 1
    return max_depth

s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))

