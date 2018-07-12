from random import random
from math import sqrt

chance = 0.05
tries = 10000.0
successes = 0.0
nrolls = 0
history = ""

while nrolls < tries:
    if random() < chance:
        history = history + "#"
        successes += 1
    else:
        history = history + "."
    nrolls += 1

def annotate_streak_history(history):
    streak = 1
    streak_history = []
    i = 0
    failcount = 0
    while i < len(history):
        if history[i] == "#":
            streak_history.append(failcount)
            failcount = 0
            streak += 1
        else:
            failcount += 1
        i += 1
    return streak_history

def average_streak(l):
    return sum(l) / len(l)

def stdev(l):
    n = len(l)
    mu = average_streak(l)
    sigma = 0.0
    for xi in l:
        sigma += (xi - mu)**2
    return sqrt((1.0/n) * sigma)

print(history)

streak_history = annotate_streak_history(history)

for nfailures in streak_history:
    print("({:3}) {}".format(nfailures, "#" * nfailures))

print("\nOut of {} tries we got {} successes for a {}% chance (ratio {})".format(
    int(tries), successes, chance*100, successes/tries
    )
)

avg = average_streak(streak_history)
sd = stdev(streak_history)

ZAX = 425 # astral diamonds per zen
def diamonds_per_ward(exchange_rate):
    return 10*exchange_rate

print("\nleast failures in a row: {}".format(min(streak_history)))
print("most failures in a row: {}".format(max(streak_history)))
print("average failure streak: {}".format(avg))
print("standard deviation of failures in a streak: {:.3f}".format(sd))
print("\nso budget for about {} preservation wards (about {} diamonds).".format(
    int(avg+sd), diamonds_per_ward(ZAX) * int(avg+sd)
))
