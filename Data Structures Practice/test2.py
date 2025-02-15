import numpy as np

def interquartile(values):
    # Calculate the first (Q1) and third (Q3) quartiles
    sorted_values = np.sort(values)
    Q1 = np.percentile(sorted_values, 25)
    Q3 = np.percentile(sorted_values, 75)
    print(Q1)
    print(Q3)
    
    # Calculate the Interquartile Range (IQR)
    IQR = Q3 - Q1
    
    # Calculate lower and upper bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Print the results
    print(f"Lower bound: {lower_bound}")
    print(f"Upper bound: {upper_bound}")

# Test the function with the given values
values = [15, 175, 80, 34, 23, 12, -95, 74, 56, 9, 65]
interquartile(values)