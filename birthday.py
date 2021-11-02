import random

def has_duplicates(ss):
    aa = sorted(ss)
    for ii in range(len(aa)-1):
        if aa[ii] == aa[ii+1]:
            return True
    return False

# loop through until the probability doesn't change to 2 dp

flag = 0
counter1 = 0.
counter2 = 0.
currentprobability = -1
savedprobability = -1
cp = "{:.2%}"
sp = "{:.2%}"

while flag < 10:
    counter2 += 1
    # make a list of 23 random birthdays in a year with replacement
    random_list = []
    for ii in range(0, 23):
        # any random numbers from 0 to 1000
        random_list.append(random.randint(1, 366))

    # if one of the birthdays is the same save to counter
    if has_duplicates(random_list):
        counter1 += 1
    random_list.sort()

    currentprobability = counter1 / counter2

    if cp.format(currentprobability) == sp.format(savedprobability):
        flag += 1
    else:
        flag = 0

    if counter2 !=1:
        savedprobability = currentprobability

print('The probability of a duplicate birthday is '+sp.format(savedprobability))
