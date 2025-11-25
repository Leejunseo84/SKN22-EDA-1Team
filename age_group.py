import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/train.csv')
df.head()


df = pd.DataFrame({'Age': [5, 22, 45, 67, 15, 38, 52]})

df['Age_Group'] = df['Age'].apply(
     lambda x: 'Youth' if x <= 19 else
               'Young_Adult' if x <= 39 else
               'Middle_aged' if x <= 59 else
               'Senior'
 )

 print(df)
 

 