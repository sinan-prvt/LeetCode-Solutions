# =================== Defanging an IP Address




# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".




# --- Solution 1 :- Using String Replace Method


# def defangIPaddr(address):
#     return address.replace('.','[.]')

# address = "1.1.1.1"
# print(defangIPaddr(address))





# --- Solution 2 :- Using Iteration and List to Build the Result (It is Best Solution)


def defangIPaddr(address):
    result = []

    for ch in address:
        if ch == ".":
            result.append("[.]")
        else:
            result.append(ch)

    return "".join(result)

address = "255.100.50.0"
print(defangIPaddr(address))