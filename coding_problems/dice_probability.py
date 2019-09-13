# probablitiy of rolling a die over the sum of k when rolled three times. 

def dice_roll_over(k):
    count_total = 0 
    count_over_k = 0
    for roll1 in range(1,k):
        for roll2 in range(1,k):
            for roll3 in range(1,k):
                count_total += 1
                if roll1 + roll2 + roll3 > k:
                    count_over_k += 1
    return count_over_k/count_total

print(dice_roll_over(7))
