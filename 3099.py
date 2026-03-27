# =================== Harshad Number



# Given an integer x:

# Find digit sum
# If x is divisible by its digit sum → return digit sum
# Otherwise → return -1




# --- Solution 1 :- Iterative Approach


def harshadNumber(x):
    digit_sum = 0
    num = x

    while num > 0:
        digit_sum += num % 10
        num //= 10
    
    if x % digit_sum == 0:
        return digit_sum
    else:
        return -1
    
x = 18
print(harshadNumber(x))


