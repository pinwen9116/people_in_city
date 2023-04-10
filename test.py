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
    while len(xs) < 100:
        who = random.randint(0, len(people) - 1)
        if who not in xs:
            xs.append(people[who])
            xs2[people[who] - 1] += 1
    return xs, xs2

def mean_x(xs, xs2):
    avg = 0
    for i in range(len(xs2)):
        xs2[i] /= (i+1)
        avg += xs2[i]*(i+1)
    return statistics.mean(xs), avg / sum(xs2)

ans_sum = 0
res_sum = 0
res2_sum = 0
# 5 iter
for i in range(10):
    city, people, ans = test_case(10000) # suppose there are 1000 houses in town
    xs, xs2 = sample(people)
    res, res2 = mean_x(xs, xs2)
    ans_sum += ans
    res_sum += res
    res2_sum += res2
    print(f"The correct answer is: {ans}, the estimated number is: {res}, the adjested number is: {res2}")

print(f"Average difference between:{(res_sum - ans_sum) / 10}, while adjusted difference is: {(res2_sum - ans_sum) / 5}")