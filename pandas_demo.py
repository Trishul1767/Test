import pandas as pd
data={
    'name':['Sai','Ram','Trishul'],
    'marks':[90,80,85],
    'age':[18,18,19]
}
df=pd.DataFrame(data)
df1=df.iloc[0]
#print(df)
print(df1)
#print(df[df['marks']>80])