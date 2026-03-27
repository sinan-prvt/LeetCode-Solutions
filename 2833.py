# ===================  Furthest Point From Origin




# Given a string moves with:

# 'L' → move left
# 'R' → move right
# '_' → can choose left or right

# Start at 0.
# Return the maximum distance from origin you can reach after all moves.





# --- Solution 1 :- Counting Left, Right and Blank Moves


def furthestDistanceFromOrigin(moves):
    left = moves.count('L')
    right = moves.count('R')
    blank = moves.count('_')

    return abs(right - left) + blank

moves = "L_RL__R"
print(furthestDistanceFromOrigin(moves))
