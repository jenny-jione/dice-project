# 주사위 100, 1000, 10000, 100000, 1000000번을 던져서 각각의 숫자가 나오는 실제 확률 계산
# 이상적인 확률(1/6)과의 차이 계산
import random
import pandas as pd
import numpy as np


dice = [1, 2, 3, 4, 5, 6]
IDEAL_PROBABILITY = 1/len(dice)

def get_difference(trial: int):
    result = {}
    for i in range(trial):
        num = random.choice(dice)
        result.setdefault(num, 0)
        result[num] += 1

    number_of_cases = []
    probabilities = []
    differences = []

    for n in dice:
        noc = result[n]     # 경우의 수, number of cases
        number_of_cases.append(noc)
        p = noc/trial
        probabilities.append(p)
        diff = abs(IDEAL_PROBABILITY - p)
        differences.append(diff)

    df = pd.DataFrame({
        "Cases": number_of_cases,
        "Probability": probabilities,
        "Difference": differences
    })

    print(df)
    
    diff_mean = np.mean(differences)
    return round(diff_mean, 5)


if __name__ == "__main__":
    trial = 10
    
    diff_list = []
    
    for i in range(5):
        print(trial)
        trial *= 10
        diff = get_difference(trial)
        diff_list.append((trial, diff))
    
    print('ideal probability:', round(IDEAL_PROBABILITY, 5))
    print(diff_list)
