# Given a sum of money compute the minimum number of bills and coins that equal that sum.
# Assume you only have the following denominations:
# Bills: 20, 10, 5, 1,
# Coins: .25, .1, .05, .01
# For example, given 6.35 the solution would be One 5, One 1, One .25, One .1
from decimal import *


def calculate_min_denominations(target_sum: Decimal):
    available_bills_and_coins = [20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
    twenty_occ = 0
    ten_occ = 0
    five_occ = 0
    one_occ = 0
    quarter_occ = 0
    dime_occ = 0
    nickel_occ = 0
    penny_occ = 0

    denominator_occurrences = dict()

    while target_sum > 0:
        if target_sum - available_bills_and_coins[0] > 0:
            target_sum = target_sum - available_bills_and_coins[0]
            twenty_occ += 1
            denominator_occurrences.update({"20": twenty_occ})
        elif target_sum - available_bills_and_coins[1] > 0:
            target_sum = target_sum - available_bills_and_coins[1]
            ten_occ += 1
            denominator_occurrences.update({"10": ten_occ})
        elif target_sum - available_bills_and_coins[2] > 0:
            target_sum = target_sum - available_bills_and_coins[2]
            five_occ += 1
            denominator_occurrences.update({"5": five_occ})
        elif target_sum - available_bills_and_coins[3] > 0:
            target_sum = target_sum - available_bills_and_coins[3]
            one_occ += 1
            denominator_occurrences.update({"1": one_occ})
        elif target_sum - available_bills_and_coins[4] > 0:
            target_sum = target_sum - available_bills_and_coins[4]
            quarter_occ += 1
            denominator_occurrences.update({"0.25": quarter_occ})
        elif target_sum - available_bills_and_coins[5] > 0:
            target_sum = target_sum - available_bills_and_coins[5]
            dime_occ += 1
            denominator_occurrences.update({"0.1": dime_occ})
        elif target_sum - available_bills_and_coins[6] > 0:
            target_sum = target_sum - available_bills_and_coins[6]
            nickel_occ += 1
            denominator_occurrences.update({"0.05": nickel_occ})
        elif target_sum - available_bills_and_coins[7] > 0:
            target_sum = target_sum - available_bills_and_coins[7]
            penny_occ += 1
            denominator_occurrences.update({"0.01": penny_occ})
        else:
            target_sum = 0

    return denominator_occurrences


if __name__ == '__main__':
    print(calculate_min_denominations(6.35))
