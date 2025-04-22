import pandas as pd

df = pd.read_csv('students.csv')
df['Total'] = df[['Subject1', 'Subject2', 'Subject3']].sum(axis=1)
student_dict = df.to_dict(orient='records')

for record in student_dict:
    print(record)
