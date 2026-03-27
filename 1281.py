# =================== Subtract the Product and Sum of Digits of an Integer



# Given an integer number n, return the difference between 
# the product of its digits and the sum of its digits.




# --- Solution 1 :-


def subtractProductAndSum(n):
    product = 1
    total = 0

    while n > 0:
        digit = n % 10
        product *= digit
        total += digit
        n //= 10
    
    return product - total

n = 234
print(subtractProductAndSum(n))