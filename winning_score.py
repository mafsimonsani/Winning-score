# CCC '19 J1 - Winning Score
apple_three_point = int(input())
apple_two_point = int(input())
apple_one_point = int(input())

banana_three_point = int(input())
banana_two_point = int(input())
banana_one_point = int(input())

# Calculate total scored by each team.
apple_total_point = ((apple_three_point * 3) + (apple_two_point * 2) +
                      (apple_one_point))

banana_total_point = ((banana_three_point * 3) + (banana_two_point * 2) +
                        (banana_one_point))

# Determine which team won, or if the game ended in a tie.
if apple_total_point > banana_total_point:
    print('A')
elif banana_total_point > apple_total_point:
    print('B')
else:
    print('T')

