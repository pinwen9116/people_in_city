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
    for i in range(100):
        who = random.randint(0, len(people) - 1)
        xs.append(people[who])
    return xs

def mean_x(xs):
    return statistics.mean(xs)

ans_sum = 0
res_sum = 0

# 5 iter
for i in range(5):
    city, people, ans = test_case(1000) # suppose there are 1000 houses in town
    xs = sample(people)
    res = mean_x(xs)
    ans_sum += ans
    res_sum += res
    print(f"The correct answer is: {ans}, the estimated number is: {res}")

print(f"Average difference between:{(res_sum - ans_sum) / 5}")