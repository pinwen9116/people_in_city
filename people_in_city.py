import random
import statistics
import math

def test_case(houses):
    city = []
    people = []
    sum = 0
    for i in range(houses):
        house = random.randint(1,10)
        city.append(house)
        for h in range(house):
            people.append(house)
        sum += house
    return city, people, sum/houses

def sample(people):
    xs = []
    xs2 = [0 for i in range(10)]
    for i in range(100):
        who = random.randint(0, len(people) - 1)
        xs.append(people[who])
        xs2[people[who]-1] += 1
    return xs, xs2

def mean_x(xs, xs2):
    sum = 0
    mean2 = 0
    for i in range(10):
        sum += xs2[i] / (i+1)
    return statistics.mean(xs), sum

city, people, ans = test_case(1000) # suppose there are 1000 houses in town
xs, xs2 = sample(people)
print(xs2)
res, res2 = mean_x(xs, xs2)

print(f"The correct answer is: {ans}, the estimated number is: {res}, corrected number is: {res2}")

