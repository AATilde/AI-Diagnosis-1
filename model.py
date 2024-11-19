import numpy as np # linear algebra
import pandas as pd
import os

'''
data_path = os.path.join(os.getcwd(), "Skin_Data")
print(f"Looking in: {data_path}")

for root, dirs, files in os.walk(data_path):
    print(f"Root: {root}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")

data = []
for root, dirs, files in os.walk(data_path):
    for file in files:
        if file.endswith(('.jpg', '.png', '.jpeg')):
            file_path = os.path.join(root, file)
            # Assign default labels based on 'cancer' or 'non_cancer' presence
            label = "cancer" if "cancer" in root.lower() else "non_cancer"
            data.append((file_path, label))

data = pd.DataFrame(data, columns=["file dir", "cancer type"])
print(f"DataFrame Shape: {data.shape}")
print(data.head())

print(data.shape)
'''

data_path = os.path.join(os.getcwd(), "Skin_Data")
print(f"Looking in: {data_path}")

data = []
for root, dirs, files in os.walk(data_path):
    print(f"Root: {root}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")
    for file in files:
        # Check for image files (case-insensitive)
        if file.lower().endswith(('.jpg', '.png', '.jpeg')):
            file_path = os.path.join(root, file)
            # Assign labels based on folder names
            if "cancer" in root.lower():
                label = "cancer"
            elif "non_cancer" in root.lower():
                label = "non_cancer"
            else:
                label = "unknown"
            data.append((file_path, label))

# Create DataFrame
data = pd.DataFrame(data, columns=["file dir", "cancer type"])
print(f"DataFrame Shape: {data.shape}")
print(data.head())
