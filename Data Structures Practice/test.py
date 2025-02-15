import numpy as np

outliers = []
#data = [43, 14, -66, 54, 49, 32, 9, 140, 51, 81, 21]
data = [15, 175, 80, 34, 23, 12, -95, 74, 56, 9, 65]

sorted_data = np.sort(data)
print(sorted_data)

Q1 = np.percentile(sorted_data, 25)
Q3 = np.percentile(sorted_data, 75)
print("Q1 is %.1f"%(Q1))
print(Q3)

IQR = Q3 - Q1
print(IQR)

lower_bound = Q1 - 1.5 * IQR 
upper_bound = Q3 + 1.5 * IQR

print(lower_bound)
print(upper_bound)

for x in data:
    if (x < lower_bound) or (x > upper_bound):
        outliers.append(x)

print(outliers)