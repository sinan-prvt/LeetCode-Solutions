# =================== Smallest Even Multiple


# Given a positive integer n, 
# return the smallest positive integer that is a multiple of both 2 and n.



# --- Solution 1 :- Simple Check for Even or Odd


# def smallestEvenMultiple(n):
#     if n % 2 == 0:
#         return n
#     else:
#         return n * 2

# n = 5
# print(smallestEvenMultiple(n))




# --- Solution 2 :- Using Ternary Operator (It is Best Solution)


def smallestEvenMultiple(n):
    return n if n % 2 == 0 else n * 2

n = 6 
print(smallestEvenMultiple(n))