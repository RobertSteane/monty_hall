# import random function for shuffling and random integer generation
import random

# initialise doors list
doors = ["goat", "goat", "car"]

# initialise trackers of how many cars are won by each strategy
switch_cars = 0
no_switch_cars = 0

# Simulate 1000 strategy choices
for i in range(1000):
    # randomise what is behind each door
    random.shuffle(doors)
    # choose a door randomly
    initial_choice = random.randint(0, 2)
    # reveal a goat behind a door you haven't picked
    revealed_goat = next(i for i in range(3) if doors[i] == "goat" and i != initial_choice)
    # not switching is your initial choice
    not_switch = doors[initial_choice]
    # switching is choosing a door that wasn't your initial choice and wasn't the revealed goat
    switch = doors[next(i for i in range(3) if i != initial_choice and i != revealed_goat)]

    # increase the appropriate tracker if that strategy choose a car
    if switch == "car":
        switch_cars += 1

    if not_switch == "car":
        no_switch_cars += 1

# print the results
print("The number of cars won by switching was " + str(switch_cars))
print("The number of cars won by not switching was " + str(no_switch_cars))
