# Dash 사용을 위한 데이터 변환
import numpy as np
import pandas as pd


def create_dataframe():
    # 데이터프레임 생성
    df = pd.read_csv("data/Iris.csv")

    # 데이터프레임 전처리
    # ...

    return df