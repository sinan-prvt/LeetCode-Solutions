# =================== Fizz Buzz


# Given a number n, generate a list from 1 to n where:

# If number divisible by 3 & 5 → "FizzBuzz"
# If divisible by 3 → "Fizz"
# If divisible by 5 → "Buzz"
# Otherwise → number as string




# --- Solution 1 :-

def fizzbuzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

n = 15
print(fizzbuzz(n))