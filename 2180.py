# =================== Count Integers With Even Digit Sum


# Given an integer num, count how many numbers from 1 to num have:
# digit sum = even
# Return the count.




# --- Solution 1 :- Iterative Approach


def countEven(num):
    count = 0

    for i in range(1, num + 1):
        digit_sum = 0
        num = i

        while num > 0:
            digit_sum = num % 10
            num //= 10

        if digit_sum % 2 == 0:
            count += 1
    return count

num = 30
print(countEven(num))