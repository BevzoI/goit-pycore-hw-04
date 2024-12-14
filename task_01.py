import re
from os import path

def total_salary(file_path: str):
    # Check if the file exists
    if not path.exists(file_path):
        return None, "File does not exist"
    
    # Initialize variables
    total = 0
    counter = 0

    # Read the file
    try:
        with open(file=file_path, mode='r', encoding='utf-8') as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                
                # Match line against regex
                match = re.match(r'([\w\s]+),(\d+)', line)
                if not match:
                    return None, f"Invalid line format: {line}"
                
                # Extract name and salary
                _, salary = match.groups()
                
                try:
                    total += int(salary)
                    counter += 1
                except ValueError:
                    return None, f"Invalid salary value: {salary}"
        
        # Calculate average
        if counter == 0:
            return None, "No valid data found"
        
        average = total / counter
        return total, "{:.2f}".format(average)
    
    except Exception as e:
        return None, f"Error reading file: {e}"

# Usage example
total, result = total_salary('task_01_file.txt')
if total is None:
    print(f"Функція закінчилась з помилкою: {result}")
else:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {result}")
