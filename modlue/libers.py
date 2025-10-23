import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


stu_ids = np.arange(1, 101)
math_mark = np.random.randint(40, 101, 100)
science_mark = np.random.randint(35, 101, 100)
english_mark = np.random.randint(30, 101, 100)

data = {
    'stu_id': stu_ids,
    'math_mark': math_mark,
    'science_mark': science_mark,
    'english_mark': english_mark,
    'Total': math_mark + science_mark + english_mark,
    'avg': ((math_mark + science_mark + english_mark)/3).round(2)
}



df= pd.DataFrame(data)

mean_mark = df[['math_mark', 'science_mark', 'english_mark']].mean()
median_mark = df[['math_mark', 'science_mark', 'english_mark']].median()
stand_mark = df[['math_mark', 'science_mark', 'english_mark']].std()


print("\n Mean:\n", mean_mark)
print("\n Median:\n", median_mark)
print("\nStandard Deviations:\n", stand_mark)

mc = stand_mark.idxmin()

print('Subject with Highest Consistency (Lowest Std Dev):',mc)


plt.figure(figsize=(10,10))

sub = ["Math","science", "English"]

plt.bar(sub,mean_mark, color = ['blue','red','green'] )
plt.title('Average score per subject')
plt.xlabel('Subject')
plt.ylabel('Average Score')
plt.show()


df['mean_mark'] = df[['math_mark', 'science_mark', 'english_mark']].mean(axis=1)

plt.figure(figsize=(10,10))
plt.hist(df['mean_mark'],bins=100, color = 'plum' , edgecolor = 'black')
plt.title('Distribution of Students by Average Score')
plt.xlabel('Average Score')
plt.ylabel('Number of Students')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10,10))
plt.scatter(df['math_mark'], df['science_mark'], color = "red",alpha = 0.7)
plt.title("Correlation between Math and Science mark")
plt.xlabel('Math Score')
plt.ylabel('Science Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()