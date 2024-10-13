import os
import random


folder_path = 'my_test_folder'  # Change this to your desired folder path
num_files = 10  # Change this to your desired number of files

# Step 1: Open/Make a folder
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Created folder: {folder_path}")
else:
    print(f"Folder already exists: {folder_path}")

# Step 2: Create multiple files
for i in range(num_files):
    file_path = os.path.join(folder_path, f'file_{i+1}.txt')
    with open(file_path, 'w') as f:
        f.write(f'This is file number {i+1}')

# Step 3: Check the number of files
total_files = len(os.listdir(folder_path))
print(f"Total number of files after creation: {total_files}")

# Step 4: Delete half of the files randomly
files_to_delete = random.sample(os.listdir(folder_path), total_files // 2)
for file in files_to_delete:
    os.remove(os.path.join(folder_path, file))
    print(f"Deleted: {file}")

# Step 5: Final check
remaining_files = len(os.listdir(folder_path))
print(f"Total number of files remaining: {remaining_files}")
