# This program generates a set of 1000 knapsack instances with specific properties to ensure algorithmic hardness
# the size of the instances varies from 20 to 1,000,000 items
# Each instance is saved in an Excel files named 'kp_instances_<num_items>_cap_<capacity>  .xlsx'
# All instances will be saved in a folder named 'kp_instances'

import numpy as np
import os
import openpyxl as pxl

def generate_knapsack_instance(num_items, seed):
    # Set random seed for reproducibility
    np.random.seed(seed)
    # Generate weights clustered around a base value, with some large outliers
    base_weight = max(1, int(10 + num_items))
    weights = np.random.randint(base_weight, base_weight * 4, size=num_items)
    # Add a few very heavy items to make the instance harder
    heavy_items = np.random.choice(num_items, size=max(1, num_items // 10), replace=False)
    for idx in heavy_items:
        weights[idx] = np.random.randint(base_weight * 5, base_weight * 8)
    # Generate values that are not proportional to weights, but with some correlation and noise
    values = weights + np.random.randint(-base_weight, base_weight * 2, size=num_items)
    values = np.maximum(values, 1)  # Ensure all values are positive
    # Set capacity to be a fraction of the total weight (e.g., 40% of total weight)
    for i in range(num_items):
        weights[i] = weights[i]/100
        values[i] = values[i]/100
    capacity = int(weights.sum() * 0.05)
    return weights, values, capacity


# Create directory for instances if it doesn't exist
output_dir = 'kp_instances'
# os.makedirs(output_dir, exist_ok=True)  

# 📌 Linearly spaced number of items: from 20 to 1,000,000
num_instances = 50
#instances_sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
instances_sizes = [100, 200, 500, 1000, 1500, 2000, 2500, 3000, 4000, 5000]
# 📌 Generate and save instances
base_seed = 42

for i, num_items in enumerate(instances_sizes):
    for j in range(num_instances // len(instances_sizes)):
        seed = base_seed + i * (num_instances // len(instances_sizes)) + j
        weights, values, capacity = generate_knapsack_instance(num_items, seed)
        file_name = f'kp_instances_{num_items}_cap_{capacity}_seed_{seed}.xlsx'
        workbook = pxl.Workbook()
        worksheet = workbook.active
        worksheet.append(['Weight', 'Value', 'Capacity'])
        for item in range(num_items):
            if item == 0:
                worksheet.append([weights[item], values[item], capacity])
            else:
                worksheet.append([weights[item], values[item]])
        workbook.save(os.path.join(output_dir, file_name))
        print(f"Saved instance with {num_items} items to {os.path.join(output_dir, file_name)}")

# Rename all generate files to remove capacity and seed from their names
# start from small size files to large size files
# add at the fist of the name the index of the file starting from 0001 to 1000

for i, filename in enumerate(sorted(os.listdir(output_dir), key=lambda x: int(x.split('_')[2])), start=1):
    if filename.endswith('.xlsx'):
        parts = filename.split('_')
        if len(parts) >= 4:
            new_filename = f"{i:04d}_{parts[0]}_{parts[1]}_{parts[2]}.xlsx"
            os.rename(os.path.join(output_dir, filename), os.path.join(output_dir, new_filename))
            print(f"Renamed {filename} to {new_filename}")
        

