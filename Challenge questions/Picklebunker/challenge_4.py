import pandas as pd

path=""
def transpose_csv(path):
    return pd.read_CSV(path).transpose()


transpose_csv(path)
