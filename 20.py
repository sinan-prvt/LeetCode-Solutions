# =================== Valid Parentheses


# Given a string s containing only brackets () [] {},
# check if the brackets are valid (balanced and correctly ordered).



# --- Solution 1 :- Using Stack and Hash Map with closing and opening brackets


# def isValid(s):
#     stack = []
#     mapping = {
#         ')' : '(',
#         ']' : '[',
#         '}' : '{'
#     }

#     for char in s:
#         if char in mapping:
#             if not stack or stack[-1] != mapping[char]:
#                 return False
#             stack.pop()
#         else:
#             stack.append(char)
        
#     return len(stack) == 0

# # s = "({[]})"
# s = "({[})"
# print(isValid(s))






# --- Solution 2 :- Using Stack and Hash Map with opening and closing brackets (It is Best Solution)

def isValid(s):
    stack = []
    mapping = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }

    for char in s:
        if char in mapping:
            stack.append(mapping[char])
        else:
            if not stack or stack.pop() != char:
                return False 
            
    return not stack

# s = "({[]})"
s = "({[})"   
print(isValid(s))
