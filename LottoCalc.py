# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:32:13 2019

@author: tomek
"""

# Program sprawdzający prawdopodobieństwo wygranaj w totka
# Simple app to check probability of winning in lottery

import random


class LottoDraw:
    def __init_(self, draws_qty = 1000, lottery_no_range = 49, no_of_numbers = 6):
        self.draws_qty = draws_qty
        self.lottery_no_range = lottery_no_range
        self.no_of_numbers = no_of_numbers

    # Draw 6 random numbers in range 1-49
    def lottery_draw(n):
        for _ in range(n):
            yield set(random.sample(range(1, lottery_no_range + 1), no_of_numbers))

    def calc_lottery():

        # Your numbers - also random
        your_random_numbers = set(random.sample(range(1, lottery_no_range + 1), no_of_numbers))

        print(your_random_numbers)
        print('\n')

        lotteryNo = 0
        no_of_6 = 0
        no_of_5 = 0
        no_of_4 = 0
        no_of_3 = 0
        win_lottery_no = []

        for draw in lottery_draw(draws_qty):  # Change magic number to variable(int)

            lotteryNo += 1
            intersection_length = len(draw.intersection(your_random_numbers))

            if intersection_length == 6:
                no_of_6 += 1
                win_lottery_no.append()
            elif intersection_length == 5:
                no_of_5 += 1
            elif intersection_length == 4:
                no_of_4 += 1
            elif intersection_length == 3:
                no_of_3 += 1
        return [no_of_3, no_of_4, no_of_5, no_of_6, win_lottery_no]




    # Zamienić iloc losowań na dni, miesiące, lata (wygrałes po ... latach)
    # Dodać interfejs graficzny

