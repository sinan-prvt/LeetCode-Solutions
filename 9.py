# =================== Palindrome Number


# Given an integer x, return true if x is a palindrome, and false otherwise.



# --- Solution 1 :- String Conversion and Reversal (Time is O(n) and Space is O(n))


# def isPalindrome(x):
#     return str(x) == str(x)[::-1]

# x = 121
# print(isPalindrome(x))




# --- Solution 2 :- Mathematical Reversal of Half the Number (Time is O(log10(n)) and Space is O(1))


def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    rev = 0

    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10

    return x == rev or x == rev // 10

x = -121
print(isPalindrome(x))