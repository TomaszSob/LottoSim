# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 21:40:40 2019

@author: tomek
"""

from tkinter import *
import random


class Window:

    def __init__(self, master):

        canvas = Canvas(master, height=500, width=600)
        canvas.pack()

        #todo backbroud_image = PhotoImage(file='.'

        frame = Frame(master, bg='#80c1ff')
        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        own_nums_entry = Entry(frame, font=40)
        own_nums_entry.grid(row=0, columnspan=2)

        draw_num_entry = Entry(frame, font=40)
        draw_num_entry.grid(row=1, column=0)

        self.start_button = Button(frame, text="Start", fg="green", command=lambda: calc_lottery(int(draw_num_entry.get())))
        self.start_button.grid(row=1, column=1)

        #todo 3 fields Entry, 1 field for own numbers and go button
        #todo own numbers if left empty - random numbers
        #todo add labels to Entry fields, and/or hover mouse info

        lower_frame = Frame(master, bg='#80c1ff', bd=10)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        self.the_label_6 = Label(lower_frame, text='...')
        self.the_label_6.pack()

#todo add button for all 3 variables
# draws_qty = 10
lottery_no_range = 49
no_of_numbers = 6


# Draw 6 random numbers in range 1-49
def lottery_draw(n):
    for _ in range(n):
        yield set(random.sample(range(1, lottery_no_range + 1), no_of_numbers))


def calc_lottery(entry):
    # Your numbers - also random
    your_random_numbers = set(random.sample(range(1, lottery_no_range + 1), no_of_numbers))

    print('\n')

    lottery_no = 0
    no_of_6 = 0
    no_of_5 = 0
    no_of_4 = 0
    no_of_3 = 0
    win_lottery_no = []

    for draw in lottery_draw(entry):

        lottery_no += 1
        intersection_length = len(draw.intersection(your_random_numbers))

        if intersection_length == 6:
            no_of_6 += 1
            win_lottery_no.append(lottery_no)
        elif intersection_length == 5:
            no_of_5 += 1
        elif intersection_length == 4:
            no_of_4 += 1
        elif intersection_length == 3:
            no_of_3 += 1

    # Test Func
    myWindow.the_label_6['text'] = f'number of 6: {no_of_6}' \
        f'\nnumber of 5: {no_of_5}' \
        f'\nnumber of 4: {no_of_4}' \
        f'\nnumber of 3: {no_of_3}'

    return [no_of_3, no_of_4, no_of_5, no_of_6, win_lottery_no]


root = Tk()
myWindow = Window(root)
root.mainloop()

# todo redo whole GUI with place() insted of grid()
# todo add entry fields to variables (with default 6 in 49)
# todo display simulation results in years, days etc
# todo add button to switch between own numbers and random
# todo add func to this button
# todo add field to enter own numbers or "tick" random
