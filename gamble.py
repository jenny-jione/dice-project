# 주사위 던지기: 원하는 숫자가 나올 때까지 던져야 하는 평균횟수를 계산하는 프로그램
# 21-09-15
# 22-12-31
# dataframe, 기댓값

import random
import numpy as np
import collections
import pandas as pd


dice = [ 1, 2, 3, 4, 5, 6 ]

# 원하는 숫자(this_num) 나올 때까지의 시행횟수 구하기
def count_implement(this_num):
    count = 0
    while(True):
        result = random.choice(dice)
        count = count + 1
        if result == this_num:
            return count


def get_average(implement_list: list):
    return sum(implement_list) / len(implement_list)


def get_median(implement_list: list):
    return np.median(implement_list)


if __name__ == "__main__":

    # 1000번 시행해서 각각의 시행횟수 저장
    result = []

    for i in range(1000):
        cnt = count_implement(1)
        result.append(cnt)
    

    # 시행횟수의 평균값, 중앙값 구하기
    avg = get_average(result)
    med = get_median(result)

    max_trial = max(result)

    # 리스트 요소의 빈도수 세기
    count_counter = collections.Counter(result)
    count_dict = dict(count_counter)
    data = collections.OrderedDict(sorted(count_dict.items()))

    trial = list(data.keys())
    frequency = list(data.values())

    # Trial만에 나올 확률
    probablity = []
    for f in frequency:
        probablity.append(f/1000)
    
    
    # 데이터프레임
    df = pd.DataFrame({
        "Trial": trial,
        "Frequency": frequency,
        "Probability": probablity
    })

    print(df)

    # 기댓값 구하기
    expected_value = 0

    for i in range(len(df)):
        x = df.loc[i]['Trial']
        p = df.loc[i]['Probability']
        e_val = x * p
        expected_value = expected_value + e_val


    print("average : ", avg)
    print("median  : ", med)
    max_frequency = max(frequency)
    print("max frequency : ", max_frequency, ", ", trial[frequency.index(max_frequency)])
    print("max trial : ", max_trial)
    print("expected_val : ", round(expected_value, 2))
