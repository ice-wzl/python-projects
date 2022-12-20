import matplotlib.pyplot as plt
import pandas as pd
  
# read_csv function 
data = pd.read_csv('file1.csv')
  
# display
print("Original 'file1.csv' CSV Data: \n")
print(data)
  
# pop function to delete nonsense column
data.pop('page')
  
# display
print("\nCSV Data after deleting the column 'page':\n")
print(data)

df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
print(X)
print(Y)

plt.bar(X, Y, color='b')
plt.title("Page Views")
plt.xlabel("Page Name")
plt.xticks(rotation=90)

plt.ylabel("View Count")
#plt.tight_layout()
plt.figure(constrained_layout=True)

plt.show()