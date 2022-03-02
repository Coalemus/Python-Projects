#! python3
allguests = {'Alice': {'apples': 5,'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

def totalbrought(guests, item):
    numbrought = 0
    for k, v in guests.items():
        numbrought = numbrought + v.get(item, 0)
        return numbrought

print("Number of things brought:")
print(' - apples          ' + str(totalbrought(allguests, 'apples')))
print(' - cups            ' + str(totalbrought(allguests, 'cups')))
print(' - cakes           ' + str(totalbrought(allguests, 'cakes')))
print(' - ham sandwiches  ' + str(totalbrought(allguests, 'ham sandwiches')))
print(' - apple pies      ' + str(totalbrought(allguests, 'apple pies')))

