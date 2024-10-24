#%% Series, Dataframe
import pandas as pd
ser = pd.Series(data=[1,2,3],index=['a','b','c'])
print(ser)
print(ser['a'])

d = {'col1':[1,2],'col2':[3,4]}
df = pd.DataFrame(data=d)
print(df['col1'])
print(df['col1'][0])

